'''
Created on Mar 17, 2015

@author: Botball
'''


import actions as act


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
    act.checkForBotGalOrPod()
    act.DEBUG()
    act.dumpBotgal()
    act.dumpPod()
    
    act.shutDown()


if __name__ == "__main__":
    main()
