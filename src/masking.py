from PIL import ImageOps, ImageDraw

def blackandwhiteradius(img, radius):
    img = img.convert('L')
    mask = ImageOps.invert(img)
    draw = ImageDraw.Draw(mask)
    w,h = img.size
    draw.ellipse((w//2-radius,h//2-radius,w//2+radius,h//2+radius), fill=255)
    img.paste(0, mask=mask)
    return img
