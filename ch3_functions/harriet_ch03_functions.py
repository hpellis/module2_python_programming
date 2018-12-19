# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:09 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 3 - FUNCTIONS AND IMPORTING MODULES
#----------------------------------------------------------------------------------------------------------------------



#TASK 2 - WRITE YOUR FIRST FUNCTION
#------------------------------------------------------------------------------------------------------------

def hello_world():
        print("Hello World!")
        hello_person()

        

def hello_person():
        print("What is your name?")        
        name=input()
        print("Hello " + name)
        print("Enter a number between 1 and 100.")
        num_1=input()
        print("Enter another number between 1 and 100.")
        num_2=input()
        print(int(num_1)*int(num_2))

        
# TASK 4 - ADDING TWO NUMBERS TOGETHER
#---------------------------------------------------------------------------------------------------------------
def add_two_numbers_from_args(number1, number2):
    answer= number1+number2
    print("{} + {} is {}.".format(number1, number2, answer))


# hello world with two arguments
#-----------------------------------------------------------------------------------------------------------

def hello_world_2args(a, b):
    print("{}{}".format(a,b))
    

# shopping list function
#-------------------------------------------------------------------------------------------------------------

def shopping_list(a, b, c, d):
    print("I'm going to the shops to buy {}, {}, {} and {}.".format(a,b,c,d))



#add two numbers function
#-------------------------------------------------------------------------------------------------------
def add_two_numbers(a,b):
    print(a+b)



#convert distance function
#------------------------------------------------------------------------------------------------------------

def convert_distance(miles):
    kilometers=(miles * 8.0)/5.0
    print("The distance in miles is {}.".format(miles))
    print("Converting distance in miles to kilometers:")
    print("Distance in miles: ", miles)
    print("Distance in kilometers: ", kilometers)
    

# TASK 5 - TEMPERATURE CONVERSION
#---------------------------------------------------------------------------------------------------------------------

def temperature_conversion(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    print("{} degrees centigrade is equal to {} degrees fahrenheit and {} degrees kelvin.".format(centigrade, fahrenheit, kelvin))
    


#alternative temperature function
#-------------------------------------------------------------------------------------------------------------------------
def temperature_conversion_2(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    print(str(centigrade)+" degrees centigrade is equal to " + str(fahrenheit) + " degrees fahrenheit and "+ str(kelvin) +" degrees kelvin.")
    

#temperature conversion function with return instead of print
#----------------------------------------------------------------------------------------------------------------------
def temperature_conversion_return(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    return(fahrenheit, kelvin)
    

#return distance conversion result
#---------------------------------------------------------------------------------------------------------------------

def convert_distance_return(miles):
    kilometers=(miles * 8.0)/5.0
    return(kilometers)
   


# TASK 6 - ADD TWO NUMBERS AND RETURN FUNCTION
#----------------------------------------------------------------------------------------------------------------
def add_two_numbers_and_return(a,b):
    return(a+b)










