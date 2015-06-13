'''
Created on Mar 17, 2015

@author: Botball
'''

import time as t
import kovan as link
#import constants as c

def noStop( rightSpeed, leftSpeed, driveTime ):
    # this method does not stop
    # to allow smooth transitions to the next drive command
    link.create_drive_direct( -1 * rightSpeed, -1 * leftSpeed )
    t.sleep( driveTime )


def withStop( rightSpeed, leftSpeed, driveTime ):
    link.create_drive_direct( -1 * rightSpeed, -1 * leftSpeed )
    t.sleep( driveTime )
    #link.ao()
    link.create_drive_direct( 0, 0 )
    
def turnCW90():
    link.create_write_byte( 152 )
    link.create_write_byte(8)
    link.create_write_byte(137)
    link.create_write_byte(0)
    link.create_write_byte(250)
    link.create_write_byte(255)
    link.create_write_byte(255)
    link.create_write_byte(157)
    link.create_write_byte(255)
    link.create_write_byte(168) #rotates -88 degrees CCW