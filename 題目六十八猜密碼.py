# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:04:17 2021

@author: user
"""

data1 = input("請輸入第一組數字:")
data2 = input("請輸入第二組數字:")
a=b=0
for i in range(0,len(data1)):
    pt = data1.find(data2[i])
    if pt ==-1:
        continue
    else:
        if i==pt:
            a+=1
        else:
            b+=1
if a==4:
    print("%dA%dB 全對" %(a,b))
else:
    print("%dA%dB 加油" %(a,b))