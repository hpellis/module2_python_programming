# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:29:39 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 3 - FUNCTIONS AND IMPORTING MODULES
#----------------------------------------------------------------------------------------------------------------------

# practice user input and formatting

print("What is your name?")
name=input()
print("Hello {}!".format(name.title()))

print("How old are you?")
age=input()
print("Your name is {} and you are {} years old.".format(name, age))

print("How tall are you?")
height=input()
print("Your name is {} and you are {} years old and {} tall.".format(name, age, height))

print ("Where do you live?")
location=input()
print("Hello {}! You are {} years old, {} tall and you live in {}.".format(name, age, height, location.title()))


print("Hmmm what do you like to eat?")
fav_food=input()


print("Hello {}! You are {} years old, {} tall and you live in {}. I also heard you are a fan of {}.".format(name.title(), age, height, location.title(), fav_food))


