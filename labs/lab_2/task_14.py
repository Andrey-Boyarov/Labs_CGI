from LabModel import LabModel
from LabImage import LabImage


def task_14():
    model = LabModel('resources/rabbit.obj')
    image = LabImage(1000, 1000)
    model.draw_trianlges(image, magnification=3000)
    image.save(2, 14, 1)
