# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:54:09 2017

@author: Gavrilov
"""

def getStats(class_list):
    newStats = []
    for element in class_list:
        newStats.append([element[0], element[1], average(element[1])])
    return newStats
        
def average(grades): #helper function
    """
    instead of a notifying of exception in a code:
        try:
            return sum(grades)/len(grades)
        except ZeroDivisionError:
            print("no grades data")
    which will give none if there are no grades
    
    use raise
    """
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("no grades data") #So will give me the warning.
                                #I handled that error by saying that's what I want to do.
        return 0.0 #I could decide I'm just going to give a 0 value
                   #catching that 0 division error idea, I can put an explicit return.
        

class_list = [[["Ilia", "Gavrilov"], [10.0, 5.0, 85.0]], 
              [['Erich', "Grimson"], [10.0, 8.0, 74.0]]] 
class_list2 = [[['deadpool', 'superhero'],[]]]
print(getStats(class_list))
print(getStats(class_list2))