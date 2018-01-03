# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:50:11 2017

@author: Gavrilov
"""
#we don't want to directly manipulate the internal representation of an object.
#We'd like to separate the use of the object from what's inside of it.
#And those getters and setters nicely do that. It says any time I want to access something
#inside an object, let me use the method that gets that part of the object out.
#representational invariant example
#I need two pieces. Data representation (class?) and I need an interface (methods? frame?).
class intSet(object):
    def __init__(self):
        self.vals = [] #initially the set is empty
                       #I don't want to have to go and check, do I have more than one instance inside the object?
                       #I want it to be the case that as I add elements to this set, I'm always making sure 
                       #that there's never more than one particular version of that integer inside of that set.

    def insert(self, e): #I can insert things into the set. 
                         #And here's where I'm going to enforce the representational invariant.
        if not e in self.vals: #when I want to insert a particular element into an instance of an IntegerSet,
                               #I'm going to first say, is that element inside the list?
            self.vals.append(e)
    
    def member(self, e): #I want to check if something's inside the list.
                         #I can simply say, return e in self.vals.
        return e in self.vals
    
    def remove(self, e): #I need to be able to remove an element from a set.
        try:
            self.vals.remove(e)
        except: #can use exseption to catch attempt to remove nonexistent element
            raise ValueError(str(e) + " element not found")
    def __str__(self):
        self.vals.sort()
        result=""
        for e in self.vals:
            result = result + str(e) + ","
        return "{" + result[:-1] + "}"
    
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3) #I'm going to insert 3 again, because I have a short memory
            #and I've forgotten I've already done that.
print(s)

print(s.member(3)) # I could check to see if something is in the list.
print(s.member(6))

s.remove(3) #I can remove something. #this is a example of a method we defined 
            #which is similar to operation 'lst.remove(val)', but difference is that 
            #we created our method by ourselves and use it as primitive

s.insert(6) #I'm simply using those built in methods to manipulate that set.
print(s)
#s.remove(7)
