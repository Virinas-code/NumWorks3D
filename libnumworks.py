# -*- coding: utf-8 -*-
"""
This is the complete description of the `kandinsky` module. You can get this list on your
calculator by pressing *toolbox* and going to **Modules** then **kandinsky**.
"""
import tkinter as tk
from typing import Any as __Any, Optional as __Optional

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

# Character: Width=10 Height=18
# Constants from NumWorks
__WIDTH: int = 320
__HEIGHT: int = 222

# _TK_TO_ION: dict[str, list[int]] = {
#     "Left": [KEY_LEFT],
#     "Up": [KEY_UP],
#     "Down": [KEY_DOWN],
#     "Right": [KEY_RIGHT],
#     "Return": [KEY_OK],
#     "KP_Enter": [KEY_EXE],
#     "Escape": [KEY_BACK],
#     "Home": [KEY_HOME],
#     "twosuperior": [KEY_HOME],
#     "KP_0": [KEY_ZERO],
#     "Control_L": [KEY_SHIFT],
#     "Shift_L": [KEY_SHIFT],
#     "Shift_R": [KEY_ALPHA],
#     "dollar": [KEY_XNT],
#     "x": [KEY_XNT, KEY_TWO],
#     "colon": [KEY_ALPHA, KEY_XNT],
#     "ugrave": [KEY_VAR],
#     "c": [KEY_VAR, KEY_LOG],
#     "semicolon": [KEY_ALPHA, KEY_VAR],
#     "Insert": [KEY_TOOLBOX],
#     "quotedbl": [KEY_ALPHA, KEY_TOOLBOX],
#     "v": [KEY_TOOLBOX, KEY_DIVISION],
#     "BackSpace": [KEY_BACKSPACE],
#     "percent": [KEY_ALPHA, KEY_BACKSPACE],
#     "Delete": [KEY_SHIFT, KEY_BACKSPACE],
# }

__TK_TO_ION: dict[str, list[int]] = {
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

__TK_TO_ION_ALPHABET: dict[str, int] = {
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

__fast_mode: bool = False


def _fast_use() -> None:  # pyright: ignore [reportUnusedFunction]
    global __fast_mode  # pylint: disable=global-statement
    __fast_mode = True


for __letter, __keys in __TK_TO_ION_ALPHABET.items():
    __TK_TO_ION[__letter] = [__keys] + [KEY_ALPHA]
    __TK_TO_ION[__letter.capitalize()] = [__keys] + [KEY_SHIFT, KEY_ALPHA]

__pixels: list[list[tuple[int, int, int]]] = [[(0, 0, 0)] * __WIDTH] * __HEIGHT
__pressed: dict[int, bool] = {}

__window = tk.Tk()


def __quit() -> None:
    __window.destroy()
    exit()  # pylint: disable=consider-using-sys-exit


__window.wm_protocol("WM_DELETE_WINDOW", __quit)
__window.wm_resizable(False, False)
__window.wm_title("PYTHON")


def _fast_mainloop() -> None:  # pyright: ignore [reportUnusedFunction]
    __window.mainloop()


__canvas = tk.Canvas(
    __window,
    width=__WIDTH,
    height=__HEIGHT,
    bg="#FFFFFF",
    insertwidth=0,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
)
__canvas.pack()


def _fast_update() -> None:  # pyright: ignore [reportUnusedFunction]
    if __fast_mode:
        __canvas.update()


def __c(rgb: tuple[int, int, int]) -> str:
    """
    Convert an RGB tuple to an hexadecimal color.
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def __key_callback(event: __Any) -> None:
    if isinstance(event, tk.Event):
        if event.type == "2":
            print(event.keysym)
            keys: list[int] = __TK_TO_ION.get(event.keysym, [54])
            for key in keys:
                __pressed[key] = True
            print(__pressed)
        if event.type == "3":
            print(event.keysym)
            keys: list[int] = __TK_TO_ION.get(event.keysym, [54])
            for key in keys:
                __pressed[key] = False
            print(__pressed)


def keydown(k: int) -> bool:
    """
    Returns `True` if the `k` key in argument is pressed and `False` otherwise.
    """
    return __pressed.get(k, False)


__window.bind("<Key>", __key_callback)
__window.bind("<KeyRelease>", __key_callback)


def color(r: int, g: int, b: int) -> tuple[int, int, int]:
    """
    Defines the color from the values of `r`,`g`,`b`. You can also simply use a tuple to define a
    color: `(r,g,b)`.
    """
    return (r, g, b)


def get_pixel(x: int, y: int) -> tuple[int, int, int]:
    """
    Returns the pixel `x`,`y` color as a tuple `(r,g,b)`.
    """
    return __pixels[y][x]


# pylint: disable=redefined-outer-name
def set_pixel(x: int, y: int, color: tuple[int, int, int]) -> None:
    """
    Colors the pixel `x`,`y` of the `color` color.
    """
    # _pixels[y][x] = color
    try:
        __canvas.create_line(x, y, x + 1, y, fill=__c(color))
    except tk.TclError:
        exit()  # pylint: disable=consider-using-sys-exit
    if not __fast_mode:
        __canvas.update()


def draw_string(
    text: str,
    x: int,
    y: int,
    color1: __Optional[tuple[int, int, int]] = None,
    color2: __Optional[tuple[int, int, int]] = None,
) -> None:
    """
    Displays text from the pixel `x`,`y`. The arguments `color1` (text color) and `color2`
    (background color) are optional.
    """
    __canvas.create_rectangle(
        x,
        y,
        x + len(text) * 10,
        y + 18,
        outline="",
        fill=__c(color2 if color2 is not None else (255, 255, 255)),
    )
    __canvas.create_text(
        x,
        y,
        text="test",
        font=("Source Pixel Large", 12, "normal"),
        anchor="nw",
        fill=__c(color1 if color1 is not None else (0, 0, 0)),
    )
    if not __fast_mode:
        __canvas.update()
    # _turtle.setposition(x, y)
    # shape_name = f"text[{len(text)}]"
    # if shape_name not in _screen.getshapes():
    #     shape: tuple[tuple[int, int], ...] = (
    #         (0, 0),
    #         (18, 0),
    #         (18, len(text) * 10),
    #         (0, len(text) * 10),
    #     )
    #     _screen.register_shape(shape_name, shape)
    # _turtle.shape(shape_name)
    # _turtle.color(color2 if color2 is not None else (255, 255, 255))
    # _turtle.stamp()
    # _turtle.shape("pixel")
    # _turtle.color(color1 if color1 is not None else (0, 0, 0))
    # _turtle.write(text, False, "left", ("Source Pixel Large", 12, "normal"))


def fill_rect(
    x: int, y: int, width: int, height: int, color: tuple[int, int, int]
) -> None:
    """
    Fills a rectangle at pixel `(x,y)` with the color `color`.
    """
    __canvas.create_rectangle(x, y, x + width, y + height, outline="", fill=__c(color))
    if not __fast_mode:
        __canvas.update()


if __name__ == "__main__":
    set_pixel(10, 10, (0, 255, 0))
    set_pixel(11, 11, (0, 255, 0))
    set_pixel(0, 0, (0, 0, 0))
    set_pixel(319, 221, (0, 0, 0))
    set_pixel(60, 60, (0, 255, 0))
    draw_string("test", 60, 60, (255, 0, 0), (0, 0, 255))
    set_pixel(60, 60, (0, 255, 0))
    fill_rect(120, 100, 75, 42, (255, 0, 255))

    __window.mainloop()
