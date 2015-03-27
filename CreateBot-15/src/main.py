'''
Created on Mar 17, 2015

@author: Botball
'''


import actions as act
import constants as c


def main():
    act.init()

    act.driveToMesa() #using ET
    #act.getOutOfStartBox() #using no sensors
    act.turnToMesa()
    act.driveToBlock()
    act.grabBot()
    act.driveAndReset()
    act.endDrive()
    act.deliverBotgalOrPod()
    
    if act.checkForBotGalOrPod() == c.seeGreen:
        act.dumpPod()
    elif act.checkForBotGalOrPod() == c.seeRed:
        act.dumpBotgal()
    else:
        print "i see nothing"
    act.shutDown()


if __name__ == "__main__":
    main()
