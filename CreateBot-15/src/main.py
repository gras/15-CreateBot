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
    #act.deliverBotgalOrPod()
    act.checkColorAndDrive()
    
        
    act.shutDown()
    #act.DEBUG("Done")
    


if __name__ == "__main__":
    main()
    #act.grabBot()