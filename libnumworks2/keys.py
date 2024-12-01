# -*- coding: utf-8 -*-
"""Link between NumWorks keycodes and Tkinter."""
import tkinter as tk
from typing import Any

KEY_LEFT = 0
KEY_UP = 1
KEY_DOWN = 2
KEY_RIGHT = 3
KEY_OK = 4
KEY_BACK = 5
KEY_HOME = 6
KEY_ONOFF = 8
KEY_SHIFT = 12
KEY_ALPHA = 13
KEY_XNT = 14
KEY_VAR = 15
KEY_TOOLBOX = 16
KEY_BACKSPACE = 17
KEY_EXP = 18
KEY_LN = 19
KEY_LOG = 20
KEY_IMAGINARY = 21
KEY_COMMA = 22
KEY_POWER = 23
KEY_SINE = 24
KEY_COSINE = 25
KEY_TANGENT = 26
KEY_PI = 27
KEY_SQRT = 28
KEY_SQUARE = 29
KEY_SEVEN = 30
KEY_EIGHT = 31
KEY_NINE = 32
KEY_LEFTPARENTHESIS = 33
KEY_RIGHTPARENTHESIS = 34
KEY_FOUR = 36
KEY_FIVE = 37
KEY_SIX = 38
KEY_MULTIPLICATION = 39
KEY_DIVISION = 40
KEY_ONE = 42
KEY_TWO = 43
KEY_THREE = 44
KEY_PLUS = 45
KEY_MINUS = 46
KEY_ZERO = 48
KEY_DOT = 49
KEY_EE = 50
KEY_ANS = 51
KEY_EXE = 52

TK_TO_ION: dict[str, list[int]] = {
    "KP_0": [KEY_ZERO],
    "KP_1": [KEY_ONE],
    "KP_2": [KEY_TWO],
    "KP_3": [KEY_THREE],
    "KP_4": [KEY_FOUR],
    "KP_5": [KEY_FIVE],
    "KP_6": [KEY_SIX],
    "KP_7": [KEY_SEVEN],
    "KP_8": [KEY_EIGHT],
    "KP_9": [KEY_NINE],
    "KP_Decimal": [KEY_DOT],
    "KP_Add": [KEY_PLUS],
    "KP_Substract": [KEY_MINUS],
    "KP_Multiply": [KEY_MULTIPLICATION],
    "KP_Divide": [KEY_DIVISION],
    "KP_Enter": [KEY_EXE],
    "parenleft": [KEY_LEFTPARENTHESIS],
    "parenright": [KEY_RIGHTPARENTHESIS],
    "colon": [KEY_ALPHA, KEY_XNT],
    "semicolon": [KEY_ALPHA, KEY_VAR],
    "quotedbl": [KEY_ALPHA, KEY_TOOLBOX],
    "percent": [KEY_ALPHA, KEY_BACKSPACE],
    "space": [KEY_ALPHA, KEY_MINUS],
    "question": [KEY_ALPHA, KEY_ZERO],
    "exclam": [KEY_ALPHA, KEY_DOT],
    "bracketleft": [KEY_SHIFT, KEY_EXP],
    "bracketright": [KEY_SHIFT, KEY_LN],
    "braceleft": [KEY_SHIFT, KEY_LOG],
    "braceright": [KEY_SHIFT, KEY_IMAGINARY],
    "underscore": [KEY_SHIFT, KEY_COMMA],
    "equal": [KEY_SHIFT, KEY_PI],
    "less": [KEY_SHIFT, KEY_SQRT],
    "greater": [KEY_SHIFT, KEY_SQUARE],
    "BackSpace": [KEY_BACKSPACE],
    "Delete": [KEY_SHIFT, KEY_BACKSPACE],
    "Escape": [KEY_BACK],
    "Return": [KEY_OK],
    "Caps_Lock": [KEY_SHIFT, KEY_ALPHA],
    "Left": [KEY_LEFT],
    "Up": [KEY_UP],
    "Down": [KEY_DOWN],
    "Right": [KEY_RIGHT],
    "Shift_L": [KEY_SHIFT],
    "Shift_R": [KEY_ALPHA],
    "Insert": [KEY_TOOLBOX],
    "asterisk": [KEY_EE],
    "section": [KEY_ANS],
    "comma": [KEY_COMMA],
    "asciicircum": [KEY_POWER],
    "twosuperior": [KEY_SQUARE],
}

TK_TO_ION_ALPHABET: dict[str, int] = {
    "a": KEY_EXP,
    "b": KEY_LN,
    "c": KEY_LOG,
    "d": KEY_IMAGINARY,
    "e": KEY_COMMA,
    "f": KEY_POWER,
    "g": KEY_SINE,
    "h": KEY_COSINE,
    "i": KEY_TANGENT,
    "j": KEY_PI,
    "k": KEY_SQRT,
    "l": KEY_SQUARE,
    "m": KEY_SEVEN,
    "n": KEY_EIGHT,
    "o": KEY_NINE,
    "p": KEY_LEFTPARENTHESIS,
    "q": KEY_RIGHTPARENTHESIS,
    "r": KEY_FOUR,
    "s": KEY_FIVE,
    "t": KEY_SIX,
    "u": KEY_MULTIPLICATION,
    "v": KEY_DIVISION,
    "w": KEY_ONE,
    "x": KEY_TWO,
    "y": KEY_THREE,
    "z": KEY_PLUS,
}

for letter, keys in TK_TO_ION_ALPHABET.items():
    TK_TO_ION[letter] = [keys] + [KEY_ALPHA]
    TK_TO_ION[letter.capitalize()] = [keys] + [KEY_SHIFT, KEY_ALPHA]

pressed: dict[int, bool] = {}


def key_callback(event: Any) -> None:
    """Callback when a key is pressed."""
    if isinstance(event, tk.Event):
        if event.type == "2":
            print(event.keysym)
            pressed_keys: list[int] = TK_TO_ION.get(event.keysym, [54])
            for key in pressed_keys:
                pressed[key] = True
        if event.type == "3":
            print(event.keysym)
            pressed_keys: list[int] = TK_TO_ION.get(event.keysym, [54])
            for key in pressed_keys:
                pressed[key] = False


def keydown(k: int) -> bool:
    """
    Returns `True` if the `k` key in argument is pressed and `False` otherwise.
    """
    return pressed.get(k, False)


def register(window: tk.Tk) -> None:
    """Register event listeners for a window."""
    window.bind("<Key>", key_callback)
    window.bind("<KeyRelease>", key_callback)
