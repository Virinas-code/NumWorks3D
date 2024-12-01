# -*- coding: utf-8 -*-
"""
Re-exports NumWorks libraries and implement stubs for special functions
"""
from libnumworks2.modules import _fast_update  # pyright: ignore [reportPrivateUsage]
from libnumworks2.modules import _fast_use  # pyright: ignore [reportPrivateUsage]
from libnumworks2.modules import _mainloop  # pyright: ignore [reportPrivateUsage]
from libnumworks2.modules import ion, kandinsky

__all__: list[str] = ["kandinsky", "ion", "_mainloop", "_fast_update", "_fast_use"]
