# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:31:16 2019

@author: 1171101679
"""

from math import sqrt

formula = input("Which side (a,b,c) do you wish to calculate?\n")

if formula == 'c':
    side_a = int(input('Input the length of side a: '))
    side_b = int(input('Input the length of side b: '))
    
    side_c = sqrt(side_a*side_a + side_b*side_b)
    
    print('The length of the side c is:')
    print(side_c)
    
elif formula == 'a':
    side_b = int(input('Input the length of side b:'))
    side_c = int(input('Input the length of side c:'))
    
    side_a = sqrt((side_c*side_c)-(side_b*side_b))
    
    print('The length of the side a is:')
    print(side_a)
    
elif formula == 'b':
    side_a = int(input('Input the length of side a:'))
    side_c = int(input('Input the length of side c:'))
    
    side_b = sqrt((side_c*side_c)-(side_a*side_a))
    
    print('The length of the side b is:')
    print(side_b)
    
else:
    print('please select a side between a,b,c')
    
    
    