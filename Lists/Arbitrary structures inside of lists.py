# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:32:56 2017

@author: Gavrilov
"""
#arbitrary structures inside of lists.
#So I could have nested lists, lists of lists
warm=['yellow','orange']
hot=['red']
brightcolors=[warm]
print(brightcolors)
brightcolors.append(hot)
print(brightcolors)

hot.append('pink') #I didn't say do something to bright colors
                   #but it's changed because of that aliasing or side effect
print(hot)

print(brightcolors)
print(hot+warm) #I get, in this case, the nice concatenation of them