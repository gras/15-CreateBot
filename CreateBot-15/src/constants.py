'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link


# globalconstants
isClone = link.digital(15)

# servo ports
arm = 3
claw  = 1
razr = 0

# motor ports
grabber = 1 


# servo positions
clawOpen = 0
clawClose = 2000

razrDown = 1750 
razrUp = 0
razrMid = 750
razrStraightUp = 400

armDown = 1900
armMesa = 1150
armHeight = 780
armMid = 600
armUp = 510
armSlightBack = 450
armMidDown = 200 # for optimization
armBackMesa = 40 # 30 before

#camera constants
blobSize = 750
chanGreen = 0
chanRed = 1
seeRed = 1
seeGreen = 2
seeNot = 0

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
    
    razrDown = 1750 
    razrUp = 120
    razrMid = 750
    razrStraightUp = 400

#isClone