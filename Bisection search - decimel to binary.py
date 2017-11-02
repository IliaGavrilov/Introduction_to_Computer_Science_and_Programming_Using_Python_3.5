# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:28:01 2017

@author: Gavrilov
"""
num = int(input("Enter an int: ")) #known number

result = "" #make simple string variable for code works

if num < 0: #way out to work with negative 
    isNeg = True #set up a variable to final condition
    num = abs(num) #make it really nice to work with
else:
    isNeg = False 

if num == 0:
    result = "0" #just print out result

while num > 0: #converting decimel in binary loop
    result = str(num % 2) + result #+result here just grabbing reminder
    num = num // 2 #second step of converting decimel

if isNeg: #final cheking of a negative
    result = "-" + result
print("Result is " + str(result))      