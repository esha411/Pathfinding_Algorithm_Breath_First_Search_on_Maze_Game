from PIL import Image

hgt, wid = 1, 1

def imgToMatrix(img: Image) -> list:
    data = img.load()
    global hgt, wid
    hgt, wid = img.height, img.width
    outMat = [[pixToSym(data[y,x]) for x in range(img.width)] for y in range(img.height)]
    return outMat

def matrixToImg(mat: list) -> Image:
    outImg = Image.new(mode = "RGBA", size = (wid,hgt))
    data = outImg.load()
    for y in range(outImg.height):
        for x in range(outImg.width):
            data[y,x] = symToPix(mat[y][x])
    return outImg

def pixToSym(col: tuple) -> str:
    if col == (0,0,0,255):
        return 'B'
    elif col == (255,255,255,255):
        return '0'
    elif col == (233,30,99,255):
        return 'S'
    elif col == (63,81,181,255):
        return 'F'
    else:
        raise Exception("Unrecognized Color Value: "+str(col))

def symToPix(sym: str) -> tuple:
    if sym == 'B':
        return (0,0,0,255)
    elif sym == '0':
        return (255,255,255,255)
    elif sym == 'S':
        return (233,30,99,255)
    elif sym == 'F':
        return (63,81,181,255)
    elif sym == 'A':
        return (175,119,181,255)
    elif sym == 'P':
        return (77,163,46,255)
    else:
        raise Exception("Unrecognized Symbol Value: \'"+str(sym)+"\'")

def printMatrix(mat: list):
    for y in range(len(mat)):
        print(''.join(mat[y][x] for x in range(len(mat[0]))))

