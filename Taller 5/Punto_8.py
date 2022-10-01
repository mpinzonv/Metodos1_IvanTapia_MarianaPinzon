# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:25:56 2022

@author: mpinz
"""

import numpy as np
import random

def distribucion_beta(x,alpha,betha):
    return (x**(alpha-1)*(1-x)**(betha-1))/(np.math.gamma(alpha)*np.math.gamma(alpha)/np.math.gamma(alpha+betha))

N = 0
alpha = 1
betha = 10000

def aceptacion_rechazo(N,alpha,betha):
    x = np.linspace(N,alpha,betha)
    y = distribucion_beta(x,alpha,betha)
    y_max = np.max(y)
    
    x_acept = []
    y_acept = []
    s = 0
    
    while len(x_acept) < N:
        x_aleatorio = random.uniform(0,1)
        y_aleatorio = random.uniform(0,y_max)
        
        if y_aleatorio < distribucion_beta(x_aleatorio,alpha,betha):
            x_acept.append(x_aleatorio)
            y_acept.append(y_aleatorio)
            s += 1
    return (s/N), x_acept, y_acept


#Para f(x; 2,4)

def integral_aceptacion_rechazo(N,alpha,betha):
    N = 10000
    alpha = 2
    betha = 4
    s,x,y = aceptacion_rechazo(N,alpha,betha)
    return s
    
print ("El área bajo la curva es:",integral_aceptacion_rechazo(N,alpha,betha))
    