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
import sensor


def getOutOfStartBox():
    drive.noStop( 100, 100, 2.0 )
    drive.noStop( 200, 200, 2.8 )
#getOutOfStartBox

def turnToMesa():
    if c.isClone:
        drive.withStop( -250, 250, 0.750 ) # 0.725
    #if
    else:
        drive.withStop( -250, 250, 0.740 ) # 0.725
    #else
    
    #drive.withStop( 100, 100, 1600 )
    
#turnToMesa

def driveToBlock():
    # link.set_servo_position( c.arm, c.armMidDown )
    # t.sleep( 1.500 ) check again
    # nnnnnarmdset_servo_position( c.arm, c.armDown )
    servo.moveArm( c.armDown, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 1.800 )
    t.sleep( 5.000 ) # check and remove the block!
#toBlock

def driveAndReset():
    if c.isClone:
        drive.withStop( 100, 100, 3.450 )
        servo.moveArm( c.armUp, 5)
        #t.sleep( 5.000 )
        drive.withStop( -100, -100, 6.400)
        t.sleep( 2.000 )
    #if
    else: 
        drive.withStop( 100, 100, 3.450 )
        drive.withStop( -100, -100, 0.250 )
        servo.moveArm( c.armUp, 5 )
        #t.sleep( 5.000 )
        drive.withStop( -100, -100, 6.400 )
        t.sleep( 2.000 )
    #else
    
    #link.set_servo_position( c.arm, c.armHeight )
    #servo.moveArm( c.armHeight, 5 )
    #t.sleep( 1.500 )
    #link.set_servo_position( c.arm, c.armMesa )
    
#driveAndReset

def endDrive():
    servo.moveArm( c.armMesa, 5 )
    t.sleep( 1.500 )
    drive.withStop( 100, 100, 6.100 )
    servo.openClaw()
    drive.withStop( -100, -100, 0.500 )
    DEBUG()
    # poms delivered at this point
    # return
    
#endDrive


def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running Create"
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
    link.set_servo_position( c.arm, c.armUp )
    #wait_for_light
    
#init

def DEBUG( msg = "DEBUG" ):
    print msg
    link.ao()
    exit()
#DEBUG
