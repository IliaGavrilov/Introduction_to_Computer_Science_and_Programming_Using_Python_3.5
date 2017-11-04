# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:49:22 2017

@author: Gavrilov
"""

def printMove(fr, to):
    '''
    print an individual move from the from stack
    to the to stack.
    '''
    print("Move from "+str(fr)+" to "+str(to))
    

#break it down into a smaller version of the same problem
#let the recursion get to the solution 
def Towers(n, fr, to, spare):
    if n == 1: #test for a base case
        printMove(fr, to)
    else: #I actually now have to solve two recursive problems
          #multiple recursive calls inside of a function body
        Towers(n-1, fr, spare, to) #I'm going to move a smaller stack from to from to the spare swap.
        Towers(1, fr, to, spare) #I'm going to move the simple case to the place I'm trying to go to.
        Towers(n-1, spare, to, fr) #I got to move another smaller size stack from the spare over to the to spot.
print(Towers(3, "P1", "P2", "P3"))