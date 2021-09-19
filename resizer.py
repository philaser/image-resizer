import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Resizes images')
parser.add_argument('--path', metavar='P', type=str, dest='path',
                    help='filepath to image to be resized', required=True)
parser.add_argument('--width', metavar='W', type=int, dest='width',
                    help='width to resize image to', required=True)
parser.add_argument('--height', metavar='H', type=int, dest='height',
                    help='height to resize image to', required=True)

args = parser.parse_args()

path = args.path
width = args.width
height = args.height

parsed_path = os.path.normpath(path)
parsed_path = parsed_path.split(os.sep)
print(parsed_path)

try:
    image = Image.open(path)
except OSError as e:
    print('Could not open file')

try:
    new_image = image.resize((width, height))
    format = image.format
    new_image.save(f'image_{width}x{height}.{format}')
    print('done')
except Exception:
    print('could not save file')

