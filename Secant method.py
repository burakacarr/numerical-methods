#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import fabs 
def f(x):
    return (x**2-2*x-3)

def error(x1,x2):
    return((x1-x2)/x1)

def RootControl(x1,x2):
    if(f(x1)==0 or f(x2)==0):
        if(f(x1)==0):
            print("Root of the equation :" , x1)
        if(f(x2)==0):
            print("Root of the equation :", x2)
        return 1
    else:
        return 0
x1 = int(input("Enter first value"))
x2 = int(input("Enter second value"))
ErrorValue = error(x1,x2)
RootValue = RootControl(x1,x2)

while(fabs(ErrorValue) >0.002 and RootValue != 1):
    x3 = x1 - (f(x1)*(x2-x1))/(f(x2)-f(x1))
    if(f(x2)-f(x1)==0):
        ErrorValue=0
    else:
        ErrorValue = error(x1,x2)
    print("x2: ",x2,"x1: ",x1, "change:", x3,"Error Value= ",ErrorValue, RootValue)
    x1,x2 = x2,x3

        
    
