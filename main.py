import pygame
import random
from world import *
import math

#map
cells = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellX = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
cellY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450]

#pygame stuff
pygame.init()
mainScreen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pythonMC")

def save():
    f = open("world.py", "w")
    f.write("\nblockA = " + str(blockA) + "\nblockB = " + str(blockB) + "\nblockC = " + str(blockC) + "\nblockD = " + str(blockD) + "\nblockE = " + str(blockE) + "\nblockF = " + str(blockF) + "\nblockG = " + str(blockG) + "\nblockH = " + str(blockH) + "\nblockI = " + str(blockI) + "\nblockJ = " + str(blockJ))
    f.close()

loc = 0
#set the current map to world.py
for i in range(1, 11):
    cells[i] = blockA[i + loc]
for i in range(1, 11):
    cells[i+10] = blockB[i + loc]
for i in range(1, 11):
    cells[i+20] = blockC[i + loc]
for i in range(1, 11):
    cells[i+30] = blockD[i + loc]
for i in range(1, 11):
    cells[i+40] = blockE[i + loc]
for i in range(1, 11):
    cells[i+50] = blockF[i + loc]
for i in range(1, 11):
    cells[i+60] = blockG[i + loc]
for i in range(1, 11):
    cells[i+70] = blockH[i + loc]
for i in range(1, 11):
    cells[i+80] = blockI[i + loc]
for i in range(1, 11):
    cells[i+90] = blockJ[i + loc]

#var
currentCell = 1
prevCell = 0
noGravity = 0
isJump = False
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

    #jumping
    if noGravity == 0:
        if cells[currentCell + 10] == 0:
            currentCell += 10
        isJump = False
    else:
        noGravity -= 1

    #keyboard input
    if keys[pygame.K_UP]:
        if cells[currentCell + 10] != 0:
            if cells[currentCell - 10] == 0:
                currentCell -= 10
            if noGravity == 0 and not isJump:
                noGravity = 2
                isJump = True
    if keys[pygame.K_LEFT]:
        if True:
            if (currentCell - 1) / 10 == int((currentCell - 1) / 10):
                if loc != 0:
                    loc -= 1
                    for i in range(1, 11):
                        cells[i] = blockA[i + loc]
                    for i in range(1, 11):
                        cells[i+10] = blockB[i + loc]
                    for i in range(1, 11):
                        cells[i+20] = blockC[i + loc]
                    for i in range(1, 11):
                        cells[i+30] = blockD[i + loc]
                    for i in range(1, 11):
                        cells[i+40] = blockE[i + loc]
                    for i in range(1, 11):
                        cells[i+50] = blockF[i + loc]
                    for i in range(1, 11):
                        cells[i+60] = blockG[i + loc]
                    for i in range(1, 11):
                        cells[i+70] = blockH[i + loc]
                    for i in range(1, 11):
                        cells[i+80] = blockI[i + loc]
                    for i in range(1, 11):
                        cells[i+90] = blockJ[i + loc]
                    if cells[currentCell] != 0:
                        currentCell += 1
            else:
                if cells[currentCell - 1] == 0:
                    currentCell -= 1
    if keys[pygame.K_RIGHT]:
            if currentCell / 10 == int(currentCell / 10):
                loc = loc + 1

                for i in range(1, 11):
                    cells[i] = blockA[i + loc]
                for i in range(1, 11):
                    cells[i+10] = blockB[i + loc]
                for i in range(1, 11):
                    cells[i+20] = blockC[i + loc]
                for i in range(1, 11):
                    cells[i+30] = blockD[i + loc]
                for i in range(1, 11):
                    cells[i+40] = blockE[i + loc]
                for i in range(1, 11):
                    cells[i+50] = blockF[i + loc]
                for i in range(1, 11):
                    cells[i+60] = blockG[i + loc]
                for i in range(1, 11):
                    cells[i+70] = blockH[i + loc]
                for i in range(1, 11):
                    cells[i+80] = blockI[i + loc]
                for i in range(1, 11):
                    cells[i+90] = blockJ[i + loc]
                if cells[currentCell] != 0:
                    currentCell -= 1
            else:
                if cells[currentCell + 1] == 0:
                    currentCell += 1

    #i have no clue
    if prevCell != currentCell:
        cells[prevCell] = 0
    prevCell = currentCell

    #map movement
    for i in range(1, 11):
        cells[i] = blockA[i + loc]
    for i in range(1, 11):
        cells[i+10] = blockB[i + loc]
    for i in range(1, 11):
        cells[i+20] = blockC[i + loc]
    for i in range(1, 11):
        cells[i+30] = blockD[i + loc]
    for i in range(1, 11):
        cells[i+40] = blockE[i + loc]
    for i in range(1, 11):
        cells[i+50] = blockF[i + loc]
    for i in range(1, 11):
        cells[i+60] = blockG[i + loc]
    for i in range(1, 11):
        cells[i+70] = blockH[i + loc]
    for i in range(1, 11):
        cells[i+80] = blockI[i + loc]
    for i in range(1, 11):
        cells[i+90] = blockJ[i + loc]

    #tile to tile interaction support (TTTIS)
    for i in range(1,101):
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
    for i in range(1, 11):
        blockA[i + loc] = cells[i]
    for i in range(1, 11):
        blockB[i + loc] = cells[i+10]
    for i in range(1, 11):
        blockC[i + loc] = cells[i+20]
    for i in range(1, 11):
        blockD[i + loc] = cells[i+30]
    for i in range(1, 11):
        blockE[i + loc] = cells[i+40]
    for i in range(1, 11):
        blockF[i + loc] = cells[i+50]
    for i in range(1, 11):
        blockG[i + loc] = cells[i+60]
    for i in range(1, 11):
        blockH[i + loc] = cells[i+70]
    for i in range(1, 11):
        blockI[i + loc] = cells[i+80]
    for i in range(1, 11):
        blockJ[i + loc] = cells[i+90]
    save()

    #moves player when map moves

    #set the player
    cells[currentCell] = 1

    #draw to the screen
    for i in range(1,101):
        if cells[i] == 1:
            pygame.draw.rect(mainScreen, (255, 255, 255), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 0:
            pygame.draw.rect(mainScreen, (3, 215, 252), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 2:
            pygame.draw.rect(mainScreen, (173, 58, 0), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 3:
            pygame.draw.rect(mainScreen, (2, 179, 14), (cellX[i], cellY[i], 50, 50))

    pygame.display.update()

pygame.quit()
