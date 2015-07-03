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
    green = act.checkColor()
    if green :
        #act.waitForLego(25)
        act.backAwayFromBin()
        act.dumpPod()
        act.podToFrisbee()
        
    else :
        #act.waitForLego(17)
        act.backAwayFromBin()
        act.dumpBotgal()
        act.botgalToFrisbee()
    #act.DEBUG("msg")  
    act.moveToEastWall()#MIDDLE WALL
    act.moveToFrisbee()
    act.grabFrisbee() 
    #act.deliverFrisbeeToNorthEndZone()
    if green:
        act.deliverFrisbeeToStartBox()
    else :
        act.deliverFrisbeeToNorthEndZone()
    
    act.shutDown()
    

if __name__ == "__main__":
    main()
