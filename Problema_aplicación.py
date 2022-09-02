# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:19:56 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

#Punto a)

x = np.linspace(-4,4,25)
y = x.copy()
h = 0.001
N = 25

#Punto b)

def Potencial_flujo(x,y): 
    return (2*x)-((8*x)/((x**2)+(y**2)))

#Punto c)

def Dx(f,x,y,h):
    if np.sqrt(x**2+y**2)<=2:
        return 0
    else:
        return (f(x+h,y)-f(x-h,y))/(2*h)
def Dy(f,x,y,h):
    if np.sqrt(x**2+y**2)<=2:
        return 0 
    else:
        return -(f(x,y+h)-f(x,y-h))/(2*h)

Ex = np.zeros((N,N))
Ey = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        Ex[i,j]=Dx(Potencial_flujo,x[i],y[j],h)
        Ey[i,j]=Dy(Potencial_flujo,x[i],y[j],h)
        
Ex = Ex.T
Ey = Ey.T

#Punto d)

fig1 = plt.figure(figsize=(8,5))
ax = fig1.add_subplot(1,1,1)

for i in range(1,len(x)):
    for j in range(1,len(y)):
        ax.quiver(x[i],y[j],Ex[i,j],Ey[i,j],color="b")
    
numero_puntos = 300
R = 2
O_x = 0
O_y = 0

theta = np.linspace(0,2*np.pi,numero_puntos+1)
x_c = R*np.cos(theta)+O_x
y_c = R*np.sin(theta)+O_y
ax.scatter(x_c,y_c,color="r",linewidth=0.5)
plt.xlabel("x[cm]")
plt.ylabel("y[cm]") 
        
   
        










