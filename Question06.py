# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:34:59 2019

@author: 1171101679
"""

textlist =[]

for x in range (10):
    input01 = input('Please input 10 text\n')
    textlist.append(input01)
    
textlist.pop(1)
textlist.pop(5)
textlist.pop(6)
#textlist.pop(7)

print("This is the list without element of position 2, 7 & 9 \n")
print(textlist)