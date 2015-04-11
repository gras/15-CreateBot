'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import constants as c
import time as t
#from constants import grabberClosed
import actions as act 


def initServos():
    link.set_servo_position( c.cubeHolderArm, c.cubeHolderArmCompleteDown)
    closecubeHolder()
    openGrabber()
    link.set_servo_position( c.grabberArm, c.grabberArmDown)
    link.enable_servos()
    print "testing cubeHolder"
    opencubeHolder()
    t.sleep(1)#was.4
    closecubeHolder()
    t.sleep(1)#was.4
    print "testing cubeHolderArm"
    cubeHolderArmSlightBack()
    t.sleep(1)
    if link.analog_et(c.ETport) > 350:
        act.DEBUG("et sensor test failed: cubeArmHolder in the way")
    else:
        print "et sensor test passed"
    cubeHolderArmCompleteDown()
    t.sleep(1)
    print "testing grabber"
    closeGrabber()
    t.sleep(1)
    openGrabber()
    t.sleep(1)#was.4
    print "testing grabberArm"
    grabberArmUp()
    t.sleep(.5) #was 1
    grabberArmDown()
    t.sleep(3)
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
   
def cubeHolderArmCompleteDown():
    movecubeHolderArm( c.cubeHolderArmCompleteDown, 10)
    
def cubeHolderArmDown():
    movecubeHolderArm( c.cubeHolderArmDown, 10)
    
def cubeHolderArmUp():
    movecubeHolderArm( c.cubeHolderArmUp, 5)
    
def cubeHolderArmSlightBack():
    movecubeHolderArm( c.cubeHolderArmSlightBack, 10)
    
def cubeHolderArmBackMesa():
    movecubeHolderArm( c.cubeHolderArmBackMesa, 5)
    
def cubeHolderArmMid():
    movecubeHolderArm( c.cubeHolderArmMid, 10)
    
def cubeHolderArmMesa():
    movecubeHolderArm( c.cubeHolderArmMesa, 5)
    
def grabberArmUp():
    movegrabberArm( c.grabberArmUp, 10 )
    
def grabberArmDown():
    movegrabberArm( c.grabberArmDown, 10 )
    
def grabberArmDrop():
    movegrabberArm( c.grabberArmDrop, 10 )
