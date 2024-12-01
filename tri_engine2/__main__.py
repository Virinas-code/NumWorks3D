# -*- coding: utf-8 -*-
"""Sample program."""
import random

from tri_engine2.framebuffer import Framebuffer

fb: Framebuffer = Framebuffer()

while True:
    for _ in range(random.randint(0, 50)):
        fb.set_pixel(
            random.randint(0, 319),
            random.randint(0, 221),
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        )
    fb.next_frame()
