# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:05:13 2021

@author: user
"""

list1=[]
n=int(input("請輸入正整數n:"))
for i in range(1,n):
    if n%i==0:
       list1.append(i)

a=sum(list1)
if a==n:
    print("perfect")
elif a>n:
    print("abundant")
else:
    print("deficient")