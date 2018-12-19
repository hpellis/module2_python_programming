# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:13:39 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 4 - CONDITIONALS
#----------------------------------------------------------------------------------------------------------------------


# EXERCISES WITH TIME
#------------------------------------------------------------------------------------------------------
import random
import datetime
import time

def luckyNumberRandom():
    name = input('please type your name here: ')
    print ("hello " + name.upper() )
    number = int(input('please give a number '))
    
    print ('your lucky number is: '+ str(random.randint(1,number)))

startTime = time.time()
print('date and time', datetime.datetime.now())
print()
print('current time' , datetime.datetime.now().time())
luckyNumberRandom()
processTime = time.time()-startTime
print()
print('program running time:', round(processTime,2),'second')



# TASK 3 & TASK 4 - USING IF AND ELSE STATEMENTS
#--------------------------------------------------------------------------------------------------

number=input("Enter a number between 1 and 10: ")
number=int(number)

if number>10:
    print("Too high!")
        
elif number<=0:
    print("Too low!")

else:
    print("Thanks.")    
    

    
# TASK 5 - USING ELIF STATEMENTS
#--------------------------------------------------------------------------------------------------

age=input("What is your age? ")
age=int(age)
    
if age <13:
    print('child')
    
elif age <18:
    print('teen')
    
elif age <65:
    print('adult')
    
else:
    print('pensioner')
