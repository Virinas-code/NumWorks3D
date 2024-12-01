# -*- coding: utf-8 -*-
"""Main entrypoint creating the window and registering it."""
import sys
import tkinter as tk

from libnumworks2.canvas import Canvas
from libnumworks2.keys import register


def build_window() -> tuple[tk.Tk, Canvas]:
    """Build the Tkinter window"""
    win = tk.Tk()

    def leave() -> None:
        win.destroy()
        sys.exit()

    win.wm_protocol("WM_DELETE_WINDOW", leave)
    win.wm_resizable(False, False)
    win.wm_title("PYTHON")

    register(win)

    canvas: Canvas = Canvas(win)

    return (win, canvas)
