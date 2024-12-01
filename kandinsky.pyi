# -*- coding: utf-8 -*-
"""
This is the complete description of the `kandinsky` module. You can get this list on your
calculator by pressing *toolbox* and going to **Modules** then **kandinsky**.
"""
# flake8: noqa
# pylint: disable=unused-argument,redefined-outer-name

def color(r: int, g: int, b: int) -> tuple[int, int, int]:
    """
    Defines the color from the values of `r`,`g`,`b`. You can also simply use a tuple to define a
    color: `(r,g,b)`.
    """

def get_pixel(x: int, y: int) -> tuple[int, int, int]:
    """
    Returns the pixel `x`,`y` color as a tuple `(r,g,b)`.
    """

def set_pixel(x: int, y: int, color: tuple[int, int, int]) -> None:
    """
    Colors the pixel `x`,`y` of the `color` color.
    """

def draw_string(
    text: str,
    x: int,
    y: int,
    color1: tuple[int, int, int] | None = None,
    color2: tuple[int, int, int] | None = None,
) -> None:
    """
    Displays text from the pixel `x`,`y`. The arguments `color1` (text color) and `color2`
    (background color) are optional.
    """

def fill_rect(
    x: int, y: int, width: int, height: int, color: tuple[int, int, int]
) -> None:
    """
    Fills a rectangle at pixel `(x,y)` with the color `color`.
    """
