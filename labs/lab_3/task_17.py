from LabModel import LabModel
from LabImage import LabImage


def task_17():
    model = LabModel('resources/rabbit.obj')

    # image = LabImage(1000, 1000)
    # model.draw_trianlges(image, magnification=1500)
    # image.save(3, 16, 1)

    image = LabImage(1000, 1000)
    model.rotate(0, 30, 0)
    model.draw_trianlges(image, magnification=1500)
    image.save(3, 17, 1)
