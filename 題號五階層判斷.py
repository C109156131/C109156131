# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:16:40 2021

@author: user
"""

a=int(input("輸入階層值M"))
b=1
c=1
while(b<a):
    c=c+1
    b=b*c
print("超過M為"+str(a)+"的最小階層N值為:"+str(c))