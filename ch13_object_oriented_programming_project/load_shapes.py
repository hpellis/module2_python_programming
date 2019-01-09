#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:47:12 2018

@author: harriet
"""

from shape import *

frame = Frame (300,300)

s1= Shape ('square', 100)
s1.goto(200,100)

s2= Shape ('circle', 100)
s2.goto(300,200)


x=0
y=0

for i in range(100):
    s1.goto(x,y)
    x=x+1
    y=y+1
    

    