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

    def save(self, lab: int, task: int, number_of_image: int):
        toolkit.save_im(self.data, task, lab, number_of_image)
