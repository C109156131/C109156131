# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:22:15 2021

@author: user
"""

a=int(input("請輸入n:"))
b=int(input("請輸入k:"))
c=a//b
d=0
e=0




if(c<b):
    
    d=a+c

    print("Peter可以抽",d,"支菸")

elif(c>=b):
   d=a+c
   while(c >= b):
       c=c//b
       d=d+c
    
print("Peter可以抽",d,"支菸")
