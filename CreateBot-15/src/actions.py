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
    
       
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"
    
    print "Connecting To Create..."
    link.create_connect()
    link.camera_open() 
    
    #insert wait_for_light here
    # preset servo positions
    servo.initServos()
    print "Press the A button to start"
    while not link.a_button():
        pass
    print "Starting run..."    


def driveToMesa():
    print "driveToMesa"
    servo.cubeHolderArmSlightBack()
    drive.noStop( 100, 100, 2.0 )
    drive.withStop( 200, 200, 3.5) #was 3.3
    drive.noStop(-50, -50, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
        #print analog_et(5)
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
#    link.disable_servo(c.grabberArm)
    link.disable_servo(c.cubeHolderArm)
    t.sleep(x)
#    link.enable_servo(c.grabberArm)
    link.enable_servo(c.cubeHolderArm)

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
    t.sleep( 1.000 )
    
    # reverting grabberArm to a motor
    '''link.motor(c.grabberArm, -100)
    t.sleep(1.0)
    link.motor(c.grabberArm, 0)
    t.sleep(1.0)
    '''
    #using grabberArm as a servo
    servo.grabberArmUp()
    t.sleep( 1.000 )
    
    servo.closeGrabber()
    t.sleep(1.000 )
    
    # using grabberArm as a servo
    #servo.movegrabberArm( c.grabberArmMid, 2000)
    #t.sleep( 1.000)
    servo.grabberArmDrop()
    link.disable_servo( c.grabberArm)
    
    #using grabberArm as a motor    
    '''link.motor( c.grabberArm, 100 )
    t.sleep(2.5)
    link.motor( c.grabberArm, 0 )
    '''
    '''
def checkForBotGalOrPod(): 
    return s.cameraTrack()
     '''
    
# sweeps more of the mesa and stops to back up in order to change cubeHolderArm position
def driveAndReset():
    print "driveAndReset"
    drive.withStop( 100, 100, 3.450 ) #was 102,100
    drive.withStop( -100, -100, 0.250 )
    servo.cubeHolderArmUp()
    drive.withStop( -100, -100, 6.400)

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin
def endDrive():
    print "endDrive"
    servo.cubeHolderArmMesa()
    t.sleep( 1.500 )
    if c.isPrime:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        servo.opencubeHolder() #dump blocks
        t.sleep(1.0)
        servo.cubeHolderArmMid()
        drive.withStop( -100, -100, 5.200 ) #was 2.900
        servo.cubeHolderArmMesa()
        t.sleep( 1.500 )
        drive.withStop( 100, 100, 5.300 )  #was 100,100
    else:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        servo.opencubeHolder() #dump blocks
        t.sleep(1.0)
        servo.cubeHolderArmMid()
        drive.withStop( -100, -100, 5.200 ) #was 2.900
        servo.cubeHolderArmMesa()
        t.sleep( 1.500 )
        drive.withStop( 103, 100, 5.300 )  #was 100,100
          
          
    
    
def checkColorAndDrive():
    print "checkColorAndDrive"
    check = s.checkForBotGalOrPod()
    print check
    #deliverBotgalOrPod()
    if check == c.seeGreen:
        print "dump pod"
        dumpPod()
    elif check == c.seeRed:
        print "dump botgal"
        dumpBotgal()
    else:
        print "i see nothing,"
    
   
'''
def deliverBotgalOrPod():
    print "deliverBotgalOrPod"
    servo.movecubeHolderArm(850, 10)
    drive.withStop(-100, -100, 2.500)
    drive.withStop(-50, 50, 4.00)
    servo.movecubeHolderArm(c.cubeHolderArmDown, 5 )
    '''
def dumpPod():
    #drive.withStop(100, 100, 6.0)
    servo.cubeHolderArmMid()
    drive.withStop(-100, -100, 2.500)
    drive.withStop(-50, 50, 4.00)
    servo.cubeHolderArmDown()
    t.sleep(10) #wait for lego
    if c.isPrime:
        drive.withStop( 100, 100, 7.0 )
    else:    
        drive.withStop( 100, 100, 6.0)
    servo.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def dumpBotgal():
    servo.cubeHolderArmMid()
    drive.withStop(-100, -100, 4.50)# 2.500
    drive.withStop(-50, 50, 4.00)
    servo.cubeHolderArmDown()
    #drive.noStop(-300,-300,0)
    drive.withStop(-200, -200, 4.5)#was 4.0
    #while not link.get_create_rbump() and not link.get_create_lbump():
    #    pass
    drive.withStop(-100, 100, 1.75)#1.5
    drive.noStop(0,0,0)
    servo.moveGrabber(c.grabberOpen, 10)
    t.sleep (1.000)
    
def shutDown():
    link.create_disconnect()
    

def DEBUG( msg = "DEBUG" ):
    print msg
    link.ao()
    exit()

