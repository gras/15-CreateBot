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

