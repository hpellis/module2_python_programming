#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:52:52 2018

@author: harriet
"""

from moving_shapes import *

frame=Frame(300,300)

shape1=Square(frame, 100)

for i in range (100):
    shape1.move_tick()
    
