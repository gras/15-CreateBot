'''
Created on Mar 17, 2015

@author: Botball
'''

import time as t

import kovan as link

import constants as c


def grabBot():
    link.motor( c.grabber, -100 )
    t.sleep( 1.000 )
    
    link.motor( c.grabber, 0 )
    t.sleep( 2.000 )
    link.motor( c.razr, 100 )
    t.sleep( 2.000 )
    link.motor( c.grabber, 100 )
    t.sleep( 4.000 )
#grabBot