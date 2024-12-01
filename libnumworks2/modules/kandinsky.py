# -*- coding: utf-8 -*-
"""Functions of the kandinsky module."""
from typing import Callable as __Callable
from typing import Optional as __Optional

from libnumworks2 import active_canvas as __active_canvas
from libnumworks2.canvas import Color


def color(r: int, g: int, b: int) -> Color:
    """
    Defines the color from the values of `r`,`g`,`b`. You can also simply use a tuple to define a
    color: `(r,g,b)`.
    """
    return (r, g, b)


get_pixel: __Callable[[int, int], Color] = __active_canvas.get_pixel
set_pixel: __Callable[[int, int, Color], None] = __active_canvas.set_pixel
fill_rect: __Callable[[int, int, int, int, Color], None] = __active_canvas.fill_rect
draw_string: __Callable[[str, int, int, __Optional[Color], __Optional[Color]], None] = (
    __active_canvas.draw_string
)
