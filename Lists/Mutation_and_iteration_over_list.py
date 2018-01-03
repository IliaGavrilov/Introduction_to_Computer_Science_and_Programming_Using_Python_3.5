# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:04:41 2017

@author: Gavrilov
"""
#wrong example
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e) #because Python uses an internal counter
                         #when I mutate list, which Remove does, 
                         #it actually caused Python to never see the element two
    return L1
L1=[1,2,3,4]
L2=[1,2,5,6]
print(remove_dups(L1,L2))

#correct example
def remove_dups_new(L1,L2):
    L1_copy=L1[::] #clone list first
    for e in L1_copy:
        if e in L2:
            L1.remove(e) #when I'm mutating L1, I've still got something
                         #that I'm iterating over that hasn't changed
    return L1
L1=[1,2,3,4]
L2=[1,2,5,6]
print(remove_dups_new(L1,L2))
