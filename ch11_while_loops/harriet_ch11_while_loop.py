
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 11 - WHILE LOOPS
#----------------------------------------------------------------------------------------------------------------------



##### while loops

# while loops repeat while a condition evaluates to true
# while {condition:}
    # do this block of code
# when no longer true return to next block of code



# TASK 1 - REPEATED DIVISION
#-----------------------------------------------------------------------------------------------------------------------

x=33
while x >= 1:
    print(x, ':', end='')
    x=x/2
print (x)


# TASK 2 - COMPUTING TRIANGULAR NUMBERS
#-----------------------------------------------------------------------------------------------------------------------

# for input integer n, return the sum of values from n down to 1

def triangular_number(n):
    tri_num_of_n = 0
    while n > 0:
        tri_num_of_n = tri_num_of_n + n
        n = n-1
    return tri_num_of_n

print(triangular_number(3))


# TASK 3 - STUDENT MARKS
#--------------------------------------------------------------------------------------------------------------------------

# create a loop to determine if student marks are a pass/fail/first
# marks: first class >= 70, pass is >= 40, fail is < 40

# while loop for student marks

#mark = 1
#while mark > 0:
#    mark = int(input("Enter student mark. "))
#    print(f"Mark is {mark}", end='')
#    if mark >= 70:
#        print("- first class.")
#    elif mark >= 40:
#        print("- pass.")
#    else:
#        print("- fail.")


# converted into a function        
  
#def convert_mark():
#    mark = 1
#    while mark > 0:
#        mark=int(input("Enter student mark. "))
#        print(f"Mark is {mark} ", end="")
#        if mark >= 70:
#            print("- first class.")
#        elif mark >=40:
#            print("- pass.")
#        else:
#            print("- fail.")
#
#convert_mark()

def convert_mark():
    mark=1
    marks_to_enter=input("Do you have marks to enter? ")
    
    while marks_to_enter == "yes" or marks_to_enter == "Yes":
        mark=int(input("Enter student mark. "))
        print(f"Mark is {mark} ", end="")
        
        if mark >= 70:
            print("- first class.")
            marks_to_enter=input("Do you have marks to enter? ")
        elif mark >=40:
            print("- pass.")
            marks_to_enter=input("Do you have marks to enter? ")
        else:
            print("- fail.")
            marks_to_enter=input("Do you have marks to enter? ")
    else:
        print("You are done entering marks.")
        

convert_mark()       
        
 
     
# exercise - input inside a while loop
#------------------------------------------------------------------------------------------------------
        
month=''

while month != "July":
    month=input("Guess which month I'm thinking of? ")
print("Correct")
    


password=''

while password != "password":
    password=input("What is the password? ")
print("Correct")



age=0

while age < 18:
    age = int(input("How old are you? Only over 18s allowed: "))
    
print("Welcome.")


# TASK 4 - USING THE BREAK STATEMENT INSIDE A LOOP
#-----------------------------------------------------------------------------------------------------------------

i=55
while i > 10:
    print(i)
    i=i*0.8
    if i == 35.2:
        break


## exercise
        
def say_hello():
    name=""
    while type(name) == str:
        name=input("What is your name? ")
        if name == "done":
            break
        else:
            print(f"Hello {name}.")

say_hello()


# TASK 5 - GUESS A NUMBER GAME
#-----------------------------------------------------------------------------------------------------------------

from random import randint

def guess_a_number(attempts, range):
    number=randint(1, range)
    print("I'm thinking of a number between 1 and 100.")
    while attempts >= 0:    
        guess=int(input("Guess my number. "))
        if guess > number:
            print(f"{guess} is too high.\nYou have {attempts} guesses left.")               
        elif guess < number:
            print(f"{guess} is too low.\nYou have {attempts} guesses left.")                
        else:                
            print(f"Success! You guessed {number}.")
            break
        attempts -= 1
    if attempts==0:
        print("You are out of guesses.")
        
    
guess_a_number(7, 100)
