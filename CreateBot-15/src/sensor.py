'''
Created on Mar 17, 2015

@author: Botball
'''
import kovan as link
import constants as c
import time
import actions as act

def lookForGreen() :
    print "cameraTrack"
    link.camera_update()
    time.sleep (0.5)
    
    #$####################
    print "waiting until we see something"
    for i in range(15):
        print "i: ", i
        greenArea = link.get_object_area( c.chanGreen, 0 )
        redArea = link.get_object_area( c.chanRed, 0 )
        print "green: ", greenArea
        print "red: ", redArea
        if greenArea > c.blobSize:
            break
        elif redArea > c.blobSize:
            break
        link.camera_update()
        time.sleep( 0.02 )
    
    ######################
    
    if link.get_object_area( c.chanGreen, 0 ) >= c.blobSize:
        print "green"
        print link.get_object_area( c.chanGreen, 0 )  
        return True
    print "green not seen"
    return False

def testETScanner():
    if link.analog_et(c.ETport) > 350:
        act.DEBUG("et sensor test failed: cubeArmHolder in the way")
    else:
        print "et sensor test passed"
