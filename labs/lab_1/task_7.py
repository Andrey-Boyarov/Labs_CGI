from LabModel import LabModel
from LabImage import LabImage
from LabImage import Color


def task_7():
    image = LabImage(10000, 7500)
    model = LabModel('resources/rabbit.obj')
    model.draw_faces(image, color=Color(255, 255, 255),  magnification=50000)
    image.save(1, 7, 1)
