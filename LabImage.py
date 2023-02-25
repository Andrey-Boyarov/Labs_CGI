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

    def draw_line(self, x0: int, y0: int, x1: int, y1: int, color=None, magnification=1):
        steep = False
        x0 *= magnification
        x1 *= magnification
        y0 *= magnification
        y1 *= magnification
        if abs(x0 - x1) < abs(y0 - y1):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            steep = True
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        derror = abs(dy / dx)
        error = 0
        y = y0
        for x in np.arange(x0, x1):
            t = (x - x0) / (x1 - x0)
            y = y0 * (1. - t) + y1 * t
            if steep:
                self.set(y, x, Color(100 * t, 100 * t + 50, 100 * t + 100) if color is None else color)
            else:
                self.set(x, y, Color(100 * t, 100 * t + 50, 100 * t + 100) if color is None else color)
            error += derror
            if error > .5:
                y += 1 if y1 > y0 else -1
                error -= 1.

    def draw_triangle(self, x0: float, y0: float, x1: float, y1: float, x2: float, y2: float, step=0.01, color=Color(255, 255, 255)):
        xmin = min(x0, x1, x2)
        ymin = min(y0, y1, y2)
        xmax = max(x0, x1, x2)
        ymax = max(y0, y1, y2)
        if xmin < 0 - self.width / 2:
            xmin = 0 - self.width / 2
        if ymin < 0 - self.width / 2:
            ymin = 0 - self.width / 2
        if xmax > 0 + self.width / 2:
            xmax = 0 + self.width / 2
        if ymax > 0 + self.width / 2:
            ymax = 0 + self.width / 2
        for y in np.arange(ymin, ymax, step):
            for x in np.arange(xmin, xmax, step):
                coordinates = toolkit.baricentrical(x, y, x0, y0, x1, y1, x2, y2)
                if coordinates[0] > 0 and coordinates[1] > 0 and coordinates[2] > 0:
                    self.set(x, y, color)

    def save(self, lab: int, task: int, number_of_image: int):
        toolkit.save_im(self.data, task, lab, number_of_image)
