import pygame
import random
import math
import sys
import getopt

#map
cells = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellX = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
cellY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450]

#pygame stuff
pygame.init()
mainScreen = pygame.display.set_mode((500, 550))
pygame.display.set_caption("pythonMC")


#args
pack = "default"
generateWorld = 0
seed = random.randint(1000, 999999)
worldNumber = 1

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:gs:w:", ["pack=", "generate", "seed=", "world="])
except getopt.GetoptError:
    print("main.py -p [texture pack] -g -s [seed] -w [world]")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("main.py -p [texture pack] -g -s [seed] -w [world]")
        sys.exit()
    elif opt in ("-p", "--pack"):
        pack = arg
        print(arg)
    elif opt in ("-g", "--generate"):
        generateWorld = 1
    elif opt in ("-s", "--seed"):
        seed = int(arg)
    elif opt in ("-w", "--world"):
        worldNumber = int(arg)

random.seed(seed)

#texture pack load
class textures:
    print("loading textures")
    grass = pygame.image.load("textures/" + pack + "/blocks/grass.png")
    dirt = pygame.image.load("textures/" + pack + "/blocks/dirt.png")
    stone = pygame.image.load("textures/" + pack + "/blocks/stone.png")
    wood = pygame.image.load("textures/" + pack + "/blocks/wood.png")
    leaves = pygame.image.load("textures/" + pack + "/blocks/leaves.png")
    slot = pygame.image.load("textures/" + pack + "/inventory/background/slot.png")
    number1 = pygame.image.load("textures/" + pack + "/inventory/background/1.png")
    number2 = pygame.image.load("textures/" + pack + "/inventory/background/2.png")
    number3 = pygame.image.load("textures/" + pack + "/inventory/background/3.png")
    number4 = pygame.image.load("textures/" + pack + "/inventory/background/4.png")
    number5 = pygame.image.load("textures/" + pack + "/inventory/background/5.png")
    number6 = pygame.image.load("textures/" + pack + "/inventory/background/6.png")
    number7 = pygame.image.load("textures/" + pack + "/inventory/background/7.png")
    number8 = pygame.image.load("textures/" + pack + "/inventory/background/8.png")
    number9 = pygame.image.load("textures/" + pack + "/inventory/background/9.png")
    number0 = pygame.image.load("textures/" + pack + "/inventory/background/0.png")
    inventoryGrass = pygame.image.load("textures/" + pack + "/inventory/blocks/grass.png")
    inventoryDirt = pygame.image.load("textures/" + pack + "/inventory/blocks/dirt.png")
    inventoryStone = pygame.image.load("textures/" + pack + "/inventory/blocks/stone.png")
    inventoryWood = pygame.image.load("textures/" + pack + "/inventory/blocks/wood.png")
    inventoryLeaves = pygame.image.load("textures/" + pack + "/inventory/blocks/leaves.png")
    select = pygame.image.load("textures/" + pack + "/select.png")
    print("done")

if worldNumber == 1:
    from world import *
elif worldNumber == 2:
    from world2 import *
elif worldNumber == 3:
    from world3 import *
elif worldNumber == 4:
    from world4 import *
elif worldNumber == 5:
    from world5 import *
else:
    print("-w must be a number between 1 and 5")
    
#convert cells into map
def loadMap(locX, locY):
    for i in range(1, 11):
        cells[i + 0] =  map[locY + 0][locX + i]
        cells[i + 10] = map[locY + 1][locX + i]
        cells[i + 20] = map[locY + 2][locX + i]
        cells[i + 30] = map[locY + 3][locX + i]
        cells[i + 40] = map[locY + 4][locX + i]
        cells[i + 50] = map[locY + 5][locX + i]
        cells[i + 60] = map[locY + 6][locX + i]
        cells[i + 70] = map[locY + 7][locX + i]
        cells[i + 80] = map[locY + 8][locX + i]
        cells[i + 90] = map[locY + 9][locX + i]

def saveMap(locX, locY):
    for i in range(1, 11):
        map[locY + 0][locX + i] = cells[i + 0]
        map[locY + 1][locX + i] = cells[i + 10]
        map[locY + 2][locX + i] = cells[i + 20]
        map[locY + 3][locX + i] = cells[i + 30]
        map[locY + 4][locX + i] = cells[i + 40]
        map[locY + 5][locX + i] = cells[i + 50]
        map[locY + 6][locX + i] = cells[i + 60]
        map[locY + 7][locX + i] = cells[i + 70]
        map[locY + 8][locX + i] = cells[i + 80]
        map[locY + 9][locX + i] = cells[i + 90]


def save():
    f = open("world.py", "w")
    f.write("\nmap = " + str(map) + "\nhotbar = " + str(hotbar) + "\namountHotbar = " + str(amountHotbar))
    f.close()

def addHotbar():
    done = 0
    for i in range(0, 10):
        if cells[selectCell] == hotbar[i]:
            if amountHotbar[i] == 64:
                continue
            else:
                amountHotbar[i] += 1
                return
    for i in range(0, 10):
        if hotbar[i] == 0:
            amountHotbar[i] += 1
            hotbar[i] = cells[selectCell]
            done = 1
        if done == 1:
            done = 0
            return
