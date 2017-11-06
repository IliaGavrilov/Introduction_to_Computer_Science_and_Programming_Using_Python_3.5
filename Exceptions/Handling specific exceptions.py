# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:12:01 2017

@author: Gavrilov
"""
#separate exceptclauses to deal with a particular type of exception
while True: 
    try:
        a = int(input("Tell me one number:"))
        b = int(input("Tell me anoter number:"))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError: #operand type okay, but value is illegal
        print("could not convert to a number.")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except: #for all other errors
        print("Something went very wrong")
    else: #And that will be executed when the execution of the try body works correctly.
        print("Execution of a try body works correctly")
        break    
    finally: #always executed after try, else and except clauses, 
             #even if they raised another error or executed a break, continue or return
             #useful for clean-up code (e.g. close a file)
        print("Finally always executed even despite break")
