# -*- coding: utf-8 -*-
"""
This is the description of the `ion` module. You can get this list on your calculator by
pressing *toolbox* and going to **Modules** then **ion**.

The other items in this menu indicate the syntax used to identify the keys on the keyboard.
"""
# flake8: noqa
# pylint: disable=unused-argument,redefined-outer-name

from typing import Literal as _Literal

def keydown(k: int) -> bool:
    """
    Returns `True` if the `k` key in argument is pressed and `False` otherwise.
    """

KEY_LEFT: _Literal[0]
KEY_UP: _Literal[1]
KEY_DOWN: _Literal[2]
KEY_RIGHT: _Literal[3]
KEY_OK: _Literal[4]
KEY_BACK: _Literal[5]
KEY_HOME: _Literal[6]
KEY_ONOFF: _Literal[8]
KEY_SHIFT: _Literal[12]
KEY_ALPHA: _Literal[13]
KEY_XNT: _Literal[14]
KEY_VAR: _Literal[15]
KEY_TOOLBOX: _Literal[16]
KEY_BACKSPACE: _Literal[17]
KEY_EXP: _Literal[18]
KEY_LN: _Literal[19]
KEY_LOG: _Literal[20]
KEY_IMAGINARY: _Literal[21]
KEY_COMMA: _Literal[22]
KEY_POWER: _Literal[23]
KEY_SINE: _Literal[24]
KEY_COSINE: _Literal[25]
KEY_TANGENT: _Literal[26]
KEY_PI: _Literal[27]
KEY_SQRT: _Literal[28]
KEY_SQUARE: _Literal[29]
KEY_SEVEN: _Literal[30]
KEY_EIGHT: _Literal[31]
KEY_NINE: _Literal[32]
KEY_LEFTPARENTHESIS: _Literal[33]
KEY_RIGHTPARENTHESIS: _Literal[34]
KEY_FOUR: _Literal[36]
KEY_FIVE: _Literal[37]
KEY_SIX: _Literal[38]
KEY_MULTIPLICATION: _Literal[39]
KEY_DIVISION: _Literal[40]
KEY_ONE: _Literal[42]
KEY_TWO: _Literal[43]
KEY_THREE: _Literal[44]
KEY_PLUS: _Literal[45]
KEY_MINUS: _Literal[46]
KEY_ZERO: _Literal[48]
KEY_DOT: _Literal[49]
KEY_EE: _Literal[50]
KEY_ANS: _Literal[51]
KEY_EXE: _Literal[52]
