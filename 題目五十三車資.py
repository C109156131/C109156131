# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:08:11 2021

@author: user
"""

a=float(input("請輸入路程公里數(km):"))
b=75
if a==0:
    print("所需車資為: 0")
else:
    if a>=1.5:
        a-=1.5
        add=int(a//0.25+0.5)
        if a%0.25>0:
            add+=1
        print("所需車資為:",b+add*5)
    else:
        print("所需車資為: 75")