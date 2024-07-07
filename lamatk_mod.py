#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from lamatk_modui import lamatkUI


class lamatk(lamatkUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = lamatk()
    app.run()
