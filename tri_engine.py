# -*- coding: utf-8 -*-
"""
A 3D engine for the NumWorks calculator.

Based on [Computer Graphics from Scratch]
(https://gabrielgambetta.com/computer-graphics-from-scratch/06-lines.html).
"""
from math import floor
from typing import Literal

from numworks import (
    kandinsky as kd,
    _fast_update,  # pyright: ignore [reportPrivateUsage]
    _fast_use,  # pyright: ignore [reportPrivateUsage]
)

RED: tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE: tuple[int, int, int] = (0, 0, 255)
YELLOW: tuple[int, int, int] = (255, 255, 0)
CYAN: tuple[int, int, int] = (0, 255, 255)
PURPLE: tuple[int, int, int] = (255, 0, 255)

CW: Literal[320] = 320
CH: Literal[222] = 222

VW = 1
VH = 1
D: Literal[1] = 1

_fast_use()


class Point:
    """A single point."""

    def __init__(self, x: int, y: int, h: float = 1.0) -> None:
        self.x: int = x
        self.y: int = y
        self.h: float = h


class Vertex:
    """A single 3D vertex."""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z


class Triangle:
    """A single 3D triangle."""

    def __init__(self, v0: int, v1: int, v2: int, color: tuple[int, int, int]) -> None:
        self.v: tuple[int, int, int] = (v0, v1, v2)
        self.color: tuple[int, int, int] = color


def interpolate(i0: int, d0: float, i1: int, d1: float) -> list[float]:
    """Interpolation."""
    if i0 == i1:
        return [d0]
    values: list[float] = []
    a: float = (d1 - d0) / (i1 - i0)
    d: float = d0
    for _ in range(i0, i1):
        values.append(d)
        d = d + a
    return values


def draw_line(p0: Point, p1: Point, color: tuple[int, int, int]) -> None:
    """Draw a line between `p0` and `p1` of colorr `color`."""
    if abs(p1.x - p0.x) > abs(p1.y - p0.y):
        # Line is horizontal-ish
        # Make sure x0 < x1
        if p0.x > p1.x:
            p0, p1 = p1, p0
        ys: list[float] = interpolate(p0.x, p0.y, p1.x, p1.y)
        for x in range(p0.x, p1.x):
            kd.set_pixel(x, int(ys[x - p0.x]), color)
    else:
        # Line is vertical-ish
        # Make sure y0 < y1
        if p0.y > p1.y:
            p0, p1 = p1, p0
        xs: list[float] = interpolate(p0.y, p0.x, p1.y, p1.x)
        for y in range(p0.y, p1.y):
            kd.set_pixel(int(xs[y - p0.y]), y, color)


def draw_wireframe_triangle(
    p0: Point, p1: Point, p2: Point, color: tuple[int, int, int]
) -> None:
    """Draw a wireframe triangle between `p0`, `p1` and `p2` with an outline of color `color`."""
    draw_line(p0, p1, color)
    draw_line(p1, p2, color)
    draw_line(p2, p0, color)


def draw_filled_triangle(
    p0: Point, p1: Point, p2: Point, color: tuple[int, int, int]
) -> None:
    """Draw a filled triangle between `p0`, `p1` and `p2` with a fill color `color`."""
    # Sort the points so that y0 <= y1 <= y2
    if p1.y < p0.y:
        p1, p0 = p0, p1
    if p2.y < p0.y:
        p2, p0 = p0, p2
    if p2.y < p1.y:
        p2, p1 = p1, p2

    # Compute the x coordinates of the triangle edges
    x01: list[float] = interpolate(p0.y, p0.x, p1.y, p1.x)
    x12: list[float] = interpolate(p1.y, p1.x, p2.y, p2.x)
    x02: list[float] = interpolate(p0.y, p0.x, p2.y, p2.x)

    # Concatenate the short sides
    # del x01[-1]
    x012: list[float] = x01 + x12

    # Determine which is left and which is right
    m: int = floor(len(x012) / 2)
    x_left: list[float]
    x_right: list[float]
    if x02[m] < x012[m]:
        x_left = x02
        x_right = x012
    else:
        x_left = x012
        x_right = x02

    # Draw the horizontal segments
    for y in range(p0.y, p2.y):
        for x in range(int(x_left[y - p0.y]), int(x_right[y - p0.y])):
            kd.set_pixel(x, y, color)


