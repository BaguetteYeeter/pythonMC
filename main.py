import pygame
import random
from world import *
import math
import sys
import getopt

#map
cells = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellX = [0, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
cellY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450]

#pygame stuff
pygame.init()
mainScreen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pythonMC")


#args
pack = "default"
try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:", ["pack="])
except getopt.GetoptError:
    print("main.py -p [texture pack]")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("main.py -p [texture pack]")
        sys.exit()
    elif opt in ("-p", "--pack"):
        pack = arg
        print(arg)

#texture pack load
class textures:
    print("loading textures")
    grass = pygame.image.load("textures/" + pack + "/blocks/grass.png")
    dirt = pygame.image.load("textures/" + pack + "/blocks/dirt.png")
    stone = pygame.image.load("textures/" + pack + "/blocks/stone.png")
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
    print("done")

#lag
def loadMap(locY):
    for i in range(1, 11):
        if locY == 0:
            cells[i] = blockA[i + locX]
            cells[i+10] = blockB[i + locX]
            cells[i+20] = blockC[i + locX]
            cells[i+30] = blockD[i + locX]
            cells[i+40] = blockE[i + locX]
            cells[i+50] = blockF[i + locX]
            cells[i+60] = blockG[i + locX]
            cells[i+70] = blockH[i + locX]
            cells[i+80] = blockI[i + locX]
            cells[i+90] = blockJ[i + locX]
        if locY == 1:
            cells[i] = blockB[i + locX]
            cells[i+10] = blockC[i + locX]
            cells[i+20] = blockD[i + locX]
            cells[i+30] = blockE[i + locX]
            cells[i+40] = blockF[i + locX]
            cells[i+50] = blockG[i + locX]
            cells[i+60] = blockH[i + locX]
            cells[i+70] = blockI[i + locX]
            cells[i+80] = blockJ[i + locX]
            cells[i+90] = blockK[i + locX]
        if locY == 2:
            cells[i] = blockC[i + locX]
            cells[i+10] = blockD[i + locX]
            cells[i+20] = blockE[i + locX]
            cells[i+30] = blockF[i + locX]
            cells[i+40] = blockG[i + locX]
            cells[i+50] = blockH[i + locX]
            cells[i+60] = blockI[i + locX]
            cells[i+70] = blockJ[i + locX]
            cells[i+80] = blockK[i + locX]
            cells[i+90] = blockL[i + locX]
        if locY == 3:
            cells[i] = blockD[i + locX]
            cells[i+10] = blockE[i + locX]
            cells[i+20] = blockF[i + locX]
            cells[i+30] = blockG[i + locX]
            cells[i+40] = blockH[i + locX]
            cells[i+50] = blockI[i + locX]
            cells[i+60] = blockJ[i + locX]
            cells[i+70] = blockK[i + locX]
            cells[i+80] = blockL[i + locX]
            cells[i+90] = blockM[i + locX]
        if locY == 4:
            cells[i] = blockE[i + locX]
            cells[i+10] = blockF[i + locX]
            cells[i+20] = blockG[i + locX]
            cells[i+30] = blockH[i + locX]
            cells[i+40] = blockI[i + locX]
            cells[i+50] = blockJ[i + locX]
            cells[i+60] = blockK[i + locX]
            cells[i+70] = blockL[i + locX]
            cells[i+80] = blockM[i + locX]
            cells[i+90] = blockN[i + locX]
        if locY == 5:
            cells[i] = blockF[i + locX]
            cells[i+10] = blockG[i + locX]
            cells[i+20] = blockH[i + locX]
            cells[i+30] = blockI[i + locX]
            cells[i+40] = blockJ[i + locX]
            cells[i+50] = blockK[i + locX]
            cells[i+60] = blockL[i + locX]
            cells[i+70] = blockM[i + locX]
            cells[i+80] = blockN[i + locX]
            cells[i+90] = blockO[i + locX]
        if locY == 6:
            cells[i] = blockG[i + locX]
            cells[i+10] = blockH[i + locX]
            cells[i+20] = blockI[i + locX]
            cells[i+30] = blockJ[i + locX]
            cells[i+40] = blockK[i + locX]
            cells[i+50] = blockL[i + locX]
            cells[i+60] = blockM[i + locX]
            cells[i+70] = blockN[i + locX]
            cells[i+80] = blockO[i + locX]
            cells[i+90] = blockP[i + locX]
        if locY == 7:
            cells[i] = blockH[i + locX]
            cells[i+10] = blockI[i + locX]
            cells[i+20] = blockJ[i + locX]
            cells[i+30] = blockK[i + locX]
            cells[i+40] = blockL[i + locX]
            cells[i+50] = blockM[i + locX]
            cells[i+60] = blockN[i + locX]
            cells[i+70] = blockO[i + locX]
            cells[i+80] = blockP[i + locX]
            cells[i+90] = blockQ[i + locX]
        if locY == 8:
            cells[i] = blockI[i + locX]
            cells[i+10] = blockJ[i + locX]
            cells[i+20] = blockK[i + locX]
            cells[i+30] = blockL[i + locX]
            cells[i+40] = blockM[i + locX]
            cells[i+50] = blockN[i + locX]
            cells[i+60] = blockO[i + locX]
            cells[i+70] = blockP[i + locX]
            cells[i+80] = blockQ[i + locX]
            cells[i+90] = blockR[i + locX]
        if locY == 9:
            cells[i] = blockJ[i + locX]
            cells[i+10] = blockK[i + locX]
            cells[i+20] = blockL[i + locX]
            cells[i+30] = blockM[i + locX]
            cells[i+40] = blockN[i + locX]
            cells[i+50] = blockO[i + locX]
            cells[i+60] = blockP[i + locX]
            cells[i+70] = blockQ[i + locX]
            cells[i+80] = blockR[i + locX]
            cells[i+90] = blockS[i + locX]
        if locY == 10:
            cells[i] = blockK[i + locX]
            cells[i+10] = blockL[i + locX]
            cells[i+20] = blockM[i + locX]
            cells[i+30] = blockN[i + locX]
            cells[i+40] = blockO[i + locX]
            cells[i+50] = blockP[i + locX]
            cells[i+60] = blockQ[i + locX]
            cells[i+70] = blockR[i + locX]
            cells[i+80] = blockS[i + locX]
            cells[i+90] = blockT[i + locX]
        if locY == 11:
            cells[i] = blockL[i + locX]
            cells[i+10] = blockM[i + locX]
            cells[i+20] = blockN[i + locX]
            cells[i+30] = blockO[i + locX]
            cells[i+40] = blockP[i + locX]
            cells[i+50] = blockQ[i + locX]
            cells[i+60] = blockR[i + locX]
            cells[i+70] = blockS[i + locX]
            cells[i+80] = blockT[i + locX]
            cells[i+90] = blockU[i + locX]
        if locY == 12:
            cells[i] = blockM[i + locX]
            cells[i+10] = blockN[i + locX]
            cells[i+20] = blockO[i + locX]
            cells[i+30] = blockP[i + locX]
            cells[i+40] = blockQ[i + locX]
            cells[i+50] = blockR[i + locX]
            cells[i+60] = blockS[i + locX]
            cells[i+70] = blockT[i + locX]
            cells[i+80] = blockU[i + locX]
            cells[i+90] = blockV[i + locX]
        if locY == 13:
            cells[i] = blockN[i + locX]
            cells[i+10] = blockO[i + locX]
            cells[i+20] = blockP[i + locX]
            cells[i+30] = blockQ[i + locX]
            cells[i+40] = blockR[i + locX]
            cells[i+50] = blockS[i + locX]
            cells[i+60] = blockT[i + locX]
            cells[i+70] = blockU[i + locX]
            cells[i+80] = blockV[i + locX]
            cells[i+90] = blockW[i + locX]
        if locY == 14:
            cells[i] = blockO[i + locX]
            cells[i+10] = blockP[i + locX]
            cells[i+20] = blockQ[i + locX]
            cells[i+30] = blockR[i + locX]
            cells[i+40] = blockS[i + locX]
            cells[i+50] = blockT[i + locX]
            cells[i+60] = blockU[i + locX]
            cells[i+70] = blockV[i + locX]
            cells[i+80] = blockW[i + locX]
            cells[i+90] = blockX[i + locX]
        if locY == 15:
            cells[i] = blockP[i + locX]
            cells[i+10] = blockQ[i + locX]
            cells[i+20] = blockR[i + locX]
            cells[i+30] = blockS[i + locX]
            cells[i+40] = blockT[i + locX]
            cells[i+50] = blockU[i + locX]
            cells[i+60] = blockV[i + locX]
            cells[i+70] = blockW[i + locX]
            cells[i+80] = blockX[i + locX]
            cells[i+90] = blockY[i + locX]
        if locY == 16:
            cells[i] = blockQ[i + locX]
            cells[i+10] = blockR[i + locX]
            cells[i+20] = blockS[i + locX]
            cells[i+30] = blockT[i + locX]
            cells[i+40] = blockU[i + locX]
            cells[i+50] = blockV[i + locX]
            cells[i+60] = blockW[i + locX]
            cells[i+70] = blockX[i + locX]
            cells[i+80] = blockY[i + locX]
            cells[i+90] = blockZ[i + locX]

