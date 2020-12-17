import pygame
from world import *

cells = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellX = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
cellY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450]

pygame.init()
mainScreen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pythonMC")

currentCell = 1
prevCell = 0

run = True
while run:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    mainScreen.fill((0, 0, 0))

    if keys[pygame.K_UP]:
        currentCell -= 10
    if keys[pygame.K_DOWN]:
        currentCell += 10
    if keys[pygame.K_LEFT]:
        currentCell -= 1
    if keys[pygame.K_RIGHT]:
        currentCell += 1

    if prevCell != currentCell:
        cells[prevCell] = 0
    prevCell = currentCell

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

    cells[currentCell] = 1

    for i in range(1,101):
        if cells[i] == 1:
            pygame.draw.rect(mainScreen, (255, 255, 255), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 0:
            pygame.draw.rect(mainScreen, (3, 215, 252), (cellX[i], cellY[i], 50, 50))
        elif cells[i] == 2:
            pygame.draw.rect(mainScreen, (173, 58, 0), (cellX[i], cellY[i], 50, 50))

    pygame.display.update()

pygame.quit()
