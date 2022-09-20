# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:08:08 2022

@author: mpinz
"""

import numpy as np

import sympy as sp
from sympy.abc import h


#El error asociado a la regla de Simpson 3/8 simple
#h = 1
n = 3
funcion = sp.Array([0,(h),(2*h),3*h])

x = sp.Symbol("x",Real=True)
x_i = sp.Symbol(r"\x_i")
f = sp.Function("f", Real=True)(x_i)
g = sp.Function("g", Real=True)

g = (x-funcion[0])*(x-funcion[1])*(x-funcion[2])*(x-funcion[3])

integral= sp.integrate(g,(x,funcion[0],funcion[-1]))

derivada = sp.Derivative(f,x,4)
integral *= derivada/np.math.factorial(4)

resultado_final = integral

print ("El error asociado a la regla de Simpson 3/8 simple es: ",resultado_final)











