from LabImage import LabImage


def task_10():
    image = LabImage(50, 50)
    image.draw_triangle(-10, -20, 0, 10, 20, 5)
    image.save(2, 10, 1)

    image = LabImage(50, 50)
    image.draw_triangle(-60, -20, 0, 10, 20, 5)
    image.save(2, 10, 2)

    image = LabImage(50, 50)
    image.draw_triangle(-10, -20, 10, 10, 20, 5)
    image.save(2, 10, 3)
