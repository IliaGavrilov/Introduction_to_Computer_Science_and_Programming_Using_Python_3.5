# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:18:20 2017

@author: Gavrilov
"""
#example to do squaring by repetitive addition
x = 27 #I'm going to start off with something that I want to square
ans = 0 #That's going to be where my answer goes
itersLeft = x #And I'm going to keep track of how many times I need to go through the process
while itersLeft != 0: #if I'm not down to 0,
    ans = ans + x #I'm going to increase ans by x. 
    itersLeft = itersLeft - 1 #I'm going to decrease the number of steps by 1.
print(str(x)+"*"+str(x)+"="+str(ans))

