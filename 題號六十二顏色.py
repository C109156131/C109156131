# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:03:01 2021

@author: user
"""

dict1 ={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
print(dict1.keys())
data=input("請輸入水果:")
print("%s是%s" %(data,dict1[data]))