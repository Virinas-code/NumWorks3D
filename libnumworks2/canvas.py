# -*- coding: utf-8 -*-
"""
NumWorks canvas implementation

Implements the `kandinsky` module, may implement `matplotlib` later
"""
from copy import copy
import tkinter as tk
from typing import Any, Final, Optional

WIDTH: Final[int] = 320
HEIGHT: Final[int] = 222

SCALE: Final[int] = 1

type Color = tuple[int, int, int]


def _c(rgb: tuple[int, int, int]) -> str:
    """
    Convert an RGB tuple to an hexadecimal color.
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def _cc(hexa: str) -> tuple[int, int, int]:
    r, g, b = hexa[1:3], hexa[3:5], hexa[5:7]
    return (int(r, 16), int(g, 16), int(b, 16))


class Canvas:
    """Canvas to draw on"""

    def __init__(self, parent: tk.Tk) -> None:
        self.canvas: tk.Canvas = tk.Canvas(
            parent,
            width=320 * SCALE,
            height=222 * SCALE,
            bg="#FFFFFF",
            insertwidth=0,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.pixels: list[list[int]] = []

        for y in range(HEIGHT):
            row: list[int] = []
            for x in range(WIDTH):
                row.append(
                    self.canvas.create_rectangle(
                        x * SCALE,
                        y * SCALE,
                        x * SCALE + SCALE,
                        y * SCALE + SCALE,
                        outline="",
                        fill=_c((255, 255, 255)),
                    )
                )
            self.pixels.append(row)

        self.fast_mode: bool = False

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        """Set the color of a pixel."""
        self.canvas.itemconfig(self.pixels[y][x], fill=_c(color))

        if not self.fast_mode:
            self.canvas.update()

    def get_pixel(self, x: int, y: int) -> Color:
        """Get the color of a pixel."""
        cc: Any = self.canvas.itemcget(  # pyright: ignore [reportUnknownMemberType]
            self.pixels[y][x], "fill"
        )
        if isinstance(cc, str):
            return _cc(cc)
        raise TypeError(f"expected str, got {type(cc)}")

    def fill_rect(self, x: int, y: int, width: int, height: int, color: Color) -> None:
        """Fill a rectangle."""
        for vx in range(x, x + width):
            for vy in range(y, y + height):
                self.set_pixel(vx, vy, color)

        if not self.fast_mode:
            self.canvas.update()

    def draw_string(
        self,
        text: str,
        x: int,
        y: int,
        color1: Optional[Color] = None,
        color2: Optional[Color] = None,
    ) -> None:
        """
        Displays text from the pixel `x`,`y`. The arguments `color1` (text color) and `color2`
        (background color) are optional.
        """
        old_fast_mode = copy(self.fast_mode)
        self.fast_mode = True

        self.fill_rect(
            x,
            y,
            len(text) * 10,
            18,
            color2 if color2 is not None else (255, 255, 255),
        )
        self.canvas.create_text(
            x * SCALE,
            y * SCALE,
            text=text,
            font=("Source Pixel Large", 12 * SCALE, "normal"),
            anchor="nw",
            fill=_c(color1 if color1 is not None else (0, 0, 0)),
        )

        self.fast_mode = old_fast_mode

        if not self.fast_mode:
            self.canvas.update()
