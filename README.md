# Python Scrcpy Client
![scrcpy-badge](https://img.shields.io/badge/scrcpy-v1.20-violet)
Introduction to pyscrcpy: A Python Library for scrcpy

# Introduction
pyscrcpy is an innovative Python library designed to simplify and streamline the integration of scrcpy into your Python projects. Scrcpy, a versatile screen mirroring tool for Android devices, gains a new level of accessibility through the seamless capabilities provided by pyscrcpy.

# Key Features

1. Easy Integration: With pyscrcpy, incorporating scrcpy functionality into your Python scripts becomes a straightforward process. The library abstracts away the complexities, allowing you to focus on leveraging scrcpy's powerful features without the need for intricate setup.
2. Enhanced Control: pyscrcpy empowers developers to exert precise control over Android devices from within their Python applications. Whether it's automating UI interactions, conducting tests, or creating custom applications, pyscrcpy provides a convenient interface for managing scrcpy commands.
3. Customization Options: Tailor scrcpy behavior to suit your project's requirements using the customizable options provided by pyscrcpy. Fine-tune parameters such as display size, bit rate, and more, all while maintaining the simplicity of Python scripting.

# Demo
```python
import cv2 as cv
from pyscrcpy import Client


def on_frame(client, frame):
    client.control.text("123")
    cv.imshow('Video', frame)
    cv.waitKey(1)


if __name__ == '__main__':
    client = Client(max_fps=1, max_size=900)
    client.on_frame(on_frame)
    client.start()

```

## Reference & Appreciation
- Fork: [S1M0N38/scrcpy](https://github.com/S1M0N38/scrcpy)
- Fork: [py-scrcpy-client](https://github.com/leng-yue/py-scrcpy-client)
- Core: [scrcpy](https://github.com/Genymobile/scrcpy)
- Idea(many bugs): [py-android-viewer](https://github.com/razumeiko/py-android-viewer)
- CI: [index.py](https://github.com/index-py/index.py)
