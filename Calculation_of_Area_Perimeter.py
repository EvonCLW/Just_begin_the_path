# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:33:10 2019

@author: 1171101679
"""

import math

i ="1"
while i=="1":

    print("Welcome! \n Which geometry do you wish to calculate?")
    Answer = input("1-->Square, 2-->Rectange, 3-->Triangle, 4-->Equilateral Triangle, 5-->Parallelogram, 6-->Trapezoid, 7-->Circle \nAnswer-")

    if (Answer=="1"):
        S = float(input("Please key in the value of side.\nS="))
        print("The area of the square is equal to\n")
        area_1 = S*S
        print(area_1)
        print("The perimeter of the square is equal to\n")
        perimeter_1 = S*4
        print(perimeter_1)
    
    elif (Answer =="2"):
        L = float(input ("please Key in the value of length. \nL="))
        W = float(input ("please key in the value of width. \nW="))
        area_2 = L*W
        print("The area of the rectange is \n")
        print(area_2)
        perimeter_2 = (2*L)+(2*W)
        print("The perimeter of the rectange is\n")
        print(perimeter_2)
                
    elif (Answer=="3"):
        B = float(input("please key in the value of base \nB="))
        H = float(input(",\n height \nH="))
        A = float(input(",\n side a \nA="))
        C = float(input(",\n side C \nC="))
        area_3 = (1/2)*B*H
        print("The area of the Triangle is \n")
        print(area_3)
        perimeter_3 = A+B+C
        print("The perimeter of the Triangle is\n")
        print(perimeter_3)
    

    elif (Answer=="4"):
        S = float(input("please key in the value of side \nS="))
        print("Height of the Equilateral Triangle is",math.sqrt(3)/2*S)
        print("Area of the Equilateral Triangle is",math.sqrt(3)/4*S*S)
    
    elif (Answer=="5"):
        B = float(input("please key in the value of base \nB="))
        H = float(input(",\n Height \nH="))
        a = float(input(",\n Side \na="))
        print("The Area of the Parallelogram is",B*H)
        print("The perimeter of the Parallelogram is", 2*a+2*B)
    
    elif (Answer=="6"):
        A = float(input("please key in the value of bases \nA="))
        B = float(input("\nB="))
        H = float(input("Height\nH="))
        C = float(input("sides \nC="))
        D = float(input("\nD="))
        print("The area of the Trapezoid is",1/2*(A+B)*H)
        print("The perimeter of the Trapezoid is", A+B+C+D)
    
    elif (Answer=="7"):
        r = float(input("please key in the value of radius \nr="))
        print("The area is", math.pi*r*r)
        print("The circumference is", math.pi*d)
        
    else:
        print("Error")
    
    i=input("Do you wish to continue? \npress 1 to continue \npress 0 to stop\n")