from LabModel import LabModel
from LabImage import LabImage


def task_11():
    model = LabModel('resources/rabbit.obj')
    image = LabImage(1000, 1000)
    model.draw_trianlges(image, step=0.1, magnification=3000)
    image.save(2, 11, 1)
