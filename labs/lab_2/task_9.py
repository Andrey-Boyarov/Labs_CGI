from LabImage import LabImage
from LabModel import LabModel


def task_9():
    model = LabModel('resources/rabbit.obj')
    image = LabImage(50, 50)

    image.draw_triangle(-10, -20, 0, 10, 20, 5)
    image.save(2, 9, 1)
