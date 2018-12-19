# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:19:09 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 3 - FUNCTIONS AND IMPORTING MODULES
#----------------------------------------------------------------------------------------------------------------------


from harriet_ch03_functions import *

# TASK 1 - INPUT FROM A USER
#--------------------------------------------------------------------------------------------------

print("What is your name? ")
name=input()
print("Hello {}!".format(name))


#testing hello_world function
#------------------------------------------------------------------------------------------------------
hello_world()


#testing shopping list function
#-----------------------------------------------------------------------------------------------------

item1="bananas"
item2="apples"
item3="pears"
item4="plums"
item5="peaches"
item6="pineapple"
item7="cherries"
item8="grapes"

shopping_list1=(shopping_list(item1, item2, item3, item4))
shopping_list2=(shopping_list(item5, item6, item7, item8))


#testing hello_world_2args function
#--------------------------------------------------------------------------------------------------------------
a1="hello "
b1="world"
a2="i love "
b2="coding"
a3="but sometimes "
b3="it's hard"

hello_world_2args(a1, b1)
hello_world_2args(a2, b2)
hello_world_2args(a3, b3)



# testing add two numbers with args
#------------------------------------------------------------------------------------------------------------

add_two_numbers_from_args(10,4)


#testing add two numbers function
#-------------------------------------------------------------------------------------------------------------

add_two_numbers(10,4)


#test convert distance function
#------------------------------------------------------------------------------------------------------

convert_distance(5)
convert_distance(42)


#test temp conversion function
#---------------------------------------------------------------------------------------------------------

temperature_conversion(31)


#test second temp conversion function
#----------------------------------------------------------------------------------------------------------
temperature_conversion_2(31)


#test temp conversion and return function
#--------------------------------------------------------------------------------------------------------

f, k=temperature_conversion_return(31)

g, h=temperature_conversion_return(40)


print(f, k)
print(g, h)


#test distance convert and return function
#-----------------------------------------------------------------------------------------------------------

kilometers=convert_distance_return(3)

print (kilometers)


#test add two numbers and return function
#---------------------------------------------------------------------------------------------------------
result1=add_two_numbers_and_return(10,4)
result2=add_two_numbers_and_return(3, 2)

print(result1)
print(result2)
