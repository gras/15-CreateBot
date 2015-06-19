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
    
    #act.waitForLego(25)
    act.checkColorAndDrive()
    act.podToFrisbee()
    act.moveToFrisbee()
    
    
    #act.newCubeTest()
    
    print "Working"
    #act.moveToFrisbee()
    act.grabFrisbee()
    act.frisbeeToBotgal()
    act.DEBUG("swag")

    
    #act.grabCubes()
    #act.shutDown()
    #act.kill()
    
    

if __name__ == "__main__":
    main()
    #act.grabBot()