import numpy as np

import toolkit


def task_1():
    _H = 512  # height
    _W = 255  # width

    mat_1 = np.zeros((_H, _W))
    toolkit.save_im(mat_1, 1, 1, 1)

    mat_2 = np.full((_H, _W), 255)
    toolkit.save_im(mat_2, 1, 1, 2)

    mat_3 = np.full((_H, _W, 3), [255, 0, 0], dtype=np.uint8)
    toolkit.save_im(mat_3, 1, 1, 3)

    mat_4 = np.zeros((_H, _W, 3), dtype=np.uint8)
    for h in range(_H):
        for w in range(_W):
            mat_4[h, w] = [h, w, h+w]
    toolkit.save_im(mat_4, 1, 1, 4)
