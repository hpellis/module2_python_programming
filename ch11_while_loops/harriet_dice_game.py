# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:52:44 2018

@author: 612383249
"""

#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 10 - DICTIONARIES
#----------------------------------------------------------------------------------------------------------------------

from random import randint


def dice_game():
    print("Guess whether the sum of two dice will be even or odd.")
    guess=""
    while guess != "3":
        guess=input("1 for even, 2 for odd or 3 to exit.")
        dice_one=randint(1,6)
        dice_two=randint(1,6)
        print(dice_one + dice_two)
        if guess == "1" and (dice_one + dice_two) % 2 == 0:
            print ("Correct")
        elif guess == "2" and (dice_one + dice_two) % 2 != 0:
            print("Correct")
        else:
            print("Wrong")
    print("Game over.")
  
    
dice_game()
