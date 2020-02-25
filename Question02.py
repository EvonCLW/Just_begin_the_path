# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:30:43 2019

@author: 1171101679
"""

import math

A = "What is A?\n"
A = input(A)
A = float(A)
A = round(A,2)
B = "What is B?\n"
B = input(B)
B = float(B)
B = round(B,2)
C = "What is C?\n"
C = input(C)
C = float(C)
C= round(C,2)

if (C*C)<(A*A+B*B):
    print("Acute Triangle")
elif (C*C)>(A*A+B*B):
    print("Obtuse Triangle")
else:
    print("Right Triangle")