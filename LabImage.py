import numpy as np

import toolkit


class Color:
    def __init__(self, r, g, b):
        self.arr = [int(r), int(g), int(b)]


class LabImage:
    def __init__(self, height: int, width: int, data: np.ndarray = None):
        self.height = height
        self.width = width
        if data is not None:
            self.data = data
        else:
            self.data = np.zeros((height, width, 3), dtype=np.uint8)

    def set_initially(self, x, y, color: Color):
        self.data[int(y), int(x)] = color.arr

    def set(self, x, y, color: Color):
        self.set_initially(x + (int(self.width / 2)), (-1 * y) + (int(self.height / 2)), color)

    def draw_line(self, x0: int, y0: int, x1: int, y1: int):
        steep = False
        if abs(x0 - x1) < abs(y0 - y1):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            steep = True
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        derror = abs(dy/dx)
        error = 0
        y = y0
        for x in np.arange(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = y0 * (1. - t) + y1 * t
            if steep:
                self.set(y, x, Color(100 * t, 100 * t + 50, 100 * t + 100))
            else:
                self.set(x, y, Color(100 * t, 100 * t + 50, 100 * t + 100))
            error += derror
            if error > .5:
                y += 1 if y1 > y0 else -1
                error -= 1.

    def save(self, lab: int, task: int, number_of_image: int):
        toolkit.save_im(self.data, task, lab, number_of_image)
