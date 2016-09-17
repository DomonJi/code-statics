import os
import argparse

parser = argparse.ArgumentParser(
    description='the suffix of the codefiles', usage='readcodes.py -s <suffix> -d <directory>')
parser.add_argument("-s", "--suffixs", default='.py .js .cs .cpp .jsx .vue .html .c .css .java', type=str,
                    required=False, help="suffix of codefiles,seperate by space")
parser.add_argument("-d", "--directory", default='./', type=str,
                    required=False, help="root directory of your files")


def main(args):
    i = 0
    for root, dirs, files in os.walk(args.directory):
        suffixs = args.suffixs.split(' ')
        suffixs = ['.' + s for s in suffixs if not s.startswith('.')]
        for OneFileName in files:
            OneFullFileName = os.path.join(root, OneFileName)
            if not os.path.splitext(OneFullFileName)[1] in suffixs:
                continue
            with open(OneFullFileName) as codefile:
                try:
                    i += len(codefile.readlines())
                except Exception as e:
                    print('cannot decode : ' + OneFileName)
    print(i)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
