def modifyreds(img):
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = pixels[i,j]
            pixels[i,j] = (min(255,int(r*1.5)), g, b)
    return img

def removegreens(img):
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = pixels[i,j]
            pixels[i,j] = (r,0,b)
    return img
