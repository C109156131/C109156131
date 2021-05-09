# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:38:28 2021

@author: user
"""

dict1 = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
a = 0
b = input("請輸入五張牌").split(" ")

for i in range (len(b)):
    a = dict1[b[i]] + a
    

print(a)