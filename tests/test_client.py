from pyscrcpy import Client
import time

def make_on_frame():
    count = 0

    def on_frame(client, frame):
        nonlocal count
        #if count % 30 == 0:
        print(f"{count} {frame.shape}")
        count += 1

    return on_frame



def test_client():
    client = Client(block_frame=True, stay_awake=True, max_fps=1)
    client.on_frame(make_on_frame())
    client.start()