def draw_shaded_triangle(
    p0: Point, p1: Point, p2: Point, color: tuple[int, int, int]
) -> None:
    """Draw a filled triangle between `p0`, `p1` and `p2` with a fill color `color` (shaded)."""
    # Sort the points so that y0 <= y1 <= y2
    if p1.y < p0.y:
        p1, p0 = p0, p1
    if p2.y < p0.y:
        p2, p0 = p0, p2
    if p2.y < p1.y:
        p2, p1 = p1, p2

    # Compute the x coordinates and h values of the triangle edges
    x01: list[float] = interpolate(p0.y, p0.x, p1.y, p1.x)
    h01: list[float] = interpolate(p0.y, p0.h, p1.y, p1.h)

    x12: list[float] = interpolate(p1.y, p1.x, p2.y, p2.x)
    h12: list[float] = interpolate(p1.y, p1.h, p2.y, p2.h)

    x02: list[float] = interpolate(p0.y, p0.x, p2.y, p2.x)
    h02: list[float] = interpolate(p0.y, p0.h, p2.y, p2.h)

    # Concatenate the short sides
    # del x01[-1]
    x012: list[float] = x01 + x12

    # del h01[-1]
    h012: list[float] = h01 + h12

    # Determine which is left and which is right
    m: int = floor(len(x012) / 2)

    x_left: list[float]
    h_left: list[float]

    x_right: list[float]
    h_right: list[float]
    if x02[m] < x012[m]:
        x_left = x02
        h_left = h02

        x_right = x012
        h_right = h012
    else:
        x_left = x012
        h_left = h012

        x_right = x02
        h_right = h02

    # Draw the horizontal segments
    for y in range(p0.y, p2.y):
        x_l: float = x_left[y - p0.y]
        x_r: float = x_right[y - p0.y]

        h_segment: list[float] = interpolate(
            int(x_l), h_left[y - p0.y], int(x_r), h_right[y - p0.y]
        )
        for x in range(int(x_l), int(x_r)):
            shaded_color: tuple[int, int, int] = (
                int(color[0] * h_segment[int(x - x_l)]),
                int(color[1] * h_segment[int(x - x_l)]),
                int(color[2] * h_segment[int(x - x_l)]),
            )
            kd.set_pixel(x, y, shaded_color)


def viewport_to_canvas(x: float, y: float) -> Point:
    """
    Convert from viewport coordinates to canvas coordinates.
    Re-centers coordinates from upper-left origin to center origin.
    """
    return Point(int(x * CW / VW + (CW / 2)), int(y * CH / VH + (CW / 2)))


def project_vertex(v: Vertex) -> Point:
    """Project a vertex."""
    return viewport_to_canvas(v.x * D / v.z, v.y * D / v.z)


def render_object(vertices: list[Vertex], triangles: list[Triangle]) -> None:
    """Render a single object made out of triangles."""
    projected: list[Point] = []
    for v in vertices:
        projected.append(project_vertex(v))
    for t in triangles:
        render_triangle(t, projected)


def render_triangle(triangle: Triangle, projected: list[Point]) -> None:
    """Render a single triangle."""
    draw_wireframe_triangle(
        projected[triangle.v[0]],
        projected[triangle.v[1]],
        projected[triangle.v[2]],
        triangle.color,
    )


# The four "front" vertices
vAf: Vertex = Vertex(-2, -0.5, 5)
vBf: Vertex = Vertex(-2, 0.5, 5)
vCf: Vertex = Vertex(-1, 0.5, 5)
vDf: Vertex = Vertex(-1, -0.5, 5)

