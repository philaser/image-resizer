import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Resizes images')
parser.add_argument('--path', metavar='P', type=str, dest='path',
                    help='filepath to directory where images are to be resized',
                    required=True)
parser.add_argument('--width', metavar='W', type=int, dest='width',
                    help='width to resize image to', required=True)
parser.add_argument('--height', metavar='H', type=int, dest='height',
                    help='height to resize image to', required=True)

args = parser.parse_args()

path = args.path
width = args.width
height = args.height

for file in os.listdir(path):
    filepath = os.path.join(path, file)
    try:
        image = Image.open(filepath)
        basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
    except OSError as e:
        print('Could not open file')

    try:
        new_image = image.resize((width, height))
        format = image.format
        new_image.save(f'{basename_without_ext}_{width}x{height}.{format}')
        print('image resized')
    except Exception:
        print('could not save file')

print('done')