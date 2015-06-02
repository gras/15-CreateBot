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

# sets up the cubeHolder and cubeHolderArm
def init():
    # flush print output, don't worry about this
    sys.stdout = os.fdopen( sys.stdout.fileno(), 'w', 0 )
    
    print "Running My Create" 
    print "Power on the Create Lauren..."
    link.create_connect()
    link.create_full()
    link.camera_open() 
    # preset servo positions
    servo.initServos()
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"
        
    '''
    print "Press the A button to start or the B button to exit"
    while not link.a_button() and not link.b_button():
        pass
    if link.b_button_clicked():
        DEBUG("exited")
    print "Starting run..."    
    link.wait_for_light(0) 
    '''
    c.stoptime= link.seconds()
    link.shut_down_in(119.0)
    link.enable_servo(c.grabber)
    link.enable_servo(c.grabberArm)
    link.enable_servo(c.cubeHolderArm)
    

def driveToMesa():
    print "driveToMesa"
    servo.cubeHolderArmSlightBack()
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
        drive.withStop( -250, 250, 0.745 ) #was 0.770
    else:
        drive.withStop( -250, 250, 0.750 ) #was 0.725
        
def waitForLego(x):
    print "waitForLego"
    t.sleep(x)

# sweeps part of the mesa. drives to the pod or botgal
def driveToBlock():
    print "driveToBlock"
    servo.cubeHolderArmBackMesa()
    if c.isPrime:
        drive.withStop( 100, 100, 1.800 )
    else:    
        drive.withStop( 100, 100, 2.1)

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    print "grabBot"
    servo.openGrabber()#opening grabber
    t.sleep( 0.500 )
    
    #using grabberArm as a servo
    servo.grabberArmUp()
    t.sleep( 1.000 )
    
    servo.closeGrabber()
    t.sleep(0.500 )
    
    # using grabberArm as a servo
    servo.grabberArmDrop()
    link.disable_servo( c.grabberArm)
     
# sweeps more of the mesa and stops to back up in order to change cubeHolderArm position
def driveAndReset():
    print "driveAndReset"
    drive.withStop( 100, 100, 3.450 ) #was 102,100
    drive.withStop( -100, -100, 0.250 )
    servo.cubeHolderArmUp()
    drive.withStop( -250, -250, 2.00)# was -100,-100,6.4

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    print "endDrive"
    servo.cubeHolderArmMesa()
    t.sleep( 1.00 )
    if c.isPrime:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        servo.opencubeHolder() #dump blocks
        t.sleep(1.0)
        servo.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        servo.cubeHolderArmMesa()
        t.sleep( 1.00 )
        drive.withStop( 100, 100, 5.300 )  #was 100,100
    else:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        servo.opencubeHolder() #dump blocks
        t.sleep(1.0)
        servo.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        servo.cubeHolderArmMesa()
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
    servo.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.0)
    t.sleep(5.00)#wait for lego
    drive.withStop(-50, 50, 4.00)
    servo.cubeHolderArmParallel()
    if c.isPrime:
        drive.withStop( 100, 100, 4.5 )
    else:    
        drive.withStop( 100, 100, 4.0)
    drive.withStop(50, -50, 4.00)
    link.enable_servo(c.grabber)
    servo.moveGrabber(c.grabberOpen, 20)
    t.sleep (2.000)
    print "enable grabber"
    """
    link.enable_servo(c.grabberArm)
    servo.grabberArmRelease()
    t.sleep(2.00)
    """
    
def dumpBotgal():
    servo.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)# 2.500
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.00)
    t.sleep(5.00)
    drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    servo.cubeHolderArmParallel()
    drive.withStop(-200, -200, 4.5)#was 4.0
    drive.withStop(-100, 100, 1.75)#1.5
    drive.noStop(0,0,0)
    servo.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def parkInSafePlace():
    servo.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.00)# 2.500
    t.sleep(15)#wait for lego
    drive.withStop(-100, -100, 1.00)
    t.sleep(5.00)
    drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    t.sleep(5.00)
    servo.cubeHolderArmParallel()

def newCubeTest():
    servo.cubeHolderArmUp()
    servo.opencubeHolderWide() 
    drive.withStop(100, 100, 4.00)
    servo.cubeHolderArmCompleteDown()
    t.sleep(1.00)
    '''drive.withStop(100, 100, 3.00)
    t.sleep(1.00)
    servo.cubeHolderArmCompleteDown()
    t.sleep(.50)'''
    servo.closecubeHolder()
    t.sleep(1.00)
    servo.cubeHolderArmUp()
    '''drive.withStop(50, 50, 1.50)'''
    
def grabCubes():
    servo.cubeHolderArmUp()
    servo.grabberArmDrop()
    servo.openGrabber()
    drive.withStop(100, 100, 4)
    drive.withStop(-100, 100, 2.00)
    '''servo.movegrabberArm(2000, 5)'''
    drive.withStop(100, 100, 2.5)
    servo.grabberArmDown()
    t.sleep(2)
    link.set_servo_position( c.grabber, 400)
    '''servo.closeGrabber()''' 
    t.sleep(2)
    servo.grabberArmDrop()
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
    link.ao()
    exit()

