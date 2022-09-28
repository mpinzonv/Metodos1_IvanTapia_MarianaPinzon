# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:18:21 2022

@author: mpinz
"""

import urllib 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym


url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'

datos_punto_4 = urllib.request.urlopen(url)

N = 100
Data = pd.read_csv(datos_punto_4,sep=',')

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x-xi[i])/(xi[j]-xi[i])
            
    return prod

def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

x=np.linspace(-5,10,N)
plt.scatter(X,Y,color='c')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,Poly(x,X,Y))

x = sym.Symbol('x')
poly_c = sym.expand(Poly(x,X,Y))
coef_c=float(poly_c.coeff(x,2))
deriv=sym.diff(poly_c)
theta=(float(deriv.coeff(x,0)))
v_inicial = np.sqrt(np.abs(9.8/(coef_c*2*(np.cos(theta)**2))))
theta = np.degrees(theta)


print('La velocidad inicial es %.0f m/s con un ángulo de inclinación de %.0f grados con respecto a la horizontal'%(v_inicial,theta))
