# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:36:00 2019

@author: 1171101679
"""

number=[]
range1 = int(input("Please enter the upper number.\n"))
range2 = int(input("Please enter the lower number.\n"))

for x in range(range1,range2):
    if(x%7==0) and (x%5==0):
        number.append(x)
print(number)