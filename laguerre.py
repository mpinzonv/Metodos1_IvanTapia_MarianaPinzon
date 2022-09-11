# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 18:49:39 2022

@author: mpinz
"""

from numbers import Real
import numpy as np
import sympy as sym

def newton_rap(f,df,xo):
    for i in range(1000):
        x=xo-f(xo)/df(xo)
        if abs(x-xo)<10**(-9):
            return(x)
        xo=x
    return(False)

def todas_raices(x,f,df):
    raices = []
    for i in x:
        root = newton_rap(f,df,i)
        redondeo=round(root,5)
        if redondeo not in raices:
            raices.append(redondeo)
        raices.sort()
    return raices

def poli_laguerre(n):
    x=sym.Symbol('x',Real=True)
    funcion=sym.exp(-x)*x**n
    derivada=sym.exp(x)*sym.diff(funcion,x,n)/(np.math.factorial(n))
    return(derivada)

for n in range(1,21):
    x = sym.Symbol('x',Real=True)
    f=sym.lambdify([x],poli_laguerre(n),'numpy')
    df=sym.lambdify([x],sym.diff(poli_laguerre(n),x,1),'numpy')
    x_prueba = np.linspace(0,100,300)
    raices = todas_raices(x_prueba,f,df)
    print(f'las raices del polinomio de laguerre para n={n} son: {raices}')