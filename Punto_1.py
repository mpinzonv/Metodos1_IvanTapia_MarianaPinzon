# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:35:42 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt


def funcion_1(x):
    return 2*x - 2

def funcion_2(x):
    return 1/2 - x/2

def funcion_3(x):
    return 4-x

#Parte a)

A = [[2,-1],[1,2],[1,1]]
b = [2,1,4]
A = np.array(A)
b = np.array(b)
AT = np.dot(A.T,A)
bT = np.dot(A.T,b)    
xsol = np.linalg.solve(AT,bT)
xsol

x = range(-10,10)
plt.grid()
plt.plot(x,[funcion_1(i) for i in x])
plt.plot(x,[funcion_2(i) for i in x])
plt.plot(x,[funcion_3(i) for i in x])
plt.scatter(xsol[1],xsol[0],color='b')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Parte b)

x = np.linspace(-5,5,300)
y = np.linspace(-5,5,300)

X,Y = np.meshgrid(x,y)
N = X.shape[0]
min = 100
E_Z = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        
        x_i=X[i][j]
        y_i=Y[i][j]
        v = np.array([[x_i],[y_i]])
   
        Ax = np.dot(A,v)
        res = Ax - b
        nor = np.linalg.norm(res)
        E_Z[i][j]=nor
        if nor < min:
            min = nor

print("La distancia mínima es:",min)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1, projection = "3d")

ax.set_xlim3d(-5,5)
ax.set_ylim3d(-5,5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('$d(x^*)$')
ax.view_init(25,55)
ax.plot_surface(X,Y,E_Z, cmap ="coolwarm")
plt.show()
