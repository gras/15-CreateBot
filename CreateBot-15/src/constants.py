'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link


# globalconstants
isClone = link.digital(15)
isPrime = not isClone

# servo ports
grabberArm = 0
cubeHolder  = 1
grabber = 2 #cubeHolder that will grab botgal or pod
cubeHolderArm = 3

# servo positions
cubeHolderOpen = 650
cubeHolderClose = 1550

grabberArmUp = 200 #was 250
grabberArmStraightUp = 550
grabberArmDrop = 1000
grabberArmDown = 2000 #was 1750

cubeHolderArmDown = 1800 #1900
cubeHolderArmMesa = 1100 #was 1150
#cubeHolderArmHeight = 780
cubeHolderArmMid = 850
cubeHolderArmUp = 510
cubeHolderArmSlightBack = 350
cubeHolderArmMidDown = 200 # for optimization
cubeHolderArmBackMesa = 0 # 30 before

grabberClosed = 150
grabberOpen = 1600

#motor ports
grabberArm = 0

#camera constants
blobSize = 750
chanGreen = 0
chanRed = 1
seeNot = 0
seeRed = 1
seeGreen = 2

# analog ports

ETport = 5

# digital ports
clonePort = 15 



# define clone values here
if isClone:
    cubeHolderOpen = 0
    cubeHolderClose = 2000
    
    cubeHolderArmDown = 1900
    cubeHolderArmMesa = 1125
    cubeHolderArmHeight = 780
    cubeHolderArmMid = 600
    cubeHolderArmUp = 550
    cubeHolderArmSlightBack = 450
    cubeHolderArmMidDown = 200 # for optimization
    cubeHolderArmBackMesa = 40 # 30 before
    
    grabberArmUp = 120
    grabberArmStraightUp = 400
    grabberArmMid = 750
    grabberArmDown = 1750 

#isClone