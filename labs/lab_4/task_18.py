from LabModel import LabModel
from LabImage import LabImage
from PIL import Image


def task_18():
    model = LabModel('resources/rabbit.obj')

    # image = LabImage(1000, 1000)
    # model.draw_trianlges(image, magnification=1500)
    # image.save(3, 16, 1)
    frames = []
    for i in range(20):
    #     image = LabImage(1000, 1000)
    #     model.rotate(0, i, 0)
    #     model.draw_trianlges(image, magnification=1500)
    #     image.save(4, 18, i)
        frames.append(Image.open(fr'D:\University Projects\CGI\labs\lab_4\results\task_18_image_{i}.png'))
    #     print(f'page {i} done')

    frames[0].save(
        'rabbit.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=400,
        loop=0
    )
