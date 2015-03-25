'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link


# servo ports
arm = 3
claw  = 1
razr = 0


# motor ports
grabber = 1 #arm that is lifts the grabby thingy


# servo positions
clawOpen = 0
clawClose = 2000

razrDown = 1950 
razrUp = 170

armDown = 1900
armMesa = 1080
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

# analog ports

ETport = 5

# digital ports
clonePort = 15 

# hard code for now, but will be clone switch
isClone = link.digital(15)
        

# define clone values here
if isClone:
    clawOpen = 0
    clawClose = 2000
    
    armDown = 1900
    armMesa = 1050
    armHeight = 780
    armMid = 600
    armUp = 550
    armSlightBack = 450
    armMidDown = 200 # for optimization
    armBackMesa = 40 # 30 before
    
