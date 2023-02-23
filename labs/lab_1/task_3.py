import numpy as np

from LabImage import *


def draw_line_v1(image: LabImage, x0: int, y0: int, x1: int, y1: int):
    for t in np.arange(0., 1., .01):
        x = x0 * (1. - t) + x1 * t
        y = y0 * (1. - t) + y1 * t
        image.set(x, y, Color(100*t, 100*t+50, 100*t+100))


def draw_line_v2(image: LabImage, x0: int, y0: int, x1: int, y1: int):
    for x in np.arange(x0, x1):
        t = (x - x0)/(x1-x0)
        y = y0*(1.-t) + y1*t
        image.set(x, y, Color(100*t, 100*t+50, 100*t+100))


def draw_line_v3(image: LabImage, x0: int, y0: int, x1: int, y1: int):
    steep = False
    if abs(x0-x1) < abs(y0-y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    for x in np.arange(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = y0 * (1. - t) + y1 * t
        if steep:
            image.set(y, x, Color(100 * t, 100 * t + 50, 100 * t + 100))
        else:
            image.set(x, y, Color(100 * t, 100 * t + 50, 100 * t + 100))


def draw_line_v4(image: LabImage, x0: int, y0: int, x1: int, y1: int):
    image.draw_line(x0, y0, x1, y1)


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

    i = LabImage(h, w)
    draw_star(i, draw_line_v2)
    i.save(1, 3, 3)

    i = LabImage(h, w)
    draw_star(i, draw_line_v3)
    i.save(1, 3, 4)

    i = LabImage(h, w)
    draw_star(i, draw_line_v4)
    i.save(1, 3, 5)

