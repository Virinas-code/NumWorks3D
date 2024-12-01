# -*- coding: utf-8 -*-
"""
Re-exports NumWorks libraries and implement stubs for special functions

Stub for the emulator / the calculator
"""
from typing import Callable
import kandinsky
import ion


def __identity() -> None:
    pass


_fast_mainloop: Callable[[], None] = __identity
_fast_update: Callable[[], None] = __identity
_fast_use: Callable[[], None] = __identity


__all__: list[str] = ["kandinsky", "ion", "_fast_mainloop", "_fast_update", "_fast_use"]
