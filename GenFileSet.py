import argparse
import string
import random
import math


class FileGenerator:

    def generate(self, length, chars):
        return ''.join(random.choice(chars) for x in range(length))

    def text(self, length):
        return self.generate(length, string.ascii_letters + string.digits + string.punctuation + string.printable + string.whitespace)

    def generateFile(self, file, size):
        text = ''
        if size <= 256:
            text = self.text(size)
        else:
            appendingText = self.text(256)
            for i in range(math.ceil(size / 256)):
                text += appendingText
            text = text[0:size]
        with file as f:
            f.write(text)


class App:

    @staticmethod
    def argumentParser():
        parser = argparse.ArgumentParser(description='Generate Files')

        parser.add_argument('File', type=argparse.FileType('w'))
        parser.add_argument('Filesize', type=int)
        parser.add_argument('-unit', default='B', choices=['B', 'KiB', 'MiB', 'GiB'], help='Unit of the Filesize')

        return parser

    @staticmethod
    def exec(args):
        size = args.Filesize
        unit = args.unit
        if unit == 'KiB':
            size *= 1024
        elif unit == 'MiB':
            size *= 1024 * 1024
        elif unit == 'GiB':
            size *= 1024 * 1024 * 1024
        fg = FileGenerator()
        fg.generateFile(args.File, size)


if __name__ == '__main__':
    parser = App.argumentParser()
    args = parser.parse_args()
    App.exec(args)
