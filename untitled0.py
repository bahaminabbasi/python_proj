# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:11:06 2021

@author: Aria-PC
"""

phrase = 'cow'
story = 'purple cows are cool!'

splitted_phrase = phrase.split()

result = False

for word in splitted_phrase:
    if (word + ' ') in story:
        result = True
        

print(result)