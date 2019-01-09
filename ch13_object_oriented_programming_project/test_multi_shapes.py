#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:14:43 2018

@author: harriet
"""

from moving_shapes import *

# this file attempts to animate several shapes at the same time
# the number of each type of shape is determined by the variable numshapes
# these instances are stored in a list called shapes
# when the second animation loop of the code runs, there is an embedded loop
# this loop calls the move_tick method on each shape object


frame=Frame(400,400)
numshapes=3
shapes=[]

size=60

for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
    
for i in range(300):
    for shape in shapes:
        shape.move_tick()
        
frame.close()        