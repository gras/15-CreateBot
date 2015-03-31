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
from constants import ETport, isClone

# sets up the claw and arm
def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running My Create"
    if c.isClone:
        print "Running Clone"
    else:
        print "Running Prime"
    
    link.create_connect()
    link.camera_open() 
    
    #insert wait_for_light here
    
    # preset servo positions
    servo.initServos()
    


def driveToMesa():
    drive.noStop( 100, 100, 2.0 )
    drive.withStop( 200, 200, 3.3) #was 3.2
    drive.noStop(-50, -50, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
        #print analog_et(5)
    print link.analog_et(c.ETport)
    if c.isClone:
        drive.withStop(-50, -50, 0.55) #.65
    else:
        drive.withStop(-75, -75, 0.60) #was 1.0
        

# turns to the right so that the arm can sweep the mesa
def turnToMesa():
    if c.isClone:
        drive.withStop( -250, 250, 0.735 ) #was 0.725
    else:
        drive.withStop( -250, 250, 0.750 ) #was 0.740

# sweeps part of the mesa
def driveToBlock():
    servo.moveArm( c.armBackMesa, 5 )
    if c.isClone:
        drive.withStop( 100, 100, 2.1)
    else:    
        drive.withStop( 100, 100, 1.800 )

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    link.motor( c.grabber, 65 ) #was 100
    t.sleep( 1.000 )
    link.motor( c.grabber, 0 )
    servo.moveRazr(c.razrMid, 40)
    servo.moveRazr(c.razrUp, 5)    
    link.motor( c.grabber, -80 ) #-100
    t.sleep( 2.000 ) #2.000 
    servo.moveRazr( c.razrStraightUp, 75)
    servo.moveRazr( c.razrDown, 10)
    link.motor( c.grabber, -60 )
   
    '''
def checkForBotGalOrPod(): 
    return s.cameraTrack()
    '''
    
# sweeps more of the mesa and stops to back up in order to change arm position
def driveAndReset():
    drive.withStop( 100, 100, 3.450 )
    drive.withStop( -100, -100, 0.250 )
    servo.moveArm( c.armUp, 5)
    drive.withStop( -100, -100, 6.400)

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    print 'end drive'
    servo.moveArm( c.armMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 6.500 )
    servo.openClaw() #dump blocks
    t.sleep(1.0)
    servo.moveArm( 850, 10 )
    drive.withStop( -100, -100, 5.200 ) #was 2.900
    servo.moveArm( c.armMesa, 5 )
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
    servo.moveArm(850, 10)
    drive.withStop(-100, -100, 2.500)
    drive.withStop(-50, 50, 4.00)
    servo.moveArm(c.armDown, 5 )
    
def dumpBotgal():
    #drive.withStop(100, 100, 6.0)
    if c.isClone:
        drive.withStop( 100, 100, 6.0)
    else:    
        drive.withStop( 100, 100, 7.0 )
    link.motor( c.grabber, 100 )
    t.sleep (1.000)
    
def dumpPod():
    drive.noStop(-300,-300,0)
    #drive.withStop(-200, -200, 6.0)
    while not link.get_create_rbump() and not link.get_create_lbump():
        pass
    drive.noStop(0,0,0)
    link.motor( c.grabber, 75 ) #was 100
    t.sleep (1.000)
    
def shutDown():
    link.create_disconnect()
    

def DEBUG( msg = "DEBUG" ):
    print msg
    link.ao()
    exit()

