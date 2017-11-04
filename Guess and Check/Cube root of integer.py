# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:22:32 2017

@author: Gavrilov
"""
cube = int(input("Enter an integer: ")) #set up a value for cube
for guess in range (abs(cube+1)): #abs because I deal with negative cases
    if guess**3 >= abs(cube): #check here, but I gone too far, simply break
        break
if guess**3 != abs(cube): #Otherwise, run loop, but now, when do check, do print
        print (cube, "is not a perfect cube")
else: #Otherwise, do the check with the second piece
    if cube < 3:
        guess =- guess
    print ("Cube root of " + str(cube) + " is " + str(guess))
