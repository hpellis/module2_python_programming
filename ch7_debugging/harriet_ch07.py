# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:40:16 2018

@author: 612383249
"""
#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 7 - DEBUGGING
#----------------------------------------------------------------------------------------------------------------------


# using the print function for debugging
#---------------------------------------------------------------------------------------------------------
# to debug, print out the data type

#userInput= input("Please give a number ")
#result = userInput-2

#print(type(userInput))

#result2=int(userInput)-2

#print(result2)


# how to use spyder's debugging tool
#----------------------------------------------------------------------------------------------------------

# doubleclick next to the line number to add a debugging point
# then use the blue icons to move through the code
# the first button runs the code until the first breakpoint
# the second button runs the code line by line
# the third buttons steps into the next function
# the fourth button runs until the return of the current function
# the fifth button runs until the next breakpoint
# the stop button exits debugging mode


###### example


userInput=input("Please give a number: ")

def simpleOperation(userInput):
    intInput=int(userInput)
    result=intInput-2
    return result

def nestedOperation(result):
    result=simpleOperation(userInput)
    result2= result * 2
    return result2
    
result = simpleOperation(userInput)

result2= nestedOperation(result)
print(result2)
