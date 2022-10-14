# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:42:26 2022

@author: mpinz
"""

import numpy as np

M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])

def Gauss_seidel(A,b,itmax=1000,error = 1e-10):
        x = [0,0,0]
        iteraciones = 0
        
        resid= np.linalg.norm(b-np.dot(A,x))
        
        while ( resid > error and iteraciones < itmax):
            x[0] = (1 + x[1] + x[2])/3
            x[1] = (3 + x[0] - x[2])/3
            x[2] = (7-2*x[0] -x[1])/4
            iteraciones += 1
            resid = np.linalg.norm(b-np.dot(A,x))
            
        return x,iteraciones,resid
    

x_sol,iteraciones,error=Gauss_seidel(M,b)

print("El resultado es:",x_sol)
print("El número de iteraciones es:",iteraciones)





