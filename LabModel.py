import collections

import pywavefront

from LabImage import Color, LabImage


class LabModel:
    def __init__(self, file_name: str):
        self.scene = pywavefront.Wavefront(file_name, create_materials=True, collect_faces=True)

    def vertices(self) -> collections.Iterable:
        return self.scene.vertices

    def faces(self) -> collections.Iterable:
        return self.scene.mesh_list[0].faces

    def draw_faces(self, image: LabImage, color: Color, magnification=1):
        vertices = self.vertices()
        for face in self.faces():
            dot_1_index = face[0]
            dot_2_index = face[1]
            dot_3_index = face[2]
            image.draw_line(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            color,
                            magnification=magnification)
            image.draw_line(vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            color,
                            magnification=magnification)
            image.draw_line(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            color,
                            magnification=magnification)
