# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:32:30 2017

@author: Gavrilov
"""
#building a tree of computations
#this code is inefficient
#it really slows down when trying to compute large numbers
def fib(n): #it had two base cases
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib (n-2) #It calls itself twice

#Memoization
#Rather than recalculating the same value many times,
#let's just keep track of what I've already done.
def fib_efficient(n, d): #I'm going to compute Fibonacci, the n-th
                         #but I'm going to give it a dictionary. 
    if n in d: #iterates over keys #if n is already in the dictionary,
        return d[n] #I just look up the value and return it.
    else: 
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d) #Otherwise, I do the recursive call 
        d[n] = ans #I store that value away in the dictionary,
        return ans
d = {1:1, 2:2} #I put into the dictionary the first and second Fibonacci numbers.
argToUse = 34

print("")
print("using fib")
print(fib(argToUse))
print("")
print("using fib efficient")
print(fib_efficient(argToUse, d)) #fib efficient came about really quickly