'''
Created on Mar 17, 2015

@author: Botball
'''

import actions as act


def main():
    
    act.init()
    
    act.driveToMesa() #using ET
    act.turnToMesa()
    act.driveToBlock()
    act.grabBot()
    act.driveAndReset()
    act.endDrive()
    #act.DEBUG("swag")
    act.waitForLego(25)
    check = act.checkColorAndDrive()
    if check :
        act.liftGrabberArmForPod()
        act.backAwayFromBin()
        act.dumpPod()
        act.podToFrisbee()
    else :
        act.backAwayFromBin()
        act.dumpBotgal()
        act.botgalToFrisbee()
    act.moveToEastWall()
    act.moveToFrisbee()
    act.grabFrisbee() 
    if check:
        act.deliverFrisbeeToStartBox()
    else :
        act.deliverFrisbeeToNorthEndZone()
    
    act.shutDown()
    

if __name__ == "__main__":
    main()
