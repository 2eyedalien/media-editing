import random

def addrandomnoise(img):
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            if random.random() < 0.05:
                pixels[i,j] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return img

def overlap(img1,img2):
    img2 = img2.resize(img1.size)
    pixels1, pixels2 = img1.load(), img2.load()
    for i in range(img1.width):
        for j in range(img1.height):
            r1,g1,b1 = pixels1[i,j]
            r2,g2,b2 = pixels2[i,j]
            pixels1[i,j] = ((r1+r2)//2,(g1+g2)//2,(b1+b2)//2)
    return img1
