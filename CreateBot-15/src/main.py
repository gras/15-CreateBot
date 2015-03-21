'''
Created on Mar 17, 2015

@author: Botball
'''

import kovan as link

import actions as act
import motor as m


def main():
    act.init()
    
    act.getOutOfStartBox()
    act.turnToMesa()
    act.driveToBlock()
    m.grabBot()
    act.driveAndReset()
    act.endDrive()
    
    link.create_disconnect()
#main

if __name__ == "__main__":
    main()
#if
