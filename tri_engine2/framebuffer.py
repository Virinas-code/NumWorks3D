# -*- coding: utf-8 -*-
"""Custom frame implementation."""
from copy import copy

from numworks import kandinsky


class Framebuffer:
    """The framebuffer holding the previous and current frame."""

    def __init__(self) -> None:
        self.previous_frame: list[list[tuple[int, int, int]]] = [
            [(255, 255, 255) for _ in range(320)] for _ in range(222)
        ]
        self.current_frame: list[list[tuple[int, int, int]]] = [
            [(255, 255, 255) for _ in range(320)] for _ in range(222)
        ]

    def next_frame(self) -> None:
        """Replace the previous frame with the current frame, drawing it on the screen"""
        for x in range(320):
            for y in range(222):
                previous_pixel: tuple[int, int, int] = self.previous_frame[y][x]
                current_pixel: tuple[int, int, int] = self.current_frame[y][x]
                if previous_pixel != current_pixel:
                    kandinsky.set_pixel(x, y, current_pixel)

        self.previous_frame = copy(self.current_frame)
        self.current_frame: list[list[tuple[int, int, int]]] = [
            [(255, 255, 255) for _ in range(320)] for _ in range(222)
        ]

    def set_pixel(self, x: int, y: int, color: tuple[int, int, int]) -> None:
        """Change a pixel in the current place"""
        self.current_frame[y][x] = color
