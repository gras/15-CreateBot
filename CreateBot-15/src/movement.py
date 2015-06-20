'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

#import motor as m
import constants as c
import time as t
#from constants import grabberClosed
import actions as act 
from constants import frisbeeGrabberOpen, grabberArmStraightUp
from sensor import testETScanner


def initMoves():
    
    testCubeHolder()
    testCubeHolderArm()
    testGrabberArm()
    testGrabber()
    testFrisbeeGrabber()
    

def testCubeHolder():
    print "testing cubeHolder"
    opencubeHolder( 0.2 )
    #t.sleep(.5)
    closecubeHolder( 0.2 )
    #t.sleep(.5) 

def testCubeHolderArm():
    print "testing cubeHolderArm"
    link.set_servo_position( c.cubeHolderArm, c.cubeHolderArmCompleteDown)
    link.enable_servo( c.cubeHolderArm)
    cubeHolderArmSlightBack() 
    t.sleep(.5)
    testETScanner
    cubeHolderArmCompleteDown() 
    t.sleep(.5)
    link.disable_servo(c.cubeHolderArm)
    
def testGrabberArm():
    print "testing grabberArm"
    link.set_servo_position( c.grabberArm, c.grabberArmDown)
    link.enable_servo( c.grabberArm) 
    grabberArmStraightUp()
    #t.sleep(1) #was 1
    link.disable_servo(c.cubeHolderArm)
    
def testGrabber():
    print "testing grabber"
    link.set_servo_position( c.grabber, c.grabberClosed)
    link.enable_servo( c.grabber)
    closeGrabber()
    t.sleep(.5)
    openGrabber()
    t.sleep(.5)#was.4
    link.disable_servo(c.grabber)
    
def testFrisbeeGrabber():
    print "test frisbeeGrabber"
    link.set_servo_position( c.frisbeeGrabber, c.frisbeeGrabberClose)
    link.enable_servo( c.frisbeeGrabber)
    frisbeeGrabberOpen()
    t.sleep(.5);
    frisbeeGrabberClose()
    link.disable_servo(c.frisbeeGrabber)
    grabberArmDown()
    link.disable_servo(c.grabberArm)
    
    

def opencubeHolder( secs ):
    link.motor( c.cubeGrabber, -30 )
    t.sleep( secs );
    link.motor( c.cubeGrabber, 0 )
    
    
def closecubeHolder( secs ):
    link.motor( c.cubeGrabber, 30 )
    t.sleep( secs );
    link.motor( c.cubeGrabber, 0 )

def gripCubes():
    link.motor( c.cubeGrabber, 10 )

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


    
#  def opencubeHolderWide():
#  link.set_servo_position( c.cubeHolder, c.cubeHolderOpenWide )


    

    
def SlowOpenGrabber():
    moveGrabber( c.grabberOpen, 5 )
    
def midCloseGrabber():
    moveGrabber( c.grabberMidClosed, 5 )
    
def openGrabber():
    link.set_servo_position( c.grabber, c.grabberOpen )
    
def closeGrabber():
    link.set_servo_position( c.grabber, c.grabberClosed )

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

def moveFrisbeeGrabber( endPos, speed=10):
    now = link.get_servo_position( c.frisbeeGrabber )
    if now > endPos:
        speed = -speed
    #if
    
    for i in range ( now, endPos, speed ):
        link.set_servo_position( c.frisbeeGrabber, i )
        t.sleep( 0.010 )
    #for
    
    link.set_servo_position( c.frisbeeGrabber, endPos )
    t.sleep( 0.010 )


   
def cubeHolderArmCompleteDown():
    movecubeHolderArm( c.cubeHolderArmCompleteDown, 10 )
    
def cubeHolderArmDown():
    movecubeHolderArm( c.cubeHolderArmDown, 10 )
    
def cubeHolderArmUp():
    movecubeHolderArm( c.cubeHolderArmUp, 10 )
    
def cubeHolderArmSlightBack():
    movecubeHolderArm( c.cubeHolderArmSlightBack, 10 )
    
def cubeHolderArmBackMesa():
    movecubeHolderArm( c.cubeHolderArmBackMesa, 5 )
    
def cubeHolderArmMid():
    movecubeHolderArm( c.cubeHolderArmMid, 10 )
    
def cubeHolderArmMesa():
    movecubeHolderArm( c.cubeHolderArmMesa, 5 )
    
def cubeHolderArmParallel():
    movecubeHolderArm( c.cubeHolderArmParallel, 10 )
    
#def cubeHolderArmSlightUp():
#   movecubeHolderArm( c.cubeHolderArmSlightUp, 5)
    
def grabberArmStraightUp(speed = 10):
    movegrabberArm( c.grabberArmStraightUp, speed ) 
       
def grabberArmUp( speed ):
    movegrabberArm( c.grabberArmUp, speed )
    
def grabberArmDown():
    movegrabberArm( c.grabberArmDown, 10 )
    
def grabberArmMid():
    movegrabberArm( c.grabberArmMid,10 )
    
def grabberArmFribee():
    movegrabberArm( c.grabberArmFrisbee, 5 )
    
def grabberArmDrop():
    movegrabberArm( c.grabberArmDrop, 10 )
    
def grabberArmRelease():
    movegrabberArm( c.grabberArmRelease, 5 )
    
def grabberArmFrisbeeAproach():
    movegrabberArm( c.grabberArmFrisbeeAproach, 10 )
    
def grabberArmGrabFrisbee():
    movegrabberArm( c.grabberArmGrabFrisbee, 10 )

def frisbeeGrabberOpen():
    moveFrisbeeGrabber(c.frisbeeGrabberOpen, 10)

def frisbeeGrabberClose():
    moveFrisbeeGrabber(c.frisbeeGrabberClose, 100)
    
