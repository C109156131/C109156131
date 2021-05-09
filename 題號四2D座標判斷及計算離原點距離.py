# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:02:27 2021

@author: user
"""

a=int(input("輸入平面中某點的X值"))
b=int(input("輸入平面中某點的Y值"))
c=a*a+b*b
if a>0 and b>0:
    print("該點位於第一象限,離原點距離為根號"+str(c))
elif a<0 and b>0:
    print("該點位於第二象限,離原點距離為根號"+str(c))
elif a<0 and b<0:
    print("該點位於第三象限,離原點距離為根號"+str(c))
elif a>0 and b<0:
    print("該點位於第四象限,離原點距離為根號"+str(c))
elif a==0 and b==0:
    print("該點位於原點")
elif a==0 and b>0:
    print("該點位於上半平面Y軸上,離原點距離為根號"+str(c))
elif a==0 and b<0:
    print("該點位於下半平面Y軸上,離原點距離為根號"+str(c))
elif a>0 and b==0:
    print("該點位於右半平面X軸上,離原點距離為根號"+str(c))
elif a<0 and b==0:
    print("該點位於左半平面X軸上,離原點距離為根號"+str(c))    