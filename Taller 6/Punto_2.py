# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:50:34 2022

@author: mpinz
"""

import numpy as np

class SolveLinSystem:
    def __init__(self,A,b):
        self.A = A
        self.b = b
        
#Por el método de Jacobi
    
    def Jacobi(self, itmax=1000, error = 1e-10):
        M,N = self.A.shape
        x = np.zeros(N)
        sumk = np.zeros_like(x)
        x = [13,20,-1]
        iteraciones = 0
    
        resid = np.linalg.norm(b - np.dot(A,x))
    
        while (resid > error and iteraciones < itmax):
        
            iteraciones += 1
        
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += A[i][j]*x[j]
                sumk[i] = sum_
          
            for i in range(M):
            
                if A[i,i] != 0:
                    x[i] = (b[i] - sumk[i])/A[i,i]
                else:
                    print("No posible")

            resid = np.linalg.norm(b - np.dot(A,x))
        
        return x,iteraciones,resid
    

#Por el método de Gauss-Seidel
    
    def Gauss_seidel(self, itmax=1000, error = 1e-10):
        x = [0,0,0]
        iteraciones = 0
        
        resid = np.linalg.norm(b - np.dot(A,x))
        
        while (resid > error and iteraciones < itmax):
            x[0] = (1 + x[1] + x[2])/3
            x[1] = (3 + x[0] - x[2])/3
            x[2] = (7-2*x[0] - x[1])/4
            iteraciones += 1
            resid = np.linalg.norm(b - np.dot(A,x))
            
        return x,iteraciones,resid
    
A = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b = np.array([1.,3.,7.])
sol = SolveLinSystem(A,b)

x_sol,iteraciones,error = sol.Jacobi()


print("1. Por el método de Jacobi")
print("El resultado es:",x_sol,", El número de interaciones es:",iteraciones)

print("2. Por el método de Gauss-Seidel se pueden mirar los resultados del punto 1 del taller")


