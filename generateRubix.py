import random

def left(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)

    temp2[0][0] = cube[3][0]
    temp2[0][1] = cube[3][1]
    temp2[1][0] = cube[0][0]
    temp2[1][1] = cube[0][1]
    temp2[2][0] = cube[1][0]
    temp2[2][1] = cube[1][1]
    temp2[3][0] = cube[2][0]
    temp2[3][1] = cube[2][1]
        
    temp2[4][0] = cube[4][2]
    temp2[4][1] = cube[4][0]
    temp2[4][2] = cube[4][3]
    temp2[4][3] = cube[4][1]
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string
    
def right(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
        
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)
        
    temp2[0][0] = cube[1][0]
    temp2[0][1] = cube[1][1]
    temp2[1][0] = cube[2][0]
    temp2[1][1] = cube[2][1]
    temp2[2][0] = cube[3][0]
    temp2[2][1] = cube[3][1]
    temp2[3][0] = cube[0][0]
    temp2[3][1] = cube[0][1]
        
    temp2[4][0] = cube[4][1]
    temp2[4][1] = cube[4][3]
    temp2[4][2] = cube[4][0]
    temp2[4][3] = cube[4][2]
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string
    
def up(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
        
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)
        
    temp2[0][0] = cube[5][0]
    temp2[0][2] = cube[5][2]
    temp2[4][0] = cube[0][0]
    temp2[4][2] = cube[0][2]
    temp2[2][3] = cube[4][0]
    temp2[2][1] = cube[4][2]
    temp2[5][0] = cube[2][3]
    temp2[5][2] = cube[2][1]
        
    temp2[1][0] = cube[1][1]
    temp2[1][1] = cube[1][3]
    temp2[1][2] = cube[1][0]
    temp2[1][3] = cube[1][2]
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string
    
def down(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
        
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)
        
    temp2[0][0] = cube[4][0]
    temp2[0][2] = cube[4][2]
    temp2[4][0] = cube[2][3]
    temp2[4][2] = cube[2][1]
    temp2[2][3] = cube[5][0]
    temp2[2][1] = cube[5][2]
    temp2[5][0] = cube[0][0]
    temp2[5][2] = cube[0][2]
        
    temp2[1][0] = cube[1][2]
    temp2[1][1] = cube[1][0]
    temp2[1][2] = cube[1][3]
    temp2[1][3] = cube[1][1]
        
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string
    
def rotateLeft(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
        
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)
        
    temp2[1][3] = cube[4][2]
    temp2[1][1] = cube[4][3]
    temp2[5][0] = cube[1][1]
    temp2[5][1] = cube[1][3]
    temp2[3][2] = cube[5][0]
    temp2[3][0] = cube[5][1]
    temp2[4][2] = cube[3][0]
    temp2[4][3] = cube[3][2]
        
    temp2[0][0] = cube[0][1]
    temp2[0][1] = cube[0][3]
    temp2[0][2] = cube[0][0]
    temp2[0][3] = cube[0][2]
        
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string
    
def rotateRight(id):
    count = 0
    temp = []
    cube = []
    for i in id:
        if count == 4:
            cube.append(temp)
            temp = []
            count = 0
        temp.append(i)
        count += 1
    cube.append(temp)
        
    temp2 = list(cube)
    for i in range(len(cube)):
        cube[i] = tuple(cube[i])
    cube = tuple(cube)
        
    temp2[4][2] = cube[1][3]
    temp2[4][3] = cube[1][1]
    temp2[3][0] = cube[4][2]
    temp2[3][2] = cube[4][3]
    temp2[5][1] = cube[3][0]
    temp2[5][0] = cube[3][2]
    temp2[1][1] = cube[5][0]
    temp2[1][3] = cube[5][1]
        
    temp2[0][0] = cube[0][2]
    temp2[0][1] = cube[0][0]
    temp2[0][2] = cube[0][3]
    temp2[0][3] = cube[0][1]
        
        
    string = ""
    for i in temp2:
        for x in i:
            string += str(x)
    return string

def leftLeft(id):
    return left(left(id))

def upUp(id):
    return up(up(id))

def rotateRotate(id):
    return rotateRight(rotateRight(id))


def randomizeStartCube():
    opposites = {"y": "w", "w": "y", "b": "g", "g": "b", "r": "o", "o": "r"}
    threes = ["ogy", "wgo", "rgw", "ygr", "yog", "boy", "wob", "gow", "ryg", "byr", "oyb", "gyo", "obw", "ybo", "rby", "wbr", "bwo", "rwb", "gwr", "owg", "yrb", "gry", "wrg", "brw"]
    string = ""
    corner = threes[random.randrange(len(threes))]
    corner = threes[0]
    side1, side2, side3 = corner

    for i in range(4):
        string += opposites[side2]

    for i in range(4):
        string += opposites[side1]

    for i in range(4):
        string += side2

    for i in range(4):
        string += side1

    for i in range(4):
        string += opposites[side3]

    for i in range(4):
        string += side3

    return string

