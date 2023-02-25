import collections

import pywavefront


class LabModel:
    def __init__(self, file_name: str):
        self.scene = pywavefront.Wavefront(file_name, create_materials=True, collect_faces=True)

    def vertices(self) -> collections.Iterable:
        return self.scene.vertices

    def faces(self) -> collections.Iterable:
        return self.scene.mesh_list[0].faces
