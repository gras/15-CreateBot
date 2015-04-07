'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import constants as c
import time as t

def initServos():
    link.enable_servos()
    link.set_servo_position(c.claw, c.clawClose)
    link.set_servo_position(c.grabber, c.grabberClosed)
    link.set_servo_position(c.razr, c.razrMid )
    link.set_servo_position(c.razr, c.razrDown )
    link.set_servo_position(c.arm, c.armDown - 20)
    t.sleep(1)
    link.set_servo_position(c.arm, c.armDown) 
    moveArm(c.armSlightBack, 10)

def moveArm( endPos, speed=10 ):
    now = link.get_servo_position( c.arm )
    if now > endPos:
        speed = -speed
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.arm, i )
        t.sleep( 0.010 )
    #for
    
    link.set_servo_position( c.arm, endPos )
    t.sleep( 0.010 )

def openClaw():
    link.set_servo_position( c.claw, c.clawOpen )

def closeClaw():
    link.set_servo_position( c.claw, c.clawClose )
    
def openGrabber():
    link.set_servo_position( c.grabber, c.grabberOpen)
    
def closeGrabber():
    link.set_servo_position( c.grabber, c.grabberClosed)

def moveGrabber( endPos, speed=10 ):
    now = link.get_servo_position( c.grabber )
    if now > endPos:
        speed = -speed
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.grabber, i )
        t.sleep( 0.010 )
    #for

def moveRazr( endPos, speed=10):
    now = link.get_servo_position( c.razr )
    if now > endPos:
        speed = -speed
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.razr, i )
        t.sleep( 0.010 )
    #for
    
    link.set_servo_position( c.razr, endPos )
    t.sleep( 0.010 )
   

