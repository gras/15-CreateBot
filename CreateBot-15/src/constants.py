'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link


# globalconstants
isClone = link.digital(15)

# servo ports
razr = 0
claw  = 1
grabber = 2 #claw that will grab botgal or pod
arm = 3


# servo positions
clawOpen = 0
clawClose = 2000

razrUp = 0
razrStraightUp = 400
razrMid = 750
razrDown = 1750

armDown = 1800 #1900
armMesa = 1150
armHeight = 780
armMid = 600
armUp = 510
armSlightBack = 450
armMidDown = 200 # for optimization
armBackMesa = 40 # 30 before

grabberClosed = 200
grabberOpen = 1600

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
    clawOpen = 0
    clawClose = 2000
    
    armDown = 1900
    armMesa = 1125
    armHeight = 780
    armMid = 600
    armUp = 550
    armSlightBack = 450
    armMidDown = 200 # for optimization
    armBackMesa = 40 # 30 before
    
    razrUp = 120
    razrStraightUp = 400
    razrMid = 750
    razrDown = 1750 

#isClone