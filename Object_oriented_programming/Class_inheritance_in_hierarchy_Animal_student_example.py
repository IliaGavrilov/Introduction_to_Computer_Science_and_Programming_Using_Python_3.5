# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#using hierarchy
#We know that a subclass can have methods with the same name
#as a superclass. But we always start with that subclass.
class Animal(object):
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

class Rabbit(Animal): #children subclass
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit: " + str(self.name) + ":" + str(self.age) 
    
class Person(Animal): #children subclass (subclass of an animal)
    def __init__(self, name, age):
        Animal.__init__(self, age) #underlying Animal method to create the instance.
        Animal.setName(self, name) #underlying setName() method of Animal 
                                   #to change the name associated with this instance of a Person.
        self.friends = [] 
    def getFriends(self):
        return self.friends
    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print ("hello")
    def ageDiff(self,other):
        #alternative way: diff = self.age - other age
        diff = self.getAge() - other.getAge()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: "+ str(self.name) + ":" + str(self.age)

import random #I import from the Miranda module ways of doing random

class Student(Person): #inherits Person and Animal attributes 
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age) #I'm going to create a constructor for this. It is going to 
                                         #use the Person creation method, the initialization method.
                                         #That used inherently a direct call to Animal. So I can chain up here.
        self.major = major #the one other thing I want to do here is, a Student has a major.
    def changeMajor(self, major):
        self.major = major #students often change majors. So I can do that 
                           #by simply having them decide they want to have a new major.
    def speak(self):
        r = random.random() #I'm going to inherit from a module the ability to just randomly pick a number.
                            #this particular call is going to give me back a number between 0 and 1.
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching TV")
    def __str__(self):
        return "Student: " + str(self.name) + ":" + str(self.age) + ":" + str(self.major)

fred = Student("Fred", 18, "Course VI")
print(fred) #uses method from student (including __str__ method)
print(fred.speak()) 
