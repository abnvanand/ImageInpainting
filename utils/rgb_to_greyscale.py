from PIL import Image
import os
import argparse


def process_dir(source, dest):
    for dirpath, dirnames, filenames in os.walk(source):
        structure = os.path.join(dest, dirpath[len(source):])
        if not os.path.isdir(structure):
            print("@@@@@@@@@@ Creating directory:", structure)
            os.mkdir(structure)

        for file in filenames:
            ifile = os.path.join(dirpath, file)
            ofile = os.path.join(dest, dirpath[len(source):], file)
            convert_file(ifile, ofile)


def convert_file(ifile, ofile):
    print("converting:", ifile, "to greyscale.")
    img = Image.open(ifile).convert('L')  # L:greyscale
    img.save(ofile)
    print("wrote file at:", ofile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to convert rgb to greyscale image.')
    parser.add_argument('--source', help='Source file/dir name', required=True)
    parser.add_argument('--dest', help='Destination file/dir name', required=True)
    args = parser.parse_args()
    source = args.source
    dest = args.dest
    if os.path.isdir(source):
        process_dir(source, dest)
    else:
        convert_file(source, dest)
