# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:32:30 2017

@author: Gavrilov
"""
#global variable break the scoping of variables that we get by a function call,
#but it's really handy if we want to keep track of the information inside of a function.
def fib(n):
    global numFibCalls #global says that I can access outside the scope of the function
                       #variable that is going to keep track of function call
    numFibCalls +=1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib (n-2)

def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d: #iterates over keys
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans #here is where we add value to key
        return ans

numFibCalls=0
argToUse = 12

print(fib(argToUse))
print("function calls", numFibCalls)

numFibCalls=0

d = {1:1, 2:2}
print(fib_efficient(argToUse, d))
print('function calls', numFibCalls)