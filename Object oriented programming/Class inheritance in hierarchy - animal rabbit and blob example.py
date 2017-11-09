# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#I can inherit methods from higher in the hierarchy, something higher in the hierarchy 
#cannot access a method of a subclass.
#I use the appropriate method by letting the instance tell me what kind of method I should look up.
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

class Rabbit(Animal): #children subclass
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit: " + str(self.name) + ":" + str(self.age) 
    
class Person(Animal): #children subclass
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.setName(self, name)
        self.friends = []
    def getFriends(self):
        return self.friends
    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print ("hello")
    def ageDiff(self,other):
        diff = self.getAge() - other.getAge()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: "+ str(self.name) + ":" + str(self.age)

import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def changeMajor(self, major):
        self.major = major
    def speak(self):
        r = random.random()
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

jelly = Cat(1)
jelly.setName("JellyBelly")      
print(jelly.speak()) #There is one speak() method associated with cats,
                     #Now I didn't define speak() inside the instance, but because this is an instance, 
                     #I know it's a kind of Cat. I look up the speak() method inside of Cat, which is why it does the right thing.
peter = Rabbit(5)
print(peter.speak()) #and another speak method associated with rabbits

blob = Animal(3)
#print(blob.speak()) #AttributeError because there is no speak() method associated with Animal.
                     #Blob is an instance of Animal. Look up an Animal. 
                     #The definition for a method for speak() - there isn't one.

#eric = Person("Eric", 45)
#john = Person("John", 55)
#print(eric.ageDiff(john))
#print(Person.ageDiff(john,eric))
#fred = Student("Fred", 18, "Course VI")
#print(fred)
#print(fred.speak())