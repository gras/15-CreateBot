'''
Created on Mar 17, 2015

@author: Botball
'''


import actions as act




def main():
    '''
    act.init()
    
    #READ INITMOVES IN THE MOVEMENT FILE
    
    act.driveToMesa() #using ET
    act.turnToMesa()
    act.driveToBlock()
    act.grabBot()
    act.driveAndReset()
    act.endDrive()
    act.DEBUG("please work")
    act.waitForLego(25)
    act.checkColorAndDrive()
    act.newCubeTest()
    '''
    print "Working"
    act.moveToFrisbee()
    act.grabFrisbee()
    act.frisbeeToBotgal()
    act.DEBUG("Yup")

    
    #act.grabCubes()
    #act.shutDown()
    #act.kill()
    
    

if __name__ == "__main__":
    main()
    #act.grabBot()