def removeHotbar():
    amountHotbar[currentHotbarCell] -= 1
    if amountHotbar[currentHotbarCell] == 0:
        hotbar[currentHotbarCell] = 0

locX = 0
locY = 0
#set the current map to world.py
loadMap(locX, locY)

#generate a world
if generateWorld == 1:
    print("Generating World")
    for i in range(1, len(map[0])):
        loadMap(locX, locY)
        map[0][i] = 0
        map[1][i] = 0
        map[2][i] = 0
        map[3][i] = 0
        map[4][i] = 0
        map[5][i] = 0
        map[6][i] = 0
        map[7][i] = 0
        map[8][i] = 0
        map[9][i] = 0
        map[10][i] = 0
        map[11][i] = 4
        map[12][i] = 4
        map[13][i] = 4
        map[14][i] = 4
        map[15][i] = 4
        map[16][i] = 4
        map[17][i] = 4
        map[18][i] = 4
        map[19][i] = 4
        map[20][i] = 4
        map[21][i] = 4
        map[22][i] = 4
        map[23][i] = 4
        map[24][i] = 4
        map[25][i] = 5
        saveMap(locX, locY)
    save()
    locY = 1
    loadMap(locX, locY)
    for i in range(1, len(map[0]) - 11):
        grassHeight = random.randint(2,8)
        if math.floor(grassHeight) in (0, 1, 2):
            grassHeight = 3
        if math.floor(grassHeight / 3) == 1:
            cells[81] = 3
            cells[91] = 2
        if math.floor(grassHeight / 3) == 2:
            cells[71] = 3
            cells[81] = 2
            cells[91] = 4
        if math.floor(grassHeight / 3) == 3:
            cells[61] = 3
            cells[71] = 2
            cells[81] = 4
            cells[91] = 4
        saveMap(locX, locY)
        locX += 1
        loadMap(locX, locY)
        print(str(int(i / 2.5)) + "% done")
    locX = 0
    locY = 0
    loadMap(locX, locY)
    print("100% done")

#var
currentCell = 1
selectCell = 1
prevCell = 0
noGravity = 0
isJump = False
currentHotbarCell = 0
hotel = "trivago"

