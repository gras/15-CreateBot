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

grabberArmUp = 120 
grabberArmBack = 375
grabberArmStraightUp = 550
grabberArmMid = 650 #was 550
grabberArmGrabFrisbee = 850 #675
grabberArmFinal = 750
grabberArmDrop = 1000
grabberArmClear = 1400
grabberArmHover = 1500
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
frisbeeGrabberClose = 1100

grabberClosed = 300 #150 385
grabberClearClosed = 575
grabberOpenInit = 750
grabberMidClosed = 850 #was 950
grabberOpen = 1600

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
    frisbeeGrabberOpen = 1000
    frisbeeGrabberClose = 2000
    
    cubeHolderArmCompleteDown = 2047
    cubeHolderArmDown = 1900
    cubeHolderArmMesa = 1050
    cubeHolderArmMid = 600
    cubeHolderArmUp = 550
    cubeHolderArmSlightBack = 450
    cubeHolderArmMidDown = 200 # for optimization
    cubeHolderArmBackMesa = 150 # 40 before
    #cubeholderArmSlightUp = 
  
    grabberArmUp = 120
    grabberArmBack = 400 
    grabberArmFrisbeeAproach = 485
    grabberArmStraightUp = 600
    grabberArmMid = 650 #was 550
    grabberArmGrabFrisbee = 750
    grabberArmFrisbee = 1100
    grabberArmClear = 1400
    grabberArmDown = 1840
    
    grabberMidClosed = 950 
    
#isClone