def randomizeRotations(cube):
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up", "rotate left": "rotate right", "rotate right": "rotate left", "left left": "left left", "up up": "up up", "rotate rotate": "rotate rotate"}
    moves = {0: "right", 1: "left", 2: "down", 3: "up", 4: "rotate right", 5: "rotate left", 6: "left left", 7: "up up", 8: "rotate rotate", 9: "none"}
    doNot = {"left": ["right", "left", "left left"], "right": ["left", "right", "left left"], "up": ["down", "up", "up up"], "down": ["up", "down", "up up"], "rotate left": ["rotate right", "rotate left", "rotate rotate"], "rotate right": ["rotate left", "rotate right", "rotate rotate"], "left left": ["left",  "right", "left left"], "up up": ["up", "down", "up up"], "rotate rotate": ["rotate right", "rotate left", "rotate rotate"], "none": []}
    rotations = []
    last = None
    for i in range(11):
        rotation = moves[random.randrange(10)]
        if last != None and rotation != "none":
            while rotation in doNot[last]:
                rotation = moves[random.randrange(10)]

        if rotation != "none":
            if rotation == "left left":
                rotations.append("left")
                rotations.append("left")
            elif rotation == "up up":
                rotations.append("up")
                rotations.append("up")
            elif rotation == "rotate rotate":
                rotations.append("rotate left")
                rotations.append("rotate left")
            else:
                rotations.append(rotation)

        if rotation == "up":
            cube = up(cube)
            last = "up"

        if rotation == "down":
            cube = down(cube)
            last = "down"

        if rotation == "left":
            cube = left(cube)
            last = "left"

        if rotation == "right":
            cube = right(cube)
            last = "right"

        if rotation == "rotate left":
            cube = rotateLeft(cube)
            last = "rotate left"

        if rotation == "rotate right":
            cube = rotateRight(cube)
            last = "rotate right"

        if rotation == "left left":
            cube = leftLeft(cube)
            last = "left left"

        if rotation == "up up":
            cube = upUp(cube)
            last = "up up"

        if rotation == "rotate rotate":
            cube = rotateRotate(cube)
            last = "rotate rotate"
    return cube, rotations

def generateList():
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up", "rotate left": "rotate right", "rotate right": "rotate left", "left left": "left left", "up up": "up up", "rotate rotate": "rotate rotate"}

    init = randomizeStartCube()
    a = randomizeRotations(init)
    newList = []
    cube = a[0]
    for i in range(len(a[1]) - 1, -1, -1):
        new = opposites[a[1][i]]
        newList.append([cube, new])
        if new == "up":
            cube = up(cube)

        if new == "down":
            cube = down(cube)

        if new == "left":
            cube = left(cube)

        if new == "right":
            cube = right(cube)

        if new == "rotate left":
            cube = rotateLeft(cube)

        if new == "rotate right":
            cube = rotateRight(cube)

        if new == "left left":
            cube = leftLeft(cube)

        if new == "up up":
            cube = upUp(cube)

        if new == "rotate rotate":
            cube = rotateRotate(cube)
    newList.append([cube, "none"])
    return newList

def parseList():
    toParse = generateList()
    moves = {"right": 7, "left": 1, "down": 2, "up": 3, "rotate right": 4, "rotate left": 5, "none": 6}
    newList = []

    for i in range(len(toParse)):
        newList.append([parse(toParse[i][0]), moves[toParse[i][1]]])

    return newList

def parse(id):
    new = []
    pieces = {"y": [-1, -1, -1], "w": [-1, -1, 1], "b": [-1, 1, -1], "g": [-1, 1, 1], "r": [1, -1, -1], "o": [1, -1, 1]}
    for i in id:
        new += pieces[i]
    return new

class FileManager:
    def __init__(self, name, numberCubes):
        self.name = name
        self.numberCubes = numberCubes
        self.inputFile = open(self.name, "w+")
        self.inputFile.truncate()

    def addToFile(self):
        for i in range(self.numberCubes):
            newList = parseList()
            for i in range(len(newList)):
                new = ""
                new += " ".join(map(str, newList[i][0]))
                new += " " + str(newList[i][1])
                self.inputFile.write(new)
                self.inputFile.write("\n")


test = FileManager("trainData.txt", 10000)
test.addToFile()
