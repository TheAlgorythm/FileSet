import argparse
import difflib


class FileDiff:

    def diffText(self, file1, file2) -> str:
        txt1 = ''
        with file1 as f:
            txt1 = f.readlines()
        txt2 = ''
        with file2 as f:
            txt2 = f.readlines()
        text = ''
        for line in difflib.unified_diff(txt1, txt2):
            text += line
        return text

    def diffTextToBool(self, file1, file2) -> bool:
        txt1 = ''
        with file1 as f:
            txt1 = f.readlines()
        txt2 = ''
        with file2 as f:
            txt2 = f.readlines()
        
        return txt1 == txt2


class App:

    @staticmethod
    def argumentParser():
        parser = argparse.ArgumentParser(description='Generate Files')

        parser.add_argument('File1', type=argparse.FileType('r'))
        parser.add_argument('File2', type=argparse.FileType('r'))
        parser.add_argument('-type', default='text', choices=['text', 'binary'], help='Type of diff')

        return parser

    @staticmethod
    def exec(args):
        fd = FileDiff()
        if args.type == 'text':
            print(fd.diffText(args.File1, args.File2))
        elif args.type == 'binary':
            print(fd.diffTextToBool(args.File1, args.File2))


if __name__ == '__main__':
    parser = App.argumentParser()
    args = parser.parse_args()
    App.exec(args)
