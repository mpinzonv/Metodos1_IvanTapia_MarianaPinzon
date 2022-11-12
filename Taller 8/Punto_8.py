# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:51:08 2022

@author: mpinz
"""

import numpy as np
import random

#Probabilidad de obtener dos caras y dos sellos

N=100000
t = 0

for i in range (int(N)):
  moneda_1=np.random.choice([-1,1])
  moneda_2=np.random.choice([-1,1])
  moneda_3=np.random.choice([-1,1])
  moneda_4=np.random.choice([-1,1])
  sum = moneda_1 + moneda_2 + moneda_3 + moneda_4
  if sum == 0: 
    t += 1
probabilidad = t/N
print ("La probabilidad es:",str(probabilidad))




