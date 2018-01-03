# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:24:10 2017

@author: Gavrilov
"""

def printName (firstName, lastName, reverse):
    if reverse:
        print(lastName+", "+firstName)
    else:
        print(firstName, lastName)
printName('Eric', 'Grimson', True)
printName('Eric', 'Grimson', reverse = False) #I could say explicitly 
                                              #give the binding to the parameter reverse
                                              #the value False.
printName(firstName = 'Eric', lastName = 'Grimson', reverse = True)                                              
#I could similarly for any of the parameters in the invocation
#literally say the parameter followed by an equal sign
#and the value that I want.

def printName (firstName, lastName, reverse = False): #I can change the definition of my function 
                                                     #to give a default value to one of the parameter
    if reverse:
        print(lastName+", "+firstName)
    else:
        print(firstName, lastName)
printName('Eric', 'Grimson') #if I call the function without an explicit parameter passed in,
                             #the default holds true
                             #In this case, I'm going to assume that reverse is false
printName('Eric', 'Grimson', True) #if I want to change the value of that, 
                                   #I need to give it an explicit value 
                                   #to overwrite the default value.
                             
