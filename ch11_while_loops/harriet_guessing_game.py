# -*- coding: utf-8 -*-'
"""
Created on Tue Dec 18 11:32:38 2018

@author: 612383249
"""

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