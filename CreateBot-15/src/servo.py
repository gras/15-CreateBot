'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import constants as c
import time as t
from constants import grabberClosed

def initServos():
    cubeHolderArmDown()
    openGrabber()
    closecubeHolder()
    grabberArmDown()
    link.enable_servos()
    print "testing cubeHolder"
    opencubeHolder()
    t.sleep(1)#was.4
    closecubeHolder()
    t.sleep(1)#was.4
    print "testing cubeHolderArm"
    cubeHolderArmUp()
    t.sleep(1)
    cubeHolderArmDown()
    t.sleep(1)
    print "testing grabber"
    closeGrabber()
    t.sleep(1)
    openGrabber()
    t.sleep(1)#was.4
    print "testing grabberArm"
    grabberArmUp()
    t.sleep(1)
    grabberArmDown()
    t.sleep(1)
    #link.set_servo_position(c.grabberArm, c.grabberArmMid )
    #link.set_servo_position(c.grabberArm, c.grabberArmDown )
    
    """ UNCOMMENT THESE FOR TESTING FROM START BOX. THESE ARE COMMENTED TO TEST
        GRABBING BOT GAL WITH grabberArm REVERTED TO A MOTOR.
    
    
    link.set_servo_position(c.cubeHolderArm, c.cubeHolderArmDown - 20)
    t.sleep(1)
    link.set_servo_position(c.cubeHolderArm, c.cubeHolderArmDown) 
    movecubeHolderArm(c.cubeHolderArmSlightBack, 10)
    """

def movecubeHolderArm( endPos, speed=10 ):
    now = link.get_servo_position( c.cubeHolderArm )
    if now > endPos:
        speed = -speed 
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.cubeHolderArm, i )
        t.sleep( 0.010 )
    #for
    
    link.set_servo_position( c.cubeHolderArm, endPos )
    t.sleep( 0.010 )

def opencubeHolder():
    link.set_servo_position( c.cubeHolder, c.cubeHolderOpen )

def closecubeHolder():
    link.set_servo_position( c.cubeHolder, c.cubeHolderClose )
    
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

def movegrabberArm( endPos, speed=10):
    now = link.get_servo_position( c.grabberArm )
    if now > endPos:
        speed = -speed
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.grabberArm, i )
        t.sleep( 0.010 )
    #for
    
    link.set_servo_position( c.grabberArm, endPos )
    t.sleep( 0.010 )
   
def cubeHolderArmDown():
    #link.set_servo_position(c.cubeHolderArm, 2047)
    movecubeHolderArm( 2047, 10)
    
def cubeHolderArmUp():
    #link.set_servo_position( c.cubeHolderArm, c.cubeHolderArmDown )
    movecubeHolderArm( c.cubeHolderArmUp, 15)
    
def grabberArmUp():
    movegrabberArm( c.grabberArmMid, 10 )
    
def grabberArmDown():
    movegrabberArm( 2047, 10 )
