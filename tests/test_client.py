from scrcpy import Client


def resolution(client, frame):
    print(frame.shape)


def test_client():
    client = Client(block_frame=True)
    client.on_frame(resolution)
    client.start()
