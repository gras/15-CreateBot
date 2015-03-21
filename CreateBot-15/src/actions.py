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
from constants import clonePort, armDown
from kovan import analog_et

# sets up the claw and arm
def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running My Create"
    if c.isClone:
        print "Running Clone"
    #if
    else:
        print "Running Prime"
    #else
    
    link.create_connect()
    
    # preset servo positions
    link.enable_servos()
    servo.closeClaw()
    link.motor( c.razr, -30 )
    t.sleep (1.000)
    link.motor( c.razr, 0 )
    link.set_servo_position( c.arm, c.armUp )
    #wait_for_light

# drives forward to start box
def getOutOfStartBox():
    drive.noStop( 100, 100, 2.0 )
    drive.noStop( 200, 200, 2.8 )

# turns to the right so that the arm can sweep the mesa
def turnToMesa():
    if c.isClone:
        drive.withStop( -250, 250, 0.725 ) #was 0.725
    else:
        drive.withStop( -250, 250, 0.72 ) #was 0.740

def driveToMesa():
    drive.noStop( 100, 100, 2.0 )
    drive.withStop( 200, 200, 3.0 ) #was 2.8
    print analog_et(5)
    drive.noStop(-50, -50, 0)
    while ( analog_et(5) > 350):
        print analog_et(5)
    drive.withStop(-50, -50, .45)
    

    
    

# sweeps part of the mesa
def driveToBlock():
    # link.set_servo_position( c.arm, c.armMidDown )
    # t.sleep( 1.500 ) check again
    # nnnnnarmdset_servo_position( c.arm, c.armBackMesa )
    servo.moveArm( c.armBackMesa, 5 )
    #t.sleep( 1.500 )
    drive.withStop( 100, 100, 1.800 )
    # t.sleep( 5.000 ) # check and remove the block!

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    link.motor( c.grabber, -100 )
    t.sleep( 1.000 )
    link.motor( c.grabber, 0 )
    t.sleep( 2.000 )
    link.motor( c.razr, 100 )
    t.sleep( 2.000 )
    link.motor( c.grabber, 100 )
    t.sleep(2.000 )
    link.motor( c.grabber, 0)
    link.motor( c.razr, 50 ) 
    
# sweeps more of the mesa and stops to back up in order to change arm position
def driveAndReset():
    drive.withStop( 100, 100, 3.450 )
    drive.withStop( -100, -100, 0.250 )  
    servo.moveArm( c.armUp, 5)
    #t.sleep( 5.000 )
    drive.withStop( -100, -100, 6.400)
    # t.sleep( 2.000 )
    
    #link.set_servo_position( c.arm, c.armHeight )
    #servo.moveArm( c.armHeight, 5 )
    #t.sleep( 1.500 )
    #link.set_servo_position( c.arm, c.armMesa )

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    servo.moveArm( c.armMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 6.150 )
    servo.openClaw()
    servo.moveArm(850, 10)
    drive.withStop( -100, -100, 0.700 ) #was 0.500
    drive.withStop( -100, -100, 2.000 ) #was 0.700
    servo.moveArm( c.armMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 2.500 ) #was 1.000
    
def deliverBotgalOrPod():
    servo.moveArm(850, 10)
    drive.withStop(-100, -100, 2.500)
    drive.withStop(-50, 50, 4.00)
    servo.moveArm(armDown, 5 )
    

    
    
    
def dumpBotgal():
    drive.withStop(100, 100, 6.0)  
    link.motor( c.razr, -30 )
    t.sleep (1.000)
    
def dumpPod():
    #drive.withStop(-50, 50, 8.0)
    drive.withStop(-200, -200, 6.0)
    link.motor( c.razr, -30 )
    t.sleep (1.000)
    

def DEBUG( msg = "DEBUG" ):
    print msg
    link.ao()
    exit()
#DEBUG
