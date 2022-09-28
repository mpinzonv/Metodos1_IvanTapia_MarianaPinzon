# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:08:11 2022

@author: mpinz
"""

import urllib 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv'

datos_punto_5 = urllib.request.urlopen(url)

N = 100
Data = pd.read_csv(datos_punto_5,sep=',')

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

Diff = np.zeros((len(X),len(Y)))
Diff[:,0] = Y

for i in range(1,len(X)):
    for j in range(i,len(Y)):
        Diff[j,i] = Diff[j,i-1]-Diff[j-1,i-1]
        
def Newton_Gregory(X,Y,x):
    
    Sum = Y[0]
    
    mtx = np.zeros((len(X),len(Y)))
    mtx[:,0] = Y
            
    poly = 1.0
    
    for i in range(1,len(X)):
        
        poly *= ( x - X[i-1] )
        
        for j in range(i, len(X)):
            h = X[j] - X[j-i]
            Diff[j,i] = (Diff[j,i-1]-Diff[j-1,i-1])/h      
        Sum += poly*(Diff[i,i])
    
    return Sum

x = np.linspace(np.min(X),np.max(X),N)
y = Newton_Gregory(X,Y,x)

plt.plot(x,y)
plt.scatter(X,Y,color='c')
plt.xlabel("x")
plt.ylabel("y")

x = sym.Symbol('x')
y = Newton_Gregory(X,Y,x)
y = y.expand()

print('El polinomio interpolante de menor grado es:', y) 

