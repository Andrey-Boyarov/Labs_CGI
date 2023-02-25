from LabImage import LabImage
from LabImage import Color
from LabModel import LabModel


def task_5():
    image = LabImage(1500, 1500)
    vertices = LabModel('resources/rabbit.obj').vertices()
    for v in vertices:
        image.set(v[0] * 5000, v[1] * 5000, Color(123, 234, 123))
    image.save(1, 5, 1)
