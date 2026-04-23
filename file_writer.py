from abstract_writer import AbstractWriter

class FileWriter(AbstractWriter):

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, ascii_2d):
        result = ""
        for row in ascii_2d:
            result += "".join(char * 2 for char in row) + "\n"

        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(result)