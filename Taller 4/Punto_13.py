# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:41:46 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

n = 3
x = sp.Symbol('x',Real=True)
y = sp.Symbol('y',Real=True)

def funcion_legendre(n, x,y):
    y = (x**2-1)**n
    pol = sp.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return pol

polinomio_p = (3 + 5*x + x**2)

coeficientes = []
for i in range(n):
    coeficientes.append(polinomio_p.coeff(x,i))

legendre = []
for i in range(n+1):
    legendre.append(funcion_legendre(i,x,y).expand())

matriz = sp.zeros(n,n)
for i in range(n):
    for j in range(n):
        matriz[j,i]=(legendre[i].coeff(x,j))  
        
b=sp.Matrix(coeficientes)
matriz = matriz.inv()
matriz_nw = matriz*b

respuesta = ""
for i in range(n):
    respuesta += (str(matriz_nw[i])+'*p'+str(i)+'(x) + ')
respuesta = respuesta[:-2]

print("El polinomio p(x) en la base de Legendre es:",respuesta)

