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
    act.waitForLego(20)
    check = act.checkColorAndDrive()
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
    #act.grabBot()