def saveMap(locY):
    for i in range(1, 11):
        if locY == 0:
            blockA[i + locX] = cells[i]
            blockB[i + locX] = cells[i+10]
            blockC[i + locX] = cells[i+20]
            blockD[i + locX] = cells[i+30]
            blockE[i + locX] = cells[i+40]
            blockF[i + locX] = cells[i+50]
            blockG[i + locX] = cells[i+60]
            blockH[i + locX] = cells[i+70]
            blockI[i + locX] = cells[i+80]
            blockJ[i + locX] = cells[i+90]
        if locY == 1:
            blockB[i + locX] = cells[i]
            blockC[i + locX] = cells[i+10]
            blockD[i + locX] = cells[i+20]
            blockE[i + locX] = cells[i+30]
            blockF[i + locX] = cells[i+40]
            blockG[i + locX] = cells[i+50]
            blockH[i + locX] = cells[i+60]
            blockI[i + locX] = cells[i+70]
            blockJ[i + locX] = cells[i+80]
            blockK[i + locX] = cells[i+90]
        if locY == 2:
            blockC[i + locX] = cells[i]
            blockD[i + locX] = cells[i+10]
            blockE[i + locX] = cells[i+20]
            blockF[i + locX] = cells[i+30]
            blockG[i + locX] = cells[i+40]
            blockH[i + locX] = cells[i+50]
            blockI[i + locX] = cells[i+60]
            blockJ[i + locX] = cells[i+70]
            blockK[i + locX] = cells[i+80]
            blockL[i + locX] = cells[i+90]
        if locY == 3:
            blockD[i + locX] = cells[i]
            blockE[i + locX] = cells[i+10]
            blockF[i + locX] = cells[i+20]
            blockG[i + locX] = cells[i+30]
            blockH[i + locX] = cells[i+40]
            blockI[i + locX] = cells[i+50]
            blockJ[i + locX] = cells[i+60]
            blockK[i + locX] = cells[i+70]
            blockL[i + locX] = cells[i+80]
            blockM[i + locX] = cells[i+90]
        if locY == 4:
            blockE[i + locX] = cells[i]
            blockF[i + locX] = cells[i+10]
            blockG[i + locX] = cells[i+20]
            blockH[i + locX] = cells[i+30]
            blockI[i + locX] = cells[i+40]
            blockJ[i + locX] = cells[i+50]
            blockK[i + locX] = cells[i+60]
            blockL[i + locX] = cells[i+70]
            blockM[i + locX] = cells[i+80]
            blockN[i + locX] = cells[i+90]
        if locY == 5:
            blockF[i + locX] = cells[i]
            blockG[i + locX] = cells[i+10]
            blockH[i + locX] = cells[i+20]
            blockI[i + locX] = cells[i+30]
            blockJ[i + locX] = cells[i+40]
            blockK[i + locX] = cells[i+50]
            blockL[i + locX] = cells[i+60]
            blockM[i + locX] = cells[i+70]
            blockN[i + locX] = cells[i+80]
            blockO[i + locX] = cells[i+90]
        if locY == 6:
            blockG[i + locX] = cells[i]
            blockH[i + locX] = cells[i+10]
            blockI[i + locX] = cells[i+20]
            blockJ[i + locX] = cells[i+30]
            blockK[i + locX] = cells[i+40]
            blockL[i + locX] = cells[i+50]
            blockM[i + locX] = cells[i+60]
            blockN[i + locX] = cells[i+70]
            blockO[i + locX] = cells[i+80]
            blockP[i + locX] = cells[i+90]
        if locY == 7:
            blockH[i + locX] = cells[i]
            blockI[i + locX] = cells[i+10]
            blockJ[i + locX] = cells[i+20]
            blockK[i + locX] = cells[i+30]
            blockL[i + locX] = cells[i+40]
            blockM[i + locX] = cells[i+50]
            blockN[i + locX] = cells[i+60]
            blockO[i + locX] = cells[i+70]
            blockP[i + locX] = cells[i+80]
            blockQ[i + locX] = cells[i+90]
        if locY == 8:
            blockI[i + locX] = cells[i]
            blockJ[i + locX] = cells[i+10]
            blockK[i + locX] = cells[i+20]
            blockL[i + locX] = cells[i+30]
            blockM[i + locX] = cells[i+40]
            blockN[i + locX] = cells[i+50]
            blockO[i + locX] = cells[i+60]
            blockP[i + locX] = cells[i+70]
            blockQ[i + locX] = cells[i+80]
            blockR[i + locX] = cells[i+90]
        if locY == 9:
            blockJ[i + locX] = cells[i]
            blockK[i + locX] = cells[i+10]
            blockL[i + locX] = cells[i+20]
            blockM[i + locX] = cells[i+30]
            blockN[i + locX] = cells[i+40]
            blockO[i + locX] = cells[i+50]
            blockP[i + locX] = cells[i+60]
            blockQ[i + locX] = cells[i+70]
            blockR[i + locX] = cells[i+80]
            blockS[i + locX] = cells[i+90]
        if locY == 10:
            blockK[i + locX] = cells[i]
            blockL[i + locX] = cells[i+10]
            blockM[i + locX] = cells[i+20]
            blockN[i + locX] = cells[i+30]
            blockO[i + locX] = cells[i+40]
            blockP[i + locX] = cells[i+50]
            blockQ[i + locX] = cells[i+60]
            blockR[i + locX] = cells[i+70]
            blockS[i + locX] = cells[i+80]
            blockT[i + locX] = cells[i+90]
        if locY == 11:
            blockL[i + locX] = cells[i]
            blockM[i + locX] = cells[i+10]
            blockN[i + locX] = cells[i+20]
            blockO[i + locX] = cells[i+30]
            blockP[i + locX] = cells[i+40]
            blockQ[i + locX] = cells[i+50]
            blockR[i + locX] = cells[i+60]
            blockS[i + locX] = cells[i+70]
            blockT[i + locX] = cells[i+80]
            blockU[i + locX] = cells[i+90]
        if locY == 12:
            blockM[i + locX] = cells[i]
            blockN[i + locX] = cells[i+10]
            blockO[i + locX] = cells[i+20]
            blockP[i + locX] = cells[i+30]
            blockQ[i + locX] = cells[i+40]
            blockR[i + locX] = cells[i+50]
            blockS[i + locX] = cells[i+60]
            blockT[i + locX] = cells[i+70]
            blockU[i + locX] = cells[i+80]
            blockV[i + locX] = cells[i+90]
        if locY == 13:
            blockN[i + locX] = cells[i]
            blockO[i + locX] = cells[i+10]
            blockP[i + locX] = cells[i+20]
            blockQ[i + locX] = cells[i+30]
            blockR[i + locX] = cells[i+40]
            blockS[i + locX] = cells[i+50]
            blockT[i + locX] = cells[i+60]
            blockU[i + locX] = cells[i+70]
            blockV[i + locX] = cells[i+80]
            blockW[i + locX] = cells[i+90]
        if locY == 14:
            blockO[i + locX] = cells[i]
            blockP[i + locX] = cells[i+10]
            blockQ[i + locX] = cells[i+20]
            blockR[i + locX] = cells[i+30]
            blockS[i + locX] = cells[i+40]
            blockT[i + locX] = cells[i+50]
            blockU[i + locX] = cells[i+60]
            blockV[i + locX] = cells[i+70]
            blockW[i + locX] = cells[i+80]
            blockX[i + locX] = cells[i+90]
        if locY == 15:
            blockP[i + locX] = cells[i]
            blockQ[i + locX] = cells[i+10]
            blockR[i + locX] = cells[i+20]
            blockS[i + locX] = cells[i+30]
            blockT[i + locX] = cells[i+40]
            blockU[i + locX] = cells[i+50]
            blockV[i + locX] = cells[i+60]
            blockW[i + locX] = cells[i+70]
            blockX[i + locX] = cells[i+80]
            blockY[i + locX] = cells[i+90]
        if locY == 16:
            blockQ[i + locX] = cells[i]
            blockR[i + locX] = cells[i+10]
            blockS[i + locX] = cells[i+20]
            blockT[i + locX] = cells[i+30]
            blockU[i + locX] = cells[i+40]
            blockV[i + locX] = cells[i+50]
            blockW[i + locX] = cells[i+60]
            blockX[i + locX] = cells[i+70]
            blockY[i + locX] = cells[i+80]
            blockZ[i + locX] = cells[i+90]

