# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#I've got ways of dealing with different kinds of objects. The methods can shadow other methods higher up in the hierarchy.
#I'm always going to start with the class associated with the instance and look for a method there.
#If there isn't one, then I'm going to go up the hierarchy to see if there's a method defined earlier on in that chain.
class Animal(object): #object is underlying class, animal is parent class
    def __init__(self, age):
        self.age = age
        self.name = None
    def getAge(self): #I've got getters.
        return self.age
    def getName(self):
        return self.name
    def setAge(self, newAge): #I've got setters.
        self.age = newAge
    def setName(self, newName=""):
        self.name = newName
    def __str__(self): #I got a way of printing them out
        return "Animal: " + str(self.name) + ":" + str(self.age)
    
class Cat(Animal): #children subclass
    def speak(self): #new functionality via new methods
        print("meow")
    def __str__(self): 
        return "Cat: " + str(self.name) + ":" + str(self.age) 

Kitty = Cat(1)
print(Kitty) #It says you've got None associated with the name, because I don't have one there.
Kitty.setName() #I could change that name as well. I'm simply going to give it no argument.
print(Kitty)
