'''
Created on Mar 17, 2015

@author: Botball
'''

import os
import sys
import time as t

import kovan as link

import constants as c
import drive
import servo
import sensor as s

# sets up the cubeHolder and cubeHolderArm
def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running My Create"
    
       
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"
    
    link.create_connect()
    link.camera_open() 
    
    #insert wait_for_light here
    
    # preset servo positions
    servo.initServos()
    


def driveToMesa():
    drive.noStop( 100, 100, 2.0 )
    servo.movecubeHolderArm(c.cubeHolderArmUp, 20)
    drive.withStop( 200, 200, 3.3) #was 3.2
    drive.noStop(-50, -50, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
        #print analog_et(5)
    print link.analog_et(c.ETport)
    if c.isPrime:
        drive.withStop(-75, -75, 0.65) #was 1.0 then 0.60
    else:
        drive.withStop(-50, -50, 0.45) #.65
        

# turns to the right so that the cubeHolderArm can sweep the mesa
def turnToMesa():
    if c.isPrime:
        drive.withStop( -250, 250, 0.750 ) #was 0.770
    else:
        drive.withStop( -250, 250, 0.735 ) #was 0.725

# sweeps part of the mesa. drives to the pod or botgal
def driveToBlock():
    servo.movecubeHolderArm( c.cubeHolderArmBackMesa, 5 )
    if c.isPrime:
        drive.withStop( 100, 100, 1.800 )
    else:    
        drive.withStop( 100, 100, 2.1)

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    servo.openGrabber()#opening grabber
    t.sleep( 1.000 )
    
    # reverting grabberArm to a motor
    link.motor(c.grabberArm, -100)
    t.sleep(1.0)
    link.motor(c.grabberArm, 0)
    t.sleep(1.0)
    
    # using grabberArm as a servo
    #servo.movegrabberArm( c.grabberArmUp, 10)
    #t.sleep( 1.000 )
    
    servo.closeGrabber()
    t.sleep(1.000 )
    
    # using grabberArm as a servo
    #servo.movegrabberArm( c.grabberArmMid, 2000)
    #t.sleep( 1.000)
    #ervo.movegrabberArm( c.grabberArmDown, 10)
    #link.disable_servo( c.grabberArm)
    
    #using grabberArm as a motor    
    link.motor( c.grabberArm, 100 )
    t.sleep(2.5)
    link.motor( c.grabberArm, 0 )
    DEBUG() 
    '''
def checkForBotGalOrPod(): 
    return s.cameraTrack()
    '''
    
# sweeps more of the mesa and stops to back up in order to change cubeHolderArm position
def driveAndReset():
    drive.withStop( 100, 100, 3.450 )
    drive.withStop( -100, -100, 0.250 )
    servo.movecubeHolderArm( c.cubeHolderArmUp, 5)
    drive.withStop( -100, -100, 6.400)

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    print 'end drive'
    servo.movecubeHolderArm( c.cubeHolderArmMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 6.500 )
    servo.opencubeHolder() #dump blocks
    t.sleep(1.0)
    servo.movecubeHolderArm( 850, 10 )
    drive.withStop( -100, -100, 5.200 ) #was 2.900
    servo.movecubeHolderArm( c.cubeHolderArmMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 5.300 ) #was 3.000
    print 'end of endDrive'   
    
    
def checkColorAndDrive():
    print 'check color and drive'
    check = s.checkForBotGalOrPod()
    print check
    deliverBotgalOrPod()
    if check == c.seeGreen:
        print "dump pod"
        dumpPod()
    elif check == c.seeRed:
        print "dump botgal"
        dumpBotgal()
    else:
        print "i see nothing,"
   

def deliverBotgalOrPod():
    servo.movecubeHolderArm(850, 10)
    drive.withStop(-100, -100, 2.500)
    drive.withStop(-50, 50, 4.00)
    servo.movecubeHolderArm(c.cubeHolderArmDown, 5 )
    
def dumpPod():
    #drive.withStop(100, 100, 6.0)
    if c.isPrime:
        drive.withStop( 100, 100, 7.0 )
    else:    
        drive.withStop( 100, 100, 6.0)
    servo.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def dumpBotgal():
    drive.noStop(-300,-300,0)
    #drive.withStop(-200, -200, 6.0)
    while not link.get_create_rbump() and not link.get_create_lbump():
        pass
    drive.noStop(0,0,0)
    servo.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def shutDown():
    link.create_disconnect()
    

def DEBUG( msg = "DEBUG" ):
    print msg
    link.ao()
    exit()

