# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:25:57 2018

@author: 612383249
"""

from module_2_project_functions import *

score = 0
print("So, you want to know if it's time to move in together." )
name2=input("What is your name? ")
name2=name2.title()
input(f"Great. Hi {name2}. Hit enter when you're ready to answer some questions about your relationship.")
name=input("First, what is your partner's name? ")
name=name.title()
months=int(input("So, how many months have you been together? "))
friends=int(input(f"And how many of {name}'s friends have you met? "))
brunch = input("Do you brunch on the weekends? (Y or N) ")
cooking = int(input(f"On a scale from 1 to 10, how good is {name} at cooking? "))


the_length_relationship= Length(name, name2, score, months)
the_length_relationship.how_long()
score= score + the_length_relationship.score

the_friends= Friends(name,name2, score,friends)
the_friends.how_friends()
score= score + the_friends.score

the_brunch = Brunch(name,name2, score,brunch)
the_brunch.brunch_test()
score += the_brunch.score

the_cooking= Cooking(name,name2, score,cooking)
the_cooking.cooking_test()
score= score + the_cooking.score

the_move= Move_in(name,name2, score)
the_move.big_move() 


print(f"\nWe've saved a copy of this result so you can share the news with {name}.")


    
