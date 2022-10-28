# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:36:45 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#Parte a) Mínimos cuadrados matriciales

m_U = np.array([[3,1,0,1],[1,2,1,1],[-1,0,2,-1]])
b = np.array([-3,-3,8,9])
A = m_U.T

U_b = np.dot(m_U,b)
U_A = np.dot(m_U,A)

respuesta = np.linalg.solve(U_A,U_b)
w1,w2,w3,w4 = np.dot(A,respuesta)
w4 = np.abs(w4)
print("La proyección ortogonal para la parte a) es:",(w1,w2,w3,w4))

#Parte b) Proceso de Grand-Schmidt

k,l = m_U.shape
M = np.zeros((k,l))

M[0]=m_U[0]
for i in range(1,k):
    M[i]=m_U[i]
    for j in range(i):
        M[i]=M[i]-((np.dot(m_U[i],M[j])/np.dot(M[j],M[j]))*M[j])
        
for i in range(k):
    norm = np.sqrt(np.dot(M[i],M[i]))
    M[i] /= norm
    
Mb = np.dot(M,b)
MMt = np.dot(M,M.T)
respuesta_2 = np.linalg.solve(MMt,Mb)
u1,u2,u3,u4 = np.dot(M.T,respuesta_2)
u4 = np.abs(u4)
print("La proyección ortogonal para la parte b) es:",(u1,u2,u3,u4))