# The four "back" vertices
vAb: Vertex = Vertex(-2, -0.5, 6)
vBb: Vertex = Vertex(-2, 0.5, 6)
vCb: Vertex = Vertex(-1, 0.5, 6)
vDb: Vertex = Vertex(-1, -0.5, 6)

cube_vertices: list[Vertex] = [
    Vertex(1, 1, 1),
    Vertex(-1, 1, 1),
    Vertex(-1, -1, 1),
    Vertex(1, -1, 1),
    Vertex(1, 1, -1),
    Vertex(-1, 1, -1),
    Vertex(-1, -1, -1),
    Vertex(1, -1, -1),
]

CUBE_TRIANGLES: list[Triangle] = [
    Triangle(0, 1, 2, RED),
    Triangle(0, 2, 3, RED),
    Triangle(4, 0, 3, GREEN),
    Triangle(4, 3, 7, GREEN),
    Triangle(1, 5, 6, YELLOW),
    Triangle(1, 6, 2, YELLOW),
    Triangle(4, 5, 1, PURPLE),
    Triangle(4, 1, 0, PURPLE),
    Triangle(2, 6, 7, CYAN),
    Triangle(2, 7, 3, CYAN),
    Triangle(5, 4, 7, BLUE),
    Triangle(5, 7, 6, BLUE),
]

while True:
    kd.fill_rect(0, 0, 320, 222, (255, 255, 255))

    # The back face
    draw_line(project_vertex(vAb), project_vertex(vBb), RED)
    draw_line(project_vertex(vBb), project_vertex(vCb), RED)
    draw_line(project_vertex(vCb), project_vertex(vDb), RED)
    draw_line(project_vertex(vDb), project_vertex(vAb), RED)

    # The front-to-back edges
    draw_line(project_vertex(vAf), project_vertex(vAb), GREEN)
    draw_line(project_vertex(vBf), project_vertex(vBb), GREEN)
    draw_line(project_vertex(vCf), project_vertex(vCb), GREEN)
    draw_line(project_vertex(vDf), project_vertex(vDb), GREEN)

    # The front face
    draw_line(project_vertex(vAf), project_vertex(vBf), BLUE)
    draw_line(project_vertex(vBf), project_vertex(vCf), BLUE)
    draw_line(project_vertex(vCf), project_vertex(vDf), BLUE)
    draw_line(project_vertex(vDf), project_vertex(vAf), BLUE)

    draw_line(Point(10, 10), Point(20, 60), (255, 0, 0))
    draw_line(Point(20, 60), Point(120, 90), (0, 255, 0))
    draw_line(Point(120, 90), Point(10, 10), (0, 0, 255))

    draw_wireframe_triangle(Point(40, 100), Point(80, 10), Point(200, 50), (0, 0, 0))
    draw_shaded_triangle(
        Point(40, 100, 1.0),
        Point(80, 10, 0.3),
        Point(200, 50, 0.7),
        (255, 255, 0),
    )
    draw_wireframe_triangle(Point(40, 100), Point(80, 10), Point(200, 50), (0, 0, 0))

    draw_wireframe_triangle(Point(200, 200), Point(160, 90), Point(210, 210), (0, 0, 0))
    draw_filled_triangle(
        Point(200, 200), Point(160, 90), Point(210, 210), (255, 0, 255)
    )
    draw_wireframe_triangle(Point(200, 200), Point(160, 90), Point(210, 210), (0, 0, 0))

    cube_vertices: list[Vertex] = [
        Vertex(1, 1, 1),
        Vertex(-1, 1, 1),
        Vertex(-1, -1, 1),
        Vertex(1, -1, 1),
        Vertex(1, 1, -1),
        Vertex(-1, 1, -1),
        Vertex(-1, -1, -1),
        Vertex(1, -1, -1),
    ]

    for index, vertex in enumerate(cube_vertices):
        cube_vertices[index] = Vertex(vertex.x - (1.5), vertex.y, vertex.z + (7))

    render_object(cube_vertices, CUBE_TRIANGLES)

    _fast_update()
