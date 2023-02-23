import os
import numpy as np
from PIL import Image as im


def create_results_folder(lab: int):
    create_folder_if_not_exists(f'labs/lab_{lab}/results')


def create_folder_if_not_exists(path: str):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def save_im(data: np.ndarray, task: int, lab: int, number_of_image: int):
    if lab > 4 or lab < 1:
        raise ValueError('Wrong lab input: ', lab)
    if task > 18 or task < 1:
        raise ValueError('Wrong task: ', task)
    if task < 1:
        raise ValueError('Wrong number of image: ', number_of_image)
    create_results_folder(lab)
    if len(data.shape) < 2:
        data = im.fromarray(data)
    else:
        data = im.fromarray(data).convert('RGB')
    data.save(f'labs/lab_{lab}/results/task_{task}_image_{number_of_image}.png')
