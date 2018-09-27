#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(array,x):
    total=0;
    a=0
    for i in range(len(array)-1,-1,-1):
        total=total+array[a]*x**i
        a+=1
    return total
def fi(array,x):
    total=0
    a=0
    for i in range(len(array)-1,0,-1): 
        total=total+a*i*x**i-1
        a+=1
    return total
def RootFind(array,xi):
    for i in range(1000):
        if(fi(array,xi)==0):
            print("you entered an incorrect value:")
            xi=float(input("enter new value:"))
        x2=xi-f(array,xi)/fi(array,xi)
        xi=x2
    return (xi)
        
array=[]
resultArray=[]
degree=int(input("degree of equation:"))
for i in range(degree+1):
    value2=float(input("%d Enter the coefficient of degree"%(i)))
    array.append(value2)
xi = float(input("enter the start value: "))
while(len(array)-2):
    xi=RootFind(array,xi)
    resultArray.append(xi)
    for i in range(1,len(array)-1):
           array[i]=xi*array[i-1]+array[i]
    array.pop()
x=-1*array[1]/array[0]
resultArray.append(x)
print (resultArray)

