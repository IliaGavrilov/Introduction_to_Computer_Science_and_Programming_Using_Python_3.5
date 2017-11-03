# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:53:51 2017

@author: Gavrilov
"""

def g(y):
    print(x) #I've already
             #defined x from outside g.
             #That's why I pick up that scope.
    print(x+1)
x = 5 #I've defined x to be 5
g(x)

#unbound variable error in 
def h(y): #the value of y being 5
    x = x + 1 #I'm going to try and define x to be x plus 1
              #I got an unbound variable error,
              #because I'm trying to look up the local variable value of x
              #I'm referencing it before I've assigned it
    return x
print(h(x)) #now I call h with 

#the moment in which you declare the variable x within the scope of the function h() 
#de facto you create a new variable
#fresh declared variable has no value
