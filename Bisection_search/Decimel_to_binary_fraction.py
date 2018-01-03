# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:04:45 2017

@author: Gavrilov
"""
#1) searching for power 
x = float(input("Enter a decimal number between 0 and 1: "))
p = 0 #we are looking for power #starting from 0

while ((2**p)*x)%1 != 0: #incrementing to 1.0
    print("Reminder = " + str((2**p)*x - int((2**p)*x))) #just observing process
    p += 1 #incrementing power

#2) converting to binary
num = int(x*(2**p)) #we found necessary power of 2 and multiplying it to get int 1 
result = ""
if num==0:
    result="0"

while num > 0: #loop reaching 0 for find binary representation (reminder, shift and division)
    result = str(num%2)+result
    num = num//2

#3) divide by found power, i.e. shift to right
for i in range(p-len(result)): #len is relevant here because of binary, shift of amount of p
    result = "0" + result #incrementation of numbers replacing shift

result = result[0:-p]+"."+result[-p:] #just incrementing before float point

print("The binary representation of the decimal " + str(x) + " is "+str(result)) #just printing out float and result
