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
    move.initMoves()
    
    if c.isPrime:
        print "Running Prime"
    else:
        print "Running Clone"
        
    #################################
    # link.enable_servos()          #    TEST
    # move.grabberArmStraightUp(10) #    CODE
    #################################

    print "Press the A button to start or the B button to exit"
    while not link.a_button() and not link.b_button():
        pass
    if link.b_button_clicked():
        DEBUG("exited")
    print "Starting run..."    
    link.wait_for_light(0) 
    
    c.stoptime= link.seconds()
    #link.shut_down_in(119.0)
    move.gripCubes()
    link.enable_servos()  
    
    # ends at mesa facing north
def driveToMesa():
    print "driveToMesa"
    move.cubeHolderArmSlightBack()
    drive.noStop( 200, 200, 1.0 ) #100,100,2.00
    if c.isPrime:
        drive.withStop( 200, 200, 3.4) #was 3.3
    else:
        drive.withStop(200, 200, 3.5)
    drive.noStop(-50, -50, 0)
    while ( link.analog_et(c.ETport) > 350):
        pass
    print link.analog_et(c.ETport)
    if c.isPrime:
        drive.withStop(-75, -75, 0.50) 
    else:
        drive.withStop(-50, -50, 0.45) #.65
        

# turns to the right so that the cubeHolderArm can sweep the mesa
# at west wall facing east
def turnToMesa():
    print "turnToMesa"
    
    if c.isPrime:
        drive.withStop( -250, 250, 0.7550 ) #was -250, 250, 0.550 #correct code
    else:
        drive.withStop( -250, 250, 0.755 ) #was 0.750
    move.grabberArmDown()
    '''
    drive.spinCW90() #download and execute the scripted turn
    '''
        
def waitForLego(x):
    print "waitForLego"
    t.sleep(x)

# sweeps part of the mesa. drives to the pod or botgal
# Facing east
def driveToBlock():
    print "driveToBlock"
    move.cubeHolderArmBackMesa()
    if c.isPrime:
        drive.withStop( 100, 100, 1.5 )
    else:    
        drive.withStop( 100, 100, 1.6)

# grabs BotGal and brings her down to the table (off the mesa)
def grabBot():
    print "grabBot"
    move.grabberOpen()#opening grabber
    
    #using grabberArm as a move
    move.grabberArmUp( 10 )
    t.sleep( .5 )
    move.grabberClose()
    t.sleep(0.500 )
    
    # using grabberArm as a move
    move.grabberArmDrop()
    link.disable_servo( c.grabberArm)
    t.sleep(1.00)
    
# sweeps more of the mesa and stops to back up in order to change cubeHolderArm position
# at west wall facing east
def driveAndReset():
    print "driveAndReset"
    drive.withStop( 100, 100, 3.450 ) #was 102,100
    drive.withStop( -100, -100, 0.50 )#was .250
    move.cubeHolderArmUp(20)
    drive.withStop( -250, -250, 2.00)# was -100,-100,6.4
    

# sweeps the mesa all the way to the bin and pushes the cubes and poms into the bin. Faces east
def endDrive():
    print "endDrive"
    move.cubeHolderArmMesa()
    #t.sleep( 1.00 )
    if c.isPrime:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        move.opencubeHolder( 1 ) # was .7  #dump blocks
        move.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        move.cubeHolderArmMesa()
        #t.sleep( 1.00 )
        drive.withStop( 100, 100, 5.300 )  #was 100,100
    else:
        drive.withStop( 102, 100, 6.500 ) #was 100,100
        move.opencubeHolder( 1 ) #dump blocks
        move.cubeHolderArmMid()
        drive.withStop( -200, -200, 2.600 ) #was 2.900
        move.cubeHolderArmMesa()
        #t.sleep( 1.00 )
        drive.withStop( 103, 100, 5.300 )  #was 100,100 
    
    
    # depends on which sub method was run
def checkColor():
    print "checkColor"
    green = s.lookForGreen()
    print green
    return green    
            
def backAwayFromBin():
    print "back Away From Bin"
    link.set_servo_position(c.grabberArm, c.grabberArmRelease)
    link.enable_servo(c.grabberArm) 
    move.cubeHolderArmMid(20)
    drive.withStop(-100, -100, 3.250)
    
    
    # ends at south wall
'''def dumpPod():
    print "dump pod"
    drive.withStop(-100, -100, 1.)
    drive.withStop(-50, 50, 4.00)
    if c.isPrime:
        drive.withStop( 100, 100, 4.25 )
    else:    
        drive.withStop( 100, 100, 4.0)
    drive.withStop(50, -50, 4.00)#was 50, -50, 4.00
    move.grabberArmDown(20)
    move.grabberOpen()
    t.sleep (1.000)
    move.grabberArmClear()'''
    
