# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:16:30 2021

@author: user
"""

data1=int(input("請輸入第一個要判斷的數字："))
data2=int(input("請輸入第二個要判斷的數字："))
data3 = data1 % 2
data4 = data2 % 2
if data3 == 0 or data4 == 0:
    print("N")
else:
    print("Y")