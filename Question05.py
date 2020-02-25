# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:34:10 2019

@author: 1171101679
"""

count=0

howmanystr = int(input("how many string u want to key in?\n"))

for x in range(howmanystr):
    print("String Number"+ str(x+1),"please")
    dummy = input()
    if len(dummy)>=2:
        count = count+1
        
print("There are"+str(count)+"string(s)with length of 2 or more")