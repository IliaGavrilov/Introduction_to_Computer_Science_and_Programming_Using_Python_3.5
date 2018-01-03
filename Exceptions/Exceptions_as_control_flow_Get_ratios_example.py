# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:02:17 2017

@author: Gavrilov
"""

def getRatios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    Ratios = []
    for index in range(len(L1)):
        try:
            Ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            Ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError("Ratios called with bad argument") #manage flow of program by raising own error
    return Ratios
L1 = [1, 2, 3, 4]
L2 = [5, 6, 0, 4]
L3 = [7, 8, 9]
print(getRatios(L1, L2))
print(getRatios(L1, L3))
