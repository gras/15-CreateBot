'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

# servo ports
arm = 3
claw  = 1

# motor ports
grabber = 2
razr = 3

# servo positions
clawOpen = 0
clawClose = 2000
armUp = 510
armMesa = 1100
armHeight = 780
armMid = 600
armMidDown = 200 # for optimization
armDown = 40 # 30 before

# analog ports


# digital ports
isClone = 0 #link.digital(15)
# hard code for now, but will be clone switch


# define clone values here
if isClone:
    clawOpen = 0
    clawClose = 2000
    armUp = 510
    armMesa = 1050
    armHeight = 780
    armMid = 600
    armMidDown = 200 # for optimization
    armDown = 40 # 30 before
#isClone