# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:00:07 2017

@author: Gavrilov
"""

def get_data(aTuple):
    num=() #Open close paren set up Nums to be an empty tuple
    words=()
    for t in aTuple:
        num=num+(t[0],)
        if t[1] not in words:
            words=words+(t[1],)
    min_num=min(num)
    max_num=max(num)
    unique_words=len(words)
    return (min_num, max_num, unique_words)
small, large, words = get_data(((1, "mine"), 
                                (3, 'yours'), 
                                (5, 'ours'), 
                                (7, 'mine'))) #multiple assignment
print("Small: ", small)
print("Large: ", large)
print("Unique words: ", words)