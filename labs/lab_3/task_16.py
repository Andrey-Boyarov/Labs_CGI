from LabModel import LabModel
from LabImage import LabImage


def task_16():
    model = LabModel('resources/rabbit.obj')

    # image = LabImage(1000, 1000)
    # model.draw_trianlges(image, magnification=1500)
    # image.save(3, 16, 1)

    image = LabImage(1000, 1000)
    model.bend(10, 10, 0.15, 0.15, 0.01)
    model.draw_trianlges(image, magnification=1500)
    image.save(3, 16, 2)
