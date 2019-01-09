#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:25:54 2018

@author: harriet
"""

from shape import *
from pylab import random as r


class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape=shape
        self.diameter=diameter
        
        self.figure=Shape(shape, diameter)
        
        self.minx = self.diameter/2
        self.miny = self.diameter/2
        
        self.maxx = frame.width-(self.diameter/2)
        self.maxy = frame.height-(self.diameter/2)
        
        self.x = self.minx + (r()* (self.maxx - self.minx))
        self.y = self.miny + (r()* (self.maxy - self.miny))
            
        self.goto(self.x, self.y)
        self.initial_move()

        
    def initial_move(self):
        self.dx = 5+10 * r()
        self.dy = 5+10 * r()       
 
# randomly change the direction
        if r() < 0.5:
            self.dx = self.dx * -1
            self.dy = self.dy * -1
            
        else:
            self.dx = self.dx
            self.dy = self.dy
            
        self.figure.goto(self.x,self.y)


    def goto(self, x, y,):
        self.figure.goto(x,y)


    def move_tick(self):
  
# set the new values for x and y
        self.x+=self.dx
        self.y+=self.dy


# check that new coordinates are in the frame        
        if self.x < self.minx:
            self.dx = self.dx * -1
            self.x = self.minx
        
        elif self.x > self.maxx:
            self.dx = self.dx * -1
            self.x = self.maxx
        
        if self.y < self.miny:
            self.dy = self.dy * -1
            self.y = self.miny
        
        elif self.y > self.maxy:
            self.dy = self.dy * -1
            self.y = self.maxy
            
        self.x+=self.dx
        self.y+=self.dy
        
        self.goto(self.x, self.y)

        
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)


class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)


class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        
        self.minx = self.diameter
        self.miny = self.diameter
        
        self.maxx = frame.width-self.diameter
        self.maxy = frame.height-self.diameter