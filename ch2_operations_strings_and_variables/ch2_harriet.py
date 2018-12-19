# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:35:30 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 2 - OPERATIONS, STRINGS AND VARIABLES
#----------------------------------------------------------------------------------------------------------------------


# TASK 1 - SIMPLE OPERATIONS
#---------------------------------------------------------------------------------------

A=5-6
B=8*9
C=6/2
D=5/2
E=5.0/2
F=5%2
G=2*(10+3)
H=2**4

print(A, B, C, D, E, F, G, H)


# TASK 2 - PRACTICING WITH VARIABLES
#---------------------------------------------------------------------------------------------------

age=5
age="almost three"

type("almost eight")


# TASK 3 - BASIC STRING MANIPULATION
#-------------------------------------------------------------------------------------------------------

print("Bob"*3)
#print("Bob"+3)
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())


# TASK 4 - STRING 
#--------------------------------------------------------------------------------------------------------

age=5
like="painting"

age_description="My age is {} and I like {}".format(age, like)
print(age_description)

age_description2="My age is {0} and I like {1}".format(age, like)
print(age_description2)


print(10/3)
print(10%3)

a=1
a=a+1
print(a)
b="hello"
print(b)
c=b.title()
print(b)
print(c)
d="hello"
e=d.title()
print(d)
print(e)
name="Dave"
f="Hello {}! ".format(name)
print(f)
name="Sarah"
print(f)
print(f*5)
