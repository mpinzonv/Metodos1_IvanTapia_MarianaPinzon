# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:01:57 2022

@author: mpinz
"""

import numpy as np

N=100000

x_1 = np.linspace(0.1,0.9,N)
x_2 = np.linspace(0.1,0.5,N)
respuesta = np.zeros(N)
for i in range(N): 
    respuesta[i]=6*(x_1[i])**2*(1-x_1[i])**2 

#¿En qué punto la probabilidad es mínima?

v_min = np.min(respuesta)
v_min = round(v_min,5)
p_min = np.argmin(respuesta)

print("El valor de la probabilidad es:",v_min)
print("El punto donde la probabilidad es la mínima es:",p_min)

#¿En qué punto la probabilidad es máxima?

v_max = np.max(respuesta)
v_max = round(v_max,5)
p_max = np.argmax(respuesta)
print("El valor de la probabilidad es:",v_max)
print("El punto donde la probabilidad es la máxima es:",p_max)



