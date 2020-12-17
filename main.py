import pygame
import random
from world import *

#map
cells = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellX = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
cellY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450]

#pygame stuff
pygame.init()
mainScreen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pythonMC")

#set the current map to world.py
for i in range(1, 11):
    cells[i] = blockA[i]
for i in range(1, 11):
    cells[i+10] = blockB[i]
for i in range(1, 11):
    cells[i+20] = blockC[i]
for i in range(1, 11):
    cells[i+30] = blockD[i]
for i in range(1, 11):
    cells[i+40] = blockE[i]
for i in range(1, 11):
    cells[i+50] = blockF[i]
for i in range(1, 11):
    cells[i+60] = blockG[i]
for i in range(1, 11):
    cells[i+70] = blockH[i]
for i in range(1, 11):
    cells[i+80] = blockI[i]
for i in range(1, 11):
    cells[i+90] = blockJ[i]

#var
currentCell = 1
prevCell = 0
noGravity = 0
isJump = False

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
        if cells[currentCell - 1] == 0:
            currentCell -= 1
    if keys[pygame.K_RIGHT]:
        if cells[currentCell + 1] == 0:
            currentCell += 1

    #i have no clue
    if prevCell != currentCell:
        cells[prevCell] = 0
    prevCell = currentCell

    #tile to tile interaction support (TTTIS)
    for i in range(1,101):
        if cells[i] == 2:
            if cells[i - 10] == 0:
                grassChance = random.randint(1, 10)
                if grassChance == 3:
                    cells[i] = 3
            if i < 91:
                if cells[i + 10] != 0:
                    dirtChance = random.randint(1, 10)
                    if dirtChance == 3:
                        cells[i] = 2

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
