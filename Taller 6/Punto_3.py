# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:37:17 2022

@author: mpinz
"""

import numpy as np

a = np.array([[1, 0, 0], [5, 1, 0], [-2, 3, 1]])
b = np.array([[4, -2, 1], [0, 3, 7], [0, 0, 2]])

def mult(a,b):
    res=[]
    
    for i in range(3):
        e=[]
        for j in range(3):
            r=0
            for k in range(3):
                f1 = a[i][k]*b[k][j]
                r=r+f1
            e.append(r)
        res.append(e)
    res=np.array(res)
    return res
print(mult(a,b))
print(np.matmul(a,b))






