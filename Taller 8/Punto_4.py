# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:03:52 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt 

#Probabilidad P(n ≤ 80) de que tengan una edad diferente

def func_product(rango):
    product = 1
    
    for i in range(rango):
        product *= (365-i)/365
    return product

n = []
list = []

for i in range(80):
    list.append(func_product(i))
    n.append(i)
    
plt.plot(n,list,linestyle = "-")

plt.xlabel("Personas")
plt.ylabel("P(n)")
plt.show()
