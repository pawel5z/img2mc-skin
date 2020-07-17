from PIL import Image
import argparse

# coords of parts of mc skin
# front
FACE_HEAD = (8, 8, 16, 16)
FRONT_RA = (44, 20, 48, 32)
FRONT_BODY = (20, 20, 28, 32)
FRONT_LA = (36, 52, 40, 64)
FRONT_RL = (4, 20, 8, 32)
FRONT_LL = (20, 52, 24, 64)
# back
BACK_HEAD = (24, 8, 32, 16)
BACK_LA = (44, 52, 48, 64)
BACK_BODY = (32, 20, 40, 32)
BACK_RA = (52, 20, 56, 32)
BACK_LL = (28, 52, 32, 64)
BACK_RL = (12, 20, 16, 32)

# coords of parts of 24x32 image mapping to mc skin
IMG_HEAD = (8, 0, 16, 8)
IMG_RA = (4, 8, 8, 20)
IMG_BODY = (8, 8, 16, 20)
IMG_LA = (16, 8, 20, 20)
IMG_RL = (8, 20, 12, 32)
IMG_LL = (12, 20, 16, 32)

frontCoords = [FACE_HEAD, FRONT_RA, FRONT_BODY, FRONT_LA, FRONT_RL, FRONT_LL]
backCoords = [BACK_HEAD, BACK_LA, BACK_BODY, BACK_RA, BACK_LL, BACK_RL]
imgCoords = [IMG_HEAD, IMG_RA, IMG_BODY, IMG_LA, IMG_RL, IMG_LL]

def img2Skin(skin: Image, imgFront: Image, imgBack: Image) -> Image:
    imgFront = imgFront.resize((24, 32))
    for fCoord, iCoord in zip(frontCoords, imgCoords):
        imgRegion = imgFront.crop(iCoord)
        skin.paste(imgRegion, fCoord)

    imgBack = imgBack.resize((24, 32))
    for bCoord, iCoord in zip(backCoords, imgCoords):
        imgRegion = imgBack.crop(iCoord)
        skin.paste(imgRegion, bCoord)
    
    return skin


parser = argparse.ArgumentParser()
parser.add_argument("skinTemplate", help="skin texture into which given images will be pasted")
parser.add_argument("imgFront", help="image that will be on front of the skin")
parser.add_argument("imgBack", help="image that will be on back of the skin")
parser.add_argument("outputFile", help="file name the skin will be saved to")
args = parser.parse_args()

res = img2Skin(Image.open(args.skinTemplate), Image.open(args.imgFront), Image.open(args.imgBack))
res.save(args.outputFile)
