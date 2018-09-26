#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import fabs 
def f(a,b,c,x):
    return (a*x**2+b*x+c)

print("Enter the values a, b, c of the equation to be ax2 + bx + c")
a= int(input("Enter a:"))
b= int(input("Enter b:"))
c= int(input("Enter c:"))
def error(x1,x2):
    return((x1-x2)/x1)

def RootControl(x1,x2):
    if(f(a,b,c,x1)==0 or f(a,b,c,x2)==0):
        if(f(a,b,c,x1)==0):
            print("Root of the equation :" , x1)
        if(f(a,b,c,x2)==0):
            print("Root of the equation :", x2)
        return 1
    else:
        return 0
if(b**2-4*a*c<0):
    print("there is no linear root of the equation you entered")
    
else:
    
    x1 =int(input("Enter first value"))
    x2 = int(input("Enter second value"))
    ErrorValue = error(x1,x2)
    RootValue = RootControl(x1,x2)

    while(fabs(ErrorValue) >0.002 and RootValue != 1):
        if(f(a,b,c,x2)-f(a,b,c,x1)==0):
            ErrorValue=1
            print("division by zero")
            continue
        else:
            ErrorValue = error(x1,x2)
        x3 = x1 - (f(a,b,c,x1)*(x2-x1))/(f(a,b,c,x2)-f(a,b,c,x1))
    
        print("x2: ",x2,"x1: ",x1, "change:", x3,"Error Value= ",ErrorValue, RootValue)
        x1,x2 = x2,x3

        
    
