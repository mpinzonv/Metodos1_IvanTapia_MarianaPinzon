# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 18:44:01 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

eqs=lambda x:3*x**5+5*x**4-x**3

def derivada(f,x,h=1e-10):
    return((f(x+h)-f(x-h))/(2*h))

def newton_rap(f,df,xo):
    for i in range(1000):
        x=xo-f(xo)/df(f,xo)
        if abs(x-xo)<10**(-10):
            return(x)
        xo=x
    return(False)

def todas_raices(x):
    raices = []
    for i in x:
        root = newton_rap(eqs,derivada,i)
        redondeo=round(root,8)
        if redondeo not in raices:
            raices.append(redondeo)
        raices.sort()
    return raices

x_prueba = np.linspace(-10,10,100)
raices = todas_raices(x_prueba)

print(f'las raices del polinomio son: {raices}')



#print(f"La solución de la ecuacion para c = 2 es {(solution_a)}")