def dumpPod():
    print "dump pod"
    move.grabberArmDown(20)
    move.grabberOpen()
    t.sleep (1.000)
    move.grabberArmRelease()
    drive.withStop(-100, 100, 2.20)
    
    

'''def podToFrisbee():
    drive.withStop(-50, 150, 2.00)
    t.sleep( 0.50 )
    move.cubeHolderArmParallel()
    move.grabberArmRelease()
    if c.isPrime:
        drive.withStop(-200, -200, 6.75 )
    else:
        drive.withStop(-200, -200, 6.50)
    move.grabberArmStraightUp()
    drive.withStop(-50, 150, 2.00)
    drive.withStop(200, 200, 1.90)#1.8'''
    
def podToFrisbee():
    move.cubeHolderArmParallel()
    move.grabberArmRelease()
    if c.isPrime:
        drive.withStop(-200, -200, 4.25 )
    else:
        drive.withStop(-200, -200, 4.00)
    move.grabberArmStraightUp()
    move.cubeHolderArmUp(10)
    drive.withStop(-50, 150, 1.90)
    t.sleep(3.00)
    
    #drive.withStop(200, 200, 1.90)#1.8
        
def moveToEastWall():
    move.cubeHolderArmParallel()
    drive.withStop(-200, -200, 3.5)
    drive.withStop( -250, 250, 0.70 ) #was 0.65
    
   
    # goes to north wall
def dumpBotgal():
    print "dump botgal"
    #drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    move.cubeHolderArmParallel()
    drive.withStop(-400, -400, 2.10)#was 4.0
    drive.withStop(-100, 100, 1.75)#1.5
    drive.noStop(0,0,0)
    move.grabberOpen()
    t.sleep (1.000)
    
    
def botgalToFrisbee():
    print("botgaltofrisbee")
    link.enable_servo(c.grabberArm)
    move.grabberArmStraightUp()
    drive.withStop(200, 200, 2.4)
    #t.sleep(27.00)
    
def parkInSafePlace():
    print "i see nothing,"
    drive.withStop(100, 100, 1.0)
    drive.withStop(-50, 50, 4.00)
    t.sleep(5.00)
    move.cubeHolderArmParallel()
    
# backwards 90 degree arc    
def deliverFrisbeeToStartBox():
    drive.withStop(300, 0, 1.2)
    move.grabberArmHover()
    drive.withStop(200, 200, 0.85)#100,100,2
    drive.withStop( 250, -250, 0.755 )#drive.withStop(300, -300, .625)
    drive.noStop(400, 400, 2.25)#100,100,9
    drive.withStop( 250, -250, 0.755 )#drive.withStop(300, -300, .6)
    move.frisbeeGrabberOpen()
    
def grabFrisbee():
    link.enable_servo(c.grabber)
    link.enable_servo(c.frisbeeGrabber)
    #t.sleep(1.00)
    move.grabberOpen()
    #t.sleep(1.00)
    move.frisbeeGrabberOpen()
    #t.sleep(1.00)
    move.grabberArmGrabFrisbee( 40 )
    t.sleep(1.00)
    move.grabberArmFinal(10)
    t.sleep(1.00)
    move.grabberMidClose()
    t.sleep(1.00)
    move.frisbeeGrabberClose()
    t.sleep(1.00)
    move.grabberSlowOpen()
    #t.sleep(1.00)
    move.grabberArmBack(5)
    #t.sleep(1.00)
    
def deliverFrisbeeToNorthEndZone():
    drive.withStop(200, 200, 2.00)
    drive.withStop( 250, -250, 0.755 )
    drive.withStop(200, 200, 1.8)
    move.grabberArmDown()
    move.frisbeeGrabberOpen() 
    
def moveToFrisbee():
    #t.sleep(2)        
    drive.noStop(-100, -100, 0)
    while ( link.analog_et(c.ETport) < 425):
        pass
    print link.analog_et(c.ETport)
    drive.withStop(0, 0, 0)    
    
def frisbeeToBotgal():
    drive.withStop(200, 100, 4.00)
    move.grabberArmDown()
    move.frisbeeGrabberOpen()
    link.create_disconnect()
       
def grabCubes():
    move.cubeHolderArmUp()
    move.grabberArmDrop()
    move.grabberOpen()
    drive.withStop(100, 100, 4)
    drive.withStop(-100, 100, 2.00)
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
    link.ao()
    shutDown()
    exit()

