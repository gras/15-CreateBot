'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import constants as c
import time as t
#from constants import grabberClosed
import actions as act 
from constants import frisbeeGrabberOpen, grabberArmStraightUp


def initServos():
    link.set_servo_position( c.cubeHolderArm, c.cubeHolderArmCompleteDown)
    #closecubeHolder()
    link.set_servo_position( c.grabberArm, c.grabberArmDown)
    link.enable_servos()
    t.sleep(2);
    print "testing cubeHolder"
    opencubeHolder()
    t.sleep(.2)#was.4
    link.motor(c.cubeGrabber,0)
    t.sleep(1)
    closecubeHolder()
    t.sleep(.15)#was.4
    link.motor(c.cubeGrabber,0)
    t.sleep(1)
    print "testing cubeHolderArm"
    cubeHolderArmUp()
    t.sleep(1)
    if link.analog_et(c.ETport) > 350:
        act.DEBUG("et sensor test failed: cubeArmHolder in the way")
    else:
        print "et sensor test passed"
    cubeHolderArmCompleteDown()
    t.sleep(1)
    link.disable_servo(c.cubeHolderArm)
    print "testing grabberArm"
    grabberArmStraightUp()
    t.sleep(1) #was 1
    link.disable_servo(c.cubeHolderArm)
    print "testing grabber"
    closeGrabber()
    t.sleep(1)
    openGrabber()
    t.sleep(1)#was.4
    link.disable_servo(c.grabber)
    grabberArmDown()
    link.disable_servo(c.grabberArm)
    frisbeeGrabberOpen()
    t.sleep(1);
    frisbeeGrabberClose()
    link.disable_servo(c.frisbeeGrabber)
    

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
    link.motor(c.cubeGrabber,-50)
    
#  def opencubeHolderWide():
#  link.set_servo_position( c.cubeHolder, c.cubeHolderOpenWide )

def closecubeHolder():
    link.motor(c.cubeGrabber,50)
    
def openGrabber():
    link.set_servo_position( c.grabber, c.grabberOpen)
    
def SlowOpenGrabber():
    moveGrabber(c.grabberOpen, 5)
    
def midCloseGrabber():
    moveGrabber( c.grabberMidClosed, 5)
    
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
    movecubeHolderArm( c.cubeHolderArmUp, 10)
    
def cubeHolderArmSlightBack():
    movecubeHolderArm( c.cubeHolderArmSlightBack, 10)
    
def cubeHolderArmBackMesa():
    movecubeHolderArm( c.cubeHolderArmBackMesa, 5)
    
def cubeHolderArmMid():
    movecubeHolderArm( c.cubeHolderArmMid, 10)
    
def cubeHolderArmMesa():
    movecubeHolderArm( c.cubeHolderArmMesa, 5)
    
def cubeHolderArmParallel():
    movecubeHolderArm( c.cubeHolderArmParallel, 10)
    
def cubeHolderArmSlightUp():
    movecubeHolderArm( c.cubeHolderArmSlightUp, 5)
    
def grabberArmStraightUp():
    movegrabberArm( c.grabberArmStraightUp, 5) 
       
def grabberArmUp():
    movegrabberArm( c.grabberArmUp, 5 )
    
def grabberArmDown():
    movegrabberArm( c.grabberArmDown, 10 )
    
def grabberArmMid():
    movegrabberArm( c.grabberArmMid,10)
    
def grabberArmFribee():
    movegrabberArm( c.grabberArmFrisbee, 5)
    
def grabberArmDrop():
    movegrabberArm( c.grabberArmDrop, 10 )
    
def grabberArmRelease():
    movegrabberArm( c.grabberArmRelease, 5 )

def frisbeeGrabberOpen():
    link.set_servo_position( c.frisbeeGrabber, c.frisbeeGrabberOpen )

def frisbeeGrabberClose():
    link.set_servo_position( c.frisbeeGrabber, c.frisbeeGrabberClose )
    
