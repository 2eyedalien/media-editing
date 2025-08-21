from PIL import ImageOps

def invertimage(img):
    return ImageOps.invert(img.convert('RGB'))
