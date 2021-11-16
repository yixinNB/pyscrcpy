from pathlib import Path
import socket
import struct
import threading
import time
from time import sleep
from typing import Any, Callable, Optional, Tuple, Union

import numpy as np
import numpy.typing as npt

from adbutils import AdbDevice, AdbError, Network, _AdbStreamConnection, adb
from av.codec import CodecContext

from .const import EVENT_FRAME, EVENT_INIT, LOCK_SCREEN_ORIENTATION_UNLOCKED
from .control import ControlSender

Frame = npt.NDArray[np.int8]

VERSION = "1.20"
HERE = Path(__file__).resolve().parent
JAR = HERE / f"scrcpy-server.jar"


class Client:
    def __init__(
        self,
        device: Optional[Union[AdbDevice, str]] = None,
        max_size: int = 0,
        bitrate: int = 8000000,
        max_fps: int = 0,
        block_frame: bool = False,
        stay_awake: bool = False,
        lock_screen_orientation: int = LOCK_SCREEN_ORIENTATION_UNLOCKED,
    ):
        """
        Create a scrcpy client.
        This client won't be started until you call .start()

        Args:
            device: Android device, select first one if none, from serial if str
            max_size: frame width that will be broadcast from android server
            bitrate: bitrate
            max_fps: maximum fps, 0 means not limited (supported after android 10)
            block_frame: only return nonempty frames, may block cv2 render thread
            stay_awake: keep Android device awake
            lock_screen_orientation: lock screen orientation, LOCK_SCREEN_ORIENTATION_*
        """

        if device is None:
            device = adb.device_list()[0]
        elif isinstance(device, str):
            device = adb.device(serial=device)

        self.device = device
        self.listeners = dict(frame=[], init=[])

        # User accessible
        self.last_frame: Optional[np.ndarray] = None
        self.resolution: Optional[Tuple[int, int]] = None
        self.device_name: Optional[str] = None
        self.control = ControlSender(self)

        # Params
        self.max_size = max_size
        self.bitrate = bitrate
        self.max_fps = max_fps
        self.block_frame = block_frame
        self.stay_awake = stay_awake
        self.lock_screen_orientation = lock_screen_orientation

        # Need to destroy
        self.alive = False
        self.__server_stream: Optional[_AdbStreamConnection] = None
        self.__video_socket: Optional[socket.socket] = None
        self.control_socket: Optional[socket.socket] = None
        self.control_socket_lock = threading.Lock()

    def __init_server_connection(self) -> None:
        """
        Connect to android server, there will be two sockets, video and control
        socket. This method will set: video_socket, control_socket, resolution
        variables
        """
        for _ in range(30):
            try:
                self.__video_socket = self.device.create_connection(
                    Network.LOCAL_ABSTRACT, "scrcpy"
                )
                break
            except AdbError:
                sleep(0.1)
                pass
        else:
            raise ConnectionError(
                "Failed to connect scrcpy-server after 3 seconds"
            )

        dummy_byte = self.__video_socket.recv(1)
        if not len(dummy_byte):
            raise ConnectionError("Did not receive Dummy Byte!")

        self.control_socket = self.device.create_connection(
            Network.LOCAL_ABSTRACT, "scrcpy"
        )
        self.device_name = (
            self.__video_socket.recv(64).decode("utf-8").rstrip("\x00")
        )
        if not len(self.device_name):
            raise ConnectionError("Did not receive Device Name!")

        res = self.__video_socket.recv(4)
        self.resolution = struct.unpack(">HH", res)
        self.__video_socket.setblocking(False)

    def __deploy_server(self) -> None:
        """
        Deploy server to android device
        """
        cmd = [
            "CLASSPATH=/data/local/tmp/scrcpy-server.jar",
            "app_process",
            "/",
            "com.genymobile.scrcpy.Server",
            VERSION,  # Scrcpy server version
            "info",  # Log level: info, verbose...
            f"{self.max_size}",  # Max screen width (long side)
            f"{self.bitrate}",  # Bitrate of video
            f"{self.max_fps}",  # Max frame per second
            f"{self.lock_screen_orientation}",  # Lock screen orientation: LOCK_SCREEN_ORIENTATION
            "true",  # Tunnel forward
            "-",  # Crop screen
            "false",  # Send frame rate to client
            "true",  # Control enabled
            "0",  # Display id
            "false",  # Show touches
            "true" if self.stay_awake else "false",  # Stay awake
            "-",  # Codec (video encoding) options
            "-",  # Encoder name
            "false",  # Power off screen after server closed
        ]
        self.device.push(JAR, "/data/local/tmp/")
        self.__server_stream = self.device.shell(cmd, stream=True)

    def start(self, threaded: bool = False) -> None:
        """
        Start listening video stream

        Args:
            threaded: Run stream loop in a different thread to avoid blocking
        """
        assert self.alive is False

        self.__deploy_server()
        self.__init_server_connection()
        self.alive = True
        for func in self.listeners[EVENT_INIT]:
            func(self)

        if threaded:
            threading.Thread(target=self.__stream_loop).start()
        else:
            self.__stream_loop()

    def stop(self) -> None:
        """
        Stop listening (both threaded and blocked)
        """
        self.alive = False
        if self.__server_stream is not None:
            self.__server_stream.close()
        if self.control_socket is not None:
            self.control_socket.close()
        if self.__video_socket is not None:
            self.__video_socket.close()

    def __stream_loop(self) -> None:
        """
        Core loop for video parsing
        """
        codec = CodecContext.create("h264", "r")
        while self.alive:
            try:
                raw = self.__video_socket.recv(0x10000)
                for packet in codec.parse(raw):
                    for frame in codec.decode(packet):
                        frame = frame.to_ndarray(format="bgr24")
                        self.last_frame = frame
                        self.resolution = (frame.shape[1], frame.shape[0])
                        for func in self.listeners[EVENT_FRAME]:
                            func(self, frame)
            except BlockingIOError:
                time.sleep(0.01)
                if not self.block_frame:
                    for func in self.listeners[EVENT_FRAME]:
                        func(self, None)
            except OSError as e:
                if self.alive:
                    raise e

    def on_init(self, func: Callable[[Client], None]) -> None:
        """
        Add funtion to on-init listeners.
        Your function is run after client.start() is called.

        Args:
            func: callback to be called after the server starts.

        Returns:
            The list of on-init callbacks.

        """
        self.listeners[EVENT_INIT].append(func)
        return self.listeners[EVENT_INIT]

    def on_frame(self, func: Callable[[Client, Frame], None]):
        """
        Add functoin to on-frame listeners.
        Your function will be run on every valid frame recived.

        Args:
            func: callback to be called on every frame.

        Returns:
            The list of on-frame callbacks.
        """
        self.listeners[EVENT_FRAME].append(func)
        return self.listeners[EVENT_FRAME]
