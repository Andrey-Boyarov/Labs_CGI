import numpy as np

from LabImage import *


def draw_line_v1(image: LabImage, x0: int, y0: int, x1: int, y1: int):
    for t in np.arange(0., 1., .01):
        x = x0 * (1. - t) + x1 * t
        y = y0 * (1. - t) + y1 * t
        image.set(x, y, Color(100*t, 100*t+50, 100*t+100))


def draw_star(image: LabImage, draw_func):
    alpha = 2 * np.pi * 0.12 / 13
    for i in range(0, 13):
        draw_func(image, 0, 0, 95*np.cos(alpha*i*8.2), 95*np.sin(alpha*i*8.2))


def task_3():
    h = 200
    w = 200

    i = LabImage(h, w)
    draw_line_v1(i, 0, 0, 40, 60)
    i.save(1, 3, 1)

    i = LabImage(h, w)
    draw_star(i, draw_line_v1)
    i.save(1, 3, 2)