#loop
run = True
while run:
    #more pygame stuff
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    #fill the screen
    mainScreen.fill((0, 0, 0))

    #gravity / down
    if noGravity == 0:
        if currentCell > 80 and locY != 16:
            locY += 1
            loadMap(locX, locY)
            if cells[currentCell] == 0:
                locY += 1
                loadMap(locX, locY)
                if cells[currentCell] != 0:
                    currentCell -= 10
                    selectCell -= 10
            if cells[currentCell] != 0:
                currentCell -= 10
                selectCell -= 10
        else:
            if cells[currentCell + 10] == 0:
                currentCell += 10
                if selectCell < 91:
                    selectCell += 10
            isJump = False
    else:
        noGravity -= 1

    #keyboard input
    if keys[pygame.K_UP]:
        if currentCell < 91:
            if cells[currentCell + 10] != 0:
                if currentCell < 50:
                    if locY != 0:
                        locY -= 1
                        loadMap(locX, locY)
                        if cells[currentCell] != 0:
                            currentCell += 10
                            selectCell += 10
                    else:
                        if cells[currentCell - 10] == 0:
                            currentCell -= 10
                            selectCell -= 10
                elif cells[currentCell - 10] == 0:
                    currentCell -= 10
                    if selectCell > 11:
                        selectCell -= 10
                if noGravity == 0 and not isJump:
                    noGravity = 2
                    isJump = True
    if keys[pygame.K_LEFT]:
        if True:
            if (currentCell - 1) / 10 == int((currentCell - 1) / 10) or (currentCell - 2) / 10 == int((currentCell - 2) / 10) or (currentCell - 3) / 10 == int((currentCell - 3) / 10) or (currentCell - 4) / 10 == int((currentCell - 4) / 10) or (currentCell - 5) / 10 == int((currentCell - 5) / 10):
                if locX != 0:
                    locX -= 1
                    loadMap(locX, locY)
                    if cells[currentCell] != 0:
                        currentCell += 1
                        selectCell += 1
                else:
                    if cells[currentCell - 1] == 0:
                        if (currentCell - 1) / 10 != int((currentCell - 1) / 10):
                            currentCell -= 1
                            selectCell -= 1
            else:
                if cells[currentCell - 1] == 0:
                    currentCell -= 1
                    if (selectCell - 1) / 10 != int((selectCell - 1) / 10):
                        selectCell -= 1
    if keys[pygame.K_RIGHT]:
            if currentCell / 10 == int(currentCell / 10) or (currentCell + 1) / 10 == int((currentCell + 1) / 10) or (currentCell + 2) / 10 == int((currentCell + 2) / 10) or (currentCell + 3) / 10 == int((currentCell + 3) / 10) or (currentCell + 4) / 10 == int((currentCell + 4) / 10):
                locX= locX+ 1
                loadMap(locX, locY)
                if cells[currentCell] != 0:
                    currentCell -= 1
                    selectCell -= 1
            else:
                if cells[currentCell + 1] == 0:
                    currentCell += 1
                    if selectCell / 10 != int(selectCell / 10):
                        selectCell += 1
    if keys[pygame.K_w]:
        if selectCell > 10:
            if selectCell != currentCell - 10 and selectCell != currentCell - 11 and selectCell != currentCell - 9:
                selectCell -= 10
    if keys[pygame.K_a]:
        if (selectCell - 1) / 10 != int((selectCell - 1) / 10):
            if selectCell != currentCell - 1 and selectCell != currentCell - 11 and selectCell != currentCell + 9:
                selectCell -= 1
    if keys[pygame.K_s]:
        if selectCell < 91:
            if selectCell != currentCell + 10 and selectCell != currentCell + 11 and selectCell != currentCell + 9:
                selectCell += 10
    if keys[pygame.K_d]:
        if selectCell / 10 != int(selectCell / 10):
            if selectCell != currentCell + 1 and selectCell != currentCell + 11 and selectCell != currentCell - 9:
                selectCell += 1
    if keys[pygame.K_e] and cells[selectCell] > 1:
        addHotbar()
        cells[selectCell] = 0
        saveMap(locX, locY)
    if keys[pygame.K_MINUS]:
        if currentHotbarCell != 0:
            currentHotbarCell -= 1
    if keys[pygame.K_EQUALS]:
        if currentHotbarCell != 9:
            currentHotbarCell += 1
    if keys[pygame.K_q]:
        if amountHotbar[currentHotbarCell] != 0 and cells[selectCell] == 0:
            cells[selectCell] = hotbar[currentHotbarCell]
            removeHotbar()
            saveMap(locX, locY)

    #i have no clue
    if prevCell != currentCell:
        cells[prevCell] = 0
    prevCell = currentCell

    #map movement
    loadMap(locX, locY)

    #tile to tile interaction support (TTTIS)
    for i in range(1, 101):
        if cells[i] == 2:
            if cells[i - 10] == 0:
                grassChance = random.randint(1, 10)
                if grassChance == 3:
                    cells[i] = 3
        elif cells[i] == 3:
            if True:
                if cells[i - 10] != 0 and cells[i - 10] != 1:
                    dirtChance = random.randint(1, 10)
                    if dirtChance == 3:
                        cells[i] = 2

    #gets rid of player for save
    for i in range (1, 101):
        if cells[i] == 1:
            cells[i] = 0

    #saves the world
    saveMap(locX, locY)
    save()

    #set the player
    cells[currentCell] = 1

    for i in range(0, 10):
        mainScreen.blit(textures.slot, (i * 50, 500))
        if hotbar[i] == 2:
            mainScreen.blit(textures.inventoryDirt, (i * 50, 500))
        elif hotbar[i] == 3:
            mainScreen.blit(textures.inventoryGrass, (i * 50, 500))
        elif hotbar[i] == 4:
            mainScreen.blit(textures.inventoryStone, (i * 50, 500))
        elif hotbar[i] == 6:
            mainScreen.blit(textures.inventoryWood, (i * 50, 500))
        elif hotbar[i] == 7:
            mainScreen.blit(textures.inventoryLeaves, (i * 50, 500))
    mainScreen.blit(textures.select, (currentHotbarCell * 50, 500))
    for i in range(0, 10):
        if amountHotbar[i] != 0:
            mainScreen.blit(pygame.image.load("textures/" + pack + "/inventory/background/" + str(math.floor(amountHotbar[i] / 10)) + ".png"), (i * 50 + 30, 540))
            mainScreen.blit(pygame.image.load("textures/" + pack + "/inventory/background/" + str(amountHotbar[i] - math.floor(amountHotbar[i] / 10) * 10) + ".png"), (i * 50 + 40, 540))

    #draw to the screen
    for i in range(1,101):
        if cells[i] == 1:
            pygame.draw.rect(mainScreen, (255, 255, 255), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 0:
            pygame.draw.rect(mainScreen, (3, 215, 252), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 2:
            mainScreen.blit(textures.dirt, (cellX[i], cellY[i]))
        elif cells[i] == 3:
            mainScreen.blit(textures.grass, (cellX[i], cellY[i]))
        elif cells[i] == 4:
            mainScreen.blit(textures.stone, (cellX[i], cellY[i]))
        elif cells[i] == 5:
            pygame.draw.rect(mainScreen, (69, 69, 69), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 6:
            mainScreen.blit(textures.wood, (cellX[i], cellY[i]))
        elif cells[i] == 7:
            pygame.draw.rect(mainScreen, (3, 215, 252), (cellX[i], cellY[i], 50, 50))
            mainScreen.blit(textures.leaves, (cellX[i], cellY[i]))
        if selectCell == i:
            mainScreen.blit(pygame.image.load("textures/" + pack + "/select.png"), (cellX[i], cellY[i]))

    pygame.display.update()

pygame.quit()
