# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 19:22:03 2017

@author: Gavrilov
"""

data = []
file_name = input("Provide a name of a file of data ") #I get a file name by asking for input from the user
try:
    fh = open(file_name, 'r') #I'm going to open up the file and I'm going to be able to execute out
except IOError: #If IO system reports malfunction (e.g. file not found)
                #I am going to catch that    
    print("Cannot open", file_name)
else: #if I do open it up, I go to the else clause, and I'm going to walk through the file
    for new in fh:
        if new != '\n': #I'm reading in a new line, as long as it isn't just a carriage return
            print("new is: ", new)
            addIt = new[:-1].split(',') #I'm going to take the line, split it by the commas
                                        #to separate out the pieces to create a list
            print("addIt is: ", addIt, '\n')
            data.append(addIt)
            print("data is ", data, '\n')
finally: #saying close up the file when you're done with all of this
    print("final version of data is: ", data)
    fh.close()
