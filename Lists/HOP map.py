# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 20:32:53 2017

@author: Gavrilov
"""
#higher order procedure called map
result=[]
for elt in map(abs, [1, -2, 3, -4]): #1)it takes the function that expects only one argument
                                     #2)it takes a collection, a list of appropriate arguments,
                                     #3)it creates a list where it has applied that function to each element 
                                     #4)produces an ‘iterable ’, so need to walk down it
    print(elt)
    result+=[elt]
print(result)

#general form –an n-aryfunction, i.e. n collections of arguments
L1 = [1, 28, 36]
L2 = [2, 57, 9]
result = []
for elt in map(min, L1, L2): #it will apply that function to elements of those pairs of lists
    print(elt)
    result += [elt]
print(result)