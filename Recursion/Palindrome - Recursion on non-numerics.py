# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:09:30 2017

@author: Gavrilov
"""
#divide and conquer algorithm.
def isPalindrome(s):
    def toChars(s): #function which convert string into characters
        s=s.lower() #built in method lower
        ans=""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print("")
print("Is eve a palindrome?")
print(isPalindrome("eve"))

print("")
print("Is able was I ere I saw Elba a palindrome?")
print(isPalindrome("Able was I, ere I saw Elba"))       