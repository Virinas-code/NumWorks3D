# -*- coding: utf-8 -*-
"""Additional features not in the base NumWorks"""
from libnumworks2 import active_canvas, active_window

__all__: list[str] = ["_fast_use", "_fast_update", "_mainloop"]


def _fast_use() -> None:
    active_canvas.fast_mode = True


def _fast_update() -> None:
    active_canvas.canvas.update()


def _mainloop() -> None:
    active_window.mainloop()
