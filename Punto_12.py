# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:30:15 2022

@author: mpinz
"""

import numpy as np

funcion_problema = lambda x : 1/(x**2)
r = lambda x : -1/x

#Integral I_2 cuando n = 2

n = 2
roots,weights = np.polynomial.legendre.leggauss(n)
resolv = 0.5*((2-1)*roots + 1 + 2)

integral = 0.5*(2-1)*np.sum( weights*funcion_problema(resolv))
integral,r(2)-r(1)

resultado_integral = integral
resultado_integral_red = round(resultado_integral,6)

print ("I_2 es igual a:",resultado_integral_red)

#Integral I_3 cuando n = 3

n = 3
roots,weights = np.polynomial.legendre.leggauss(n)
resolv = 0.5*((2-1)*roots + 1 + 2)

integral = 0.5*(2-1)*np.sum( weights*funcion_problema(resolv))
integral,r(2)-r(1)

resultado_integral = integral
resultado_integral_red = round(resultado_integral,6)

print ("I_3 es igual a:", resultado_integral_red)

