# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:16:06 2017

@author: Gavrilov
"""
#important high-level issue, which is when you're accessing data attributes outside
#of the classes, you should always use the getters
class Animal(object):
    def __init__(self, age): 
        self.years = age #author of class definition may change data attribute variable names
                         #Here I've decided to have init define years to hold the value of age.
    
    def getAge(self): #I can make that be OK by simply changing simply changing the getter 
        return self.years #so that it refers to that piece.
      
    def setAge(self, new_age):
        self.years = new_age 
        
myAnimal=Animal(3) 
#print(myAnimal.age) #If you're doing access directly outside of the class 
                    #and the class definition changes (age to years), may get errors.
print(myAnimal.getAge()) #whereas if I use the getter and I've changed it, this will always work well.
#Python allows you to access data from outside class definition, for example, print(a.age)
#and allows you to write to data from outside class definition, for example, a.age = 'infinite'
#as well as allows you to create data attributes for an instance from outside class definition, like, a.size = "tiny"
#But Always write a method to store new attributes inside of it 
#to access using getters the attribute values that you want out there.
