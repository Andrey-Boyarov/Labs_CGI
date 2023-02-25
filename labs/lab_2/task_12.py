from LabModel import LabModel
from LabImage import LabImage


def task_12():
    model = LabModel('resources/rabbit.obj')
    print(model.normals())