def save():
    f = open("world.py", "w")
    f.write("\nblockA = " + str(blockA) + "\nblockB = " + str(blockB) + "\nblockC = " + str(blockC) + "\nblockD = " + str(blockD) + "\nblockE = " + str(blockE) + "\nblockF = " + str(blockF) + "\nblockG = " + str(blockG) + "\nblockH = " + str(blockH) + "\nblockI = " + str(blockI) + "\nblockJ = " + str(blockJ) + "\nblockK = " + str(blockK) + "\nblockL = " + str(blockL) + "\nblockM = " + str(blockM) + "\nblockN = " + str(blockN) + "\nblockO = " + str(blockO) + "\nblockP = " + str(blockP) + "\nblockQ = " + str(blockQ) + "\nblockR = " + str(blockR) + "\nblockS = " + str(blockS) + "\nblockT = " + str(blockT) + "\nblockU = " + str(blockU) + "\nblockV = " + str(blockV) + "\nblockW = " + str(blockW) + "\nblockX = " + str(blockX) + "\nblockY = " + str(blockY) + "\nblockZ = " + str(blockZ))
    f.close()

locX = 0
locY = 0
#set the current map to world.py
loadMap(locY)

#var
currentCell = 1
selectCell = 1
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

    #gravity / down
    if noGravity == 0:
        if currentCell > 90:
            locY += 1
            loadMap(locY)
            if cells[currentCell] == 0:
                locY += 1
                loadMap(locY)
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
                if currentCell < 10:
                    if locY != 0:
                        locY -= 1
                    loadMap(locY)
                    if cells[currentCell] != 0:
                        currentCell += 10
                        selectCell += 10
                elif cells[currentCell - 10] == 0:
                    currentCell -= 10
                    if selectCell > 11:
                        selectCell -= 10
                if noGravity == 0 and not isJump:
                    noGravity = 2
                    isJump = True
    if keys[pygame.K_LEFT]:
        if True:
            if (currentCell - 1) / 10 == int((currentCell - 1) / 10):
                if locX!= 0:
                    locX-= 1
                    loadMap(locY)
                    if cells[currentCell] != 0:
                        currentCell += 1
                        selectCell += 1
            else:
                if cells[currentCell - 1] == 0:
                    currentCell -= 1
                    if (selectCell - 1) / 10 != int((selectCell - 1) / 10):
                        selectCell -= 1
    if keys[pygame.K_RIGHT]:
            if currentCell / 10 == int(currentCell / 10):
                locX= locX+ 1
                loadMap(locY)
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
    if keys[pygame.K_e]:
        cells[selectCell] = 0
        saveMap(locY)
    if keys[pygame.K_2]:
        cells[selectCell] = 2
        saveMap(locY)
    if keys[pygame.K_3]:
        cells[selectCell] = 3
        saveMap(locY)
    if keys[pygame.K_4]:
        cells[selectCell] = 4
        saveMap(locY)

    #i have no clue
    if prevCell != currentCell:
        cells[prevCell] = 0
    prevCell = currentCell

    #map movement
    loadMap(locY)

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
    saveMap(locY)
    save()

    #set the player
    cells[currentCell] = 1

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
        if selectCell == i:
            mainScreen.blit(pygame.image.load("select.png"), (cellX[i], cellY[i]))

    pygame.display.update()

pygame.quit()
