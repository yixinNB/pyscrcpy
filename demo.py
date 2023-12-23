import time

import cv2 as cv
from scrcpy import Client


def on_frame(client, frame):
    # print(dir(client.control.text))
    client.control.text("123")
    cv.imshow('Video', frame)
    cv.waitKey(1)


if __name__ == '__main__':
    client = Client(max_fps=1, max_size=900)
    client.on_frame(on_frame)
    client.start()
