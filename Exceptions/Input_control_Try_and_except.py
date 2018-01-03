# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:53:53 2017

@author: Gavrilov
"""

while True:
    try:
        n = input("Please enter an integer") #input is a string, 
        n = int(n) #so if it can't be casting to int, the ValueError occurs
        break #exit, the loop only when the correct type of input is provided
    except ValueError:
        print("Input not an int, try again")
print("Correct input of an integer!")      
