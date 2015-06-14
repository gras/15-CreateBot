'''
Created on Mar 17, 2015

@author: Botball
'''

import os
import sys
import time as t

import kovan as link

import constants as c
import movement as move
import drive
import sensor as s
#from kovan import create_spin_CW
# from time import sleep

# sets up the cubeHolder and cubeHolderArm
def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running My Create" 
    print "Power on the Create Lauren..."
    link.create_connect()
    link.create_full()
    link.camera_open() 
    # preset move positions
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"
    move.initMoves()
    
    print "Press the A button to start or the B button to exit"
    while not link.a_button() and not link.b_button():
        pass
    if link.b_button_clicked():
        DEBUG("exited")
    print "Starting run..."    
    #link.wait_for_light(0) 
    
    c.stoptime= link.seconds()
    #link.shut_down_in(119.0)
    move.gripCubes()
    link.enable_servos()  
    
def driveToMesa():
    print "driveToMesa"
    move.cubeHolderArmSlightBack()
    drive.noStop( 100, 100, 2.0 )
    drive.withStop( 200, 200, 3.5) #was 3.3
    drive.noStop(-50, -50, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
    print link.analog_et(c.ETport)
    if c.isPrime:
        drive.withStop(-75, -75, 0.65) #was 1.0 then 0.60
    else:
        drive.withStop(-50, -50, 0.45) #.65
        

# turns to the right so that the cubeHolderArm can sweep the mesa
def turnToMesa():
    print "turnToMesa"
    
    if c.isPrime:
        drive.withStop( -300, 300, 0.600 ) #was -250, 250, 0.550 #correct code
    else:
        drive.withStop( -250, 250, 0.755 ) #was 0.750
    '''
    drive.spinCW90() #download the scripted turn
    '''
        
def waitForLego(x):
    print "waitForLego"
    t.sleep(x)

# sweeps part of the mesa. drives to the pod or botgal
def driveToBlock():
    print "driveToBlock"
    move.cubeHolderArmBackMesa()
    if c.isPrime:
        drive.withStop( 100, 100, 1.800 )
    else:    
        drive.withStop( 100, 100, 2)

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    print "grabBot"
    move.openGrabber()#opening grabber
    #t.sleep( 0.500 )
    
    #using grabberArm as a move
    move.grabberArmUp( 10 )
    t.sleep( .500 )
    
    move.closeGrabber()
    t.sleep(0.500 )
    
    # using grabberArm as a move
    move.grabberArmDrop()
    link.disable_servo( c.grabberArm)
     
# sweeps more of the mesa and stops to back up in order to change cubeHolderArm position
def driveAndReset():
    print "driveAndReset"
    drive.withStop( 100, 100, 3.450 ) #was 102,100
    drive.withStop( -100, -100, 0.250 )
    move.cubeHolderArmUp()
    drive.withStop( -250, -250, 2.00)# was -100,-100,6.4

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    print "endDrive"
    move.cubeHolderArmMesa()
    t.sleep( 1.00 )
    if c.isPrime:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        move.opencubeHolder( 1 ) # was .7  #dump blocks
        t.sleep(1.0)
        move.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        move.cubeHolderArmMesa()
        t.sleep( 1.00 )
        drive.withStop( 100, 100, 5.300 )  #was 100,100
    else:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        move.opencubeHolder() #dump blocks
        t.sleep(1.0)
        move.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        move.cubeHolderArmMesa()
        t.sleep( 1.00 )
        drive.withStop( 103, 100, 5.300 )  #was 100,100 
    
    
def checkColorAndDrive():
    print "checkColorAndDrive"
    check = s.checkForBotGalOrPod()
    print check
    if check == c.seeGreen:
        print "dump pod"
        dumpPod()
    elif check == c.seeRed:
        print "dump botgal"
        dumpBotgal()
    else:
        print "i see nothing,"
        parkInSafePlace()

def dumpPod():
    #drive.withStop(100, 100, 6.0)
    move.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.0)
    t.sleep(5.00)#wait for lego
    drive.withStop(-50, 50, 4.00)
    move.cubeHolderArmParallel()
    if c.isPrime:
        drive.withStop( 100, 100, 4.5 )
    else:    
        drive.withStop( 100, 100, 4.0)
    drive.withStop(50, -50, 4.00)
    link.enable_servo(c.grabber)
    move.moveGrabber(c.grabberOpen, 20)
    t.sleep (2.000)
    print "enable grabber"
    """
    link.enable_servo(c.grabberArm)
    move.grabberArmRelease()
    t.sleep(2.00)
    """
    
def dumpBotgal():
    move.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)# 2.500
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.00)
    t.sleep(5.00)
    drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    move.cubeHolderArmParallel()
    drive.withStop(-200, -200, 4.5)#was 4.0
    drive.withStop(-100, 100, 1.75)#1.5
    drive.noStop(0,0,0)
    move.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def parkInSafePlace():
    move.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)# 2.500
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.00)
    t.sleep(5.00)
    drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    t.sleep(5.00)
    move.cubeHolderArmParallel()

'''
def newCubeTest():
    move.cubeHolderArmUp()
    move.opencubeHolderWide() 
    drive.withStop(100, 100, 4.00)
    move.cubeHolderArmCompleteDown()
    t.sleep(1.00)
    
    drive.withStop(100, 100, 3.00)
    t.sleep(1.00)
    move.cubeHolderArmCompleteDown()
    t.sleep(.50)
    
    move.closecubeHolder()
    t.sleep(1.00)
    move.cubeHolderArmUp()
    
    drive.withStop(50, 50, 1.50)
'''

def podToFrisbee():
    drive.withStop(-50, 150, 2.00)
    t.sleep( 0.50 )
    move.cubeHolderArmParallel()
    drive.withStop(-200, -200, 7.00 )
    #drive.withStop( 0, 150, 2.50)
    move.grabberArmStraightUp()
    drive.withStop(-50, 150, 2.00)
    drive.withStop(200, 200, 1.50)
    drive.withStop(-200, -200, 3.5)
    #DEBUG("msg")
    drive.withStop( -250, 250, 0.72 ) #was 0.750
    
    
    
    
def grabFrisbee():
    link.enable_servo(1)
    link.enable_servo(2)
    #move.grabberArmMid()
    t.sleep(1.00)
    move.openGrabber()
    t.sleep(1.00)
    move.frisbeeGrabberOpen()
    t.sleep(1.00)
    move.grabberArmMid()
    t.sleep(2.00)
    move.midCloseGrabber()
    t.sleep(1.00)
    move.frisbeeGrabberClose()
    t.sleep(1.00)
    move.SlowOpenGrabber()
    t.sleep(1.00)
    move.grabberArmStraightUp()
    t.sleep(2.00)
    
    

def moveToFrisbee():
    '''link.create_connect()
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"

    link.set_servo_position( c.grabberArm, c.grabberArmFrisbeeAproach)
    link.enable_servo(c.grabberArm)
    '''
    #move.movegrabberArm(c.grabberArmStraightUp, 10) 
    t.sleep(2)
        
    drive.noStop(-100, -100, 0)
    while ( link.analog_et(c.ETport) < 425):
        pass
    print link.analog_et(c.ETport)
    drive.withStop(25, 50, 0.20)
    '''
    drive.noStop(100, 100, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
    print link.analog_et(c.ETport)
    drive.withStop(-50, -50, 0.45)
    '''
    
    
def frisbeeToBotgal():
    drive.withStop(200, 100, 4.00)
    move.grabberArmDown()
    move.frisbeeGrabberOpen()
    link.create_disconnect()
    
    
    
def grabCubes():
    move.cubeHolderArmUp()
    move.grabberArmDrop()
    move.openGrabber()
    drive.withStop(100, 100, 4)
    drive.withStop(-100, 100, 2.00)
    '''move.movegrabberArm(2000, 5)'''
    drive.withStop(100, 100, 2.5)
    move.grabberArmDown()
    t.sleep(2)
    link.set_servo_position( c.grabber, 400)
    '''move.closeGrabber()''' 
    t.sleep(2)
    move.grabberArmDrop()
    drive.withStop(50, 50, 1.5)

    
def shutDown():
    link.create_disconnect()
    print "elapsed time"
    print link.seconds()- c.stoptime

def kill():
    from subprocess import call
    call(["killall","python"])    

def DEBUG( msg = "DEBUG" ):
    print msg
    link.create_disconnect()
    link.ao()
    exit()

