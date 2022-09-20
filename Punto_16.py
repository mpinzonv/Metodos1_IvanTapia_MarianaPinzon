# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:20:41 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

#Punto a) Integral usando el método de cuadratura de Gauss-Laguerre para n=3

n = 3
func_problema = lambda x : np.exp(x)*x**3/(np.exp(x)-1)
r = np.pi**4/15


def funcion_laguerre(f,n):
    roots,weights = np.polynomial.laguerre.laggauss(n)
    return np.sum(weights*func_problema(roots))


#Punto b) Gráfica del error relativo

n = [2,3,4,5,6,7,8,9,10]
matriz = [] 
x = np.arange(2,11)

for n in x:
    integral = funcion_laguerre(func_problema,n)
    error = (integral/r)
    matriz = np.append(matriz,error)
    
plt.figure(figsize=(5,5))
plt.plot(x,matriz,"o")
plt.title("Accurracy vs n-points for the Gauss-Laguerre quadrature")
plt.grid()
plt.xlabel("n-points")
plt.ylabel("Accurracy")
plt.show()
