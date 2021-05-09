# -*- coding: utf-8 -*-
"""
Created on Sun May  9 18:31:08 2021

@author: user
"""

a=int(input("輸入一個度數"))
if a<=120:
    print("Summer months:"+str(a*2.10)
          +"Non-Summer months"+str(a*2.10))
elif 330>=a>=121:
    print("Summer months:"+str(a(-120)*3.02+252)
          +"Non-Summer months"+str((a-120)*2.68+252))
elif 500>=a>=331:
     print("Summer months:"+str((a-330)*4.39+252+634.2)
          +"Non-Summer months"+str((a-330)*3.61+252+562.8))
elif 700>=a>=501:
      print("Summer months:"+str((a-500)*4.97+252+634.2+746.3)
          +"Non-Summer months"+str((a-500)*4.01+252+562.8+613.7))
elif 701>=a:
      print("Summer months:"+str((a-700)*5.63+252+634.2+746.3+994)
          +"Non-Summer months"+str((a-700)*4.50+252+562.8+613.7+802))