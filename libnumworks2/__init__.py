# -*- coding: utf-8 -*-
"""
Newer implementation of NumWorks' libraries over Tkinter
"""
from tkinter import Tk

from libnumworks2.canvas import Canvas
from libnumworks2.window import build_window

active_window: Tk
active_canvas: Canvas
active_window, active_canvas = build_window()
