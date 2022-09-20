# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:45:40 2022

@author: mpinz
"""

import numpy as np
import sympy as sym

x = np.linspace(-1,1,100)
funcion = lambda x: np.sqrt(1+np.exp(-x**2))

def simpson_38(y,a,b):
    
    m_1 = (2*a+b)/3
    m_2 = (a+2*b)/3
    integral = (b-a)/8*(y(a)+3*y(m_1)+3*y(m_2)+y(b))
    return integral

integral = 0

for i in range(1,len(x)):
    integral += simpson_38(funcion,x[i-1],x[i])
    
resultado_integral = integral
resultado_integral_red = round(resultado_integral,10)
    
print("El resultado de la integral es:",resultado_integral_red)




