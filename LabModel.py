import collections
import random

import numpy as np
import pywavefront

import toolkit
from LabImage import Color, LabImage


class LabModel:
    def __init__(self, file_name: str):
        self.scene = pywavefront.Wavefront(file_name, create_materials=True, collect_faces=True)

    def vertices(self) -> collections.Iterable:
        return self.scene.vertices

    def faces(self) -> collections.Iterable:
        return self.scene.mesh_list[0].faces

    def normals(self) -> collections.Iterable:
        vertices = self.vertices()
        result = []
        for face in self.faces():
            dot_1_index = face[0]
            dot_2_index = face[1]
            dot_3_index = face[2]
            normal = toolkit.normal(vertices[dot_1_index][0],
                            vertices[dot_1_index][1],
                            vertices[dot_1_index][2],
                            vertices[dot_2_index][0],
                            vertices[dot_2_index][1],
                            vertices[dot_2_index][2],
                            vertices[dot_3_index][0],
                            vertices[dot_3_index][1],
                            vertices[dot_3_index][2])
            result.append(normal)
        return result


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

    def draw_trianlges(self, image: LabImage, step=0.3, color=None, magnification=1):
        vertices = self.vertices()
        faces = self.faces()
        normals = self.normals()
        for i in range(len(faces)):
            face = faces[i]
            normal = normals[i]
            cos = toolkit.find_cos(normal)
            if cos < 0:
                dot_1_index = face[0]
                dot_2_index = face[1]
                dot_3_index = face[2]
                image.draw_triangle(vertices[dot_1_index][0],
                                    vertices[dot_1_index][1],
                                    vertices[dot_2_index][0],
                                    vertices[dot_2_index][1],
                                    vertices[dot_3_index][0],
                                    vertices[dot_3_index][1],
                                    step,
                                    Color(255 * -cos, 0, 0) if color is None else color,
                                    magnification=magnification)
