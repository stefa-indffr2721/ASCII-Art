from abstract_writer import AbstractWriter

class ConsoleWriter(AbstractWriter):
    def write(self, ascii_2d):
        for row in ascii_2d:
            print("".join(char*2 for char in row))