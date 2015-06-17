'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

# globalconstants
isClone = link.digital(15)
isPrime = not isClone

# motor ports
cubeGrabber = 2

# servo ports
grabberArm = 0
grabber = 1 #cubeHolder that will grab botgal or pod
frisbeeGrabber = 2
cubeHolderArm = 3

grabberArmUp = 200 #was 250
grabberArmStraightUp = 550
grabberArmMid = 650 #was 550
grabberArmDrop = 1000
grabberArmRelease = 1800
grabberArmDown = 2000 #was 1750

cubeHolderArmCompleteDown = 2000
cubeHolderArmDown = 1900 #was 1800
cubeHolderArmParallel= 1400
cubeHolderArmMesa = 1100 #was 1150
cubeHolderArmMid = 850
cubeHolderArmUp = 510
cubeHolderArmSlightBack = 350
cubeHolderArmMidDown = 200 # for optimization
cubeHolderArmBackMesa = 0 # 30 before

frisbeeGrabberOpen = 80
frisbeeGrabberClose = 2000


grabberClosed = 150
grabberMidClosed = 1100
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

ETport = 2
stoptime= 0

# digital ports
clonePort = 15 



# define clone values here
if isClone:
    frisbeeGrabberOpen = 80
    frisbeeGrabberClose = 2000
    
    cubeHolderArmCompleteDown = 2047
    cubeHolderArmDown = 1900
    cubeHolderArmMesa = 1110
    cubeHolderArmMid = 600
    cubeHolderArmUp = 550
    cubeHolderArmSlightBack = 450
    cubeHolderArmMidDown = 200 # for optimization
    cubeHolderArmBackMesa = 100 # 40 before
    #cubeholderArmSlightUp = 
    
    grabberArmUp = 120
    grabberArmStraightUp = 400
    grabberArmMid = 650 #was 550
    grabberArmBack = 850 
    grabberArmFrisbee = 1100
    grabberArmDown = 1840
    grabberArmFrisbeeAproach = 485

#isClone