#!/usr/bin/python3

import argparse
import io
import sys
from copy import deepcopy
from PIL import Image

import utils

# coords of parts of mc skin
# front
FACE_HEAD = (8, 8, 16, 16)
FRONT_RIGHT_ARM = (44, 20, 48, 32)
FRONT_BODY = (20, 20, 28, 32)
FRONT_LEFT_ARM = (36, 52, 40, 64)
FRONT_RIGHT_LEG = (4, 20, 8, 32)
FRONT_LEFT_LEG = (20, 52, 24, 64)
# back
BACK_HEAD = (24, 8, 32, 16)
BACK_RIGHT_ARM = (52, 20, 56, 32)
BACK_BODY = (32, 20, 40, 32)
BACK_LEFT_ARM = (44, 52, 48, 64)
BACK_RIGHT_LEG = (12, 20, 16, 32)
BACK_LEFT_LEG = (28, 52, 32, 64)

# coords of parts of 24x32 image mapping to mc skin
IMG_HEAD = (8, 0, 16, 8)
IMG_RIGHT_ARM = (4, 8, 8, 20)
IMG_BODY = (8, 8, 16, 20)
IMG_LEFT_ARM = (16, 8, 20, 20)
IMG_RIGHT_LEG = (8, 20, 12, 32)
IMG_LEFT_LEG = (12, 20, 16, 32)

front_coords = [FACE_HEAD, FRONT_RIGHT_ARM, FRONT_BODY,
                FRONT_LEFT_ARM, FRONT_RIGHT_LEG, FRONT_LEFT_LEG]
back_coords = [BACK_HEAD, BACK_LEFT_ARM, BACK_BODY,
               BACK_RIGHT_ARM, BACK_LEFT_LEG, BACK_RIGHT_LEG]
img_coords = [IMG_HEAD, IMG_RIGHT_ARM, IMG_BODY,
              IMG_LEFT_ARM, IMG_RIGHT_LEG, IMG_LEFT_LEG]


def img2skin(img_front: Image, img_back: Image, template: Image = None) -> Image:
    """Paste `img_front` and `img_back` onto `skin`.

    Args:
        skin (Image): _description_
        img_front (Image): _description_
        img_back (Image): _description_

    Returns:
        Image: _description_
    """
    skin = deepcopy(template)
    if skin is None:
        skin = Image.fromarray(utils.template)

    img_front = img_front.resize((24, 32))
    for f_coord, i_coord in zip(front_coords, img_coords):
        img_region = img_front.crop(i_coord)
        skin.paste(img_region, f_coord)

    img_back = img_back.resize((24, 32))
    for b_coord, i_coord in zip(back_coords, img_coords):
        img_region = img_back.crop(i_coord)
        skin.paste(img_region, b_coord)

    return skin


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "front", help="Image that will be on front of the skin.")
    parser.add_argument(
        "back", help="Image that will be on back of the skin.")
    parser.add_argument(
        "-t", "--template", help="Optional skin template. If absent, a default one will be used.",
        required=False)
    parser.add_argument(
        "-o", "--out", help="File name the skin will be saved to.", required=False)
    args = parser.parse_args()

    res: Image = img2skin(Image.open(args.front), Image.open(args.back),
                          None if args.template is None else Image.open(args.template))
    if args.out is None:
        bin_res = io.BytesIO()
        res.save(bin_res, format="png")
        sys.stdout.buffer.write(bin_res.getvalue())
    else:
        res.save(args.out)
