'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import constants as c
import time as t

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
#moveArm

def openClaw():
    link.set_servo_position( c.claw, c.clawOpen )
#openClaw

def closeClaw():
    link.set_servo_position( c.claw, c.clawClose )
    
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
   
#move razr down

