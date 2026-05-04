from abstract_writer import AbstractWriter

class FileWriter(AbstractWriter):

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, ascii_2d):
        result = ""
        for row in ascii_2d:
            line = ""
            for (char, r, g, b) in row:
                line = line + char * 2
            result += line + "\n"

        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(result)