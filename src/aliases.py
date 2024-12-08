"""MIT License

Copyright (c) 2024 Bananchiki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import math
from random import randint

def int_input() -> int:
    """Function for getting number input. Exists for compatibility with python. The actual code is still INPUT."""
    return int(input())

def color(value: int) -> None:
    """Set color of next graphical elements. Dummy function. Used as an alias for COLOR in PBasic.

    Args:
        value (`int`): Index of a value. Must be in range from 1 to 16.

    Raises:
        ValueError: Color value out of range.
    """

    if value not in range(1, 17):
        raise ValueError('Color value out of range.')

def fill(x: int, y: int, fill_color: int) -> None:
    """Fill a closed contour of pixels with a specific color. Dummy function. Used as an alias for FILL in PBasic.

    Args:
        x (`int`): X coordinate.
        y (`int`): Y coordinate.
        fill_color (`int`): color index. Must be in range from 1 to 16.

    Raises:
        ValueError: Fill_color value out of range.
    """

    if fill_color not in range(1, 17):
        raise ValueError('Color value out of range.')

def cls() -> None:
    """Clear screen. Dummy function. Used as an alias for CLS in PBasic."""

def sin(value: int | float) -> float:
    """Return the sin of a value. Used as an alias for SIN in PBasic.

    Args:
        value (`int`): A value to find sin of.

    Returns:
        `float`: sin of a value.
    """

    return math.sin(value)

def cos(value: int | float) -> float:
    """Return the cos of a value. Used as an alias for COS in PBasic.

    Args:
        value (`int` | `float`): A value to find cos of.

    Returns:
        `float`: cos of a value.
    """

    return math.cos(value)

def tan(value: int | float) -> float:
    """Return the tan of a value. Used as an alias for TAN in PBasic.

    Args:
        value (`int`): A value to find tan of.

    Returns:
        `float`: tan of a value.
    """

    return math.tan(value)

def rnd(value: int) -> int:
    """Generate a random number between 1 and value, including both end points. Used as an alias for RND in PBasic.

    Returns:
        `int`: Random integer from range.
    """

    return randint(1, value)

def background(value: int) -> None:
    """Set the background color. Dummy function. Used as an alias for BACKGROUND in PBasic.

    Args:
        value (`int`): Index of a value. Must be in range from 1 to 16.

    Raises:
        ValueError: Color value out of range.
    """

    if value not in range(1, 17):
        raise ValueError('Color value out of range.')

def plot(x: int, y: int) -> None:
    """Create a point at the given coordinates. Dummy function. Used as an alias for PLOT in PBasic.

    Args:
        x (`int`): X coordinate.
        y (`int`): Y coordinate.
    """

def line(x1: int, y1: int, x2: int, y2: int) -> None:
    """Create a line from point (x1, y1) to the point (x2, y2). Dummy function, used as an alias for LINE in PBasic."""

def circle(x: int, y: int, radius: int) -> None:
    """Create a circle at point (x, y) with the given radius. Dummy function, used as an alias for CIRCLE in PBasic.

    Args:
        x (`int`): X coordinate.
        y (`int`): Y coordinate.
        radius (`int`): Radius of a circle.
    """

def beep() -> None:
    """Play beep sound. Dummy function, used as an alias for BEEP in PBasic."""