import pywavefront


class LabModel:
    def __init__(self, file_name: str):
        self.scene = pywavefront.Wavefront(file_name, create_materials=True)
