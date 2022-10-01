# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:26:35 2022

@author: mpinz
"""



import numpy as np
import random 

def funcion_1(f,a,b,N):
    I = 0
    for i in range(N):
        x_1 = random.uniform(a,b)
        x_2 = random.uniform(a,b)
        x_3 = random.uniform(a,b)
        x_4 = random.uniform(a,b)
        x_5 = random.uniform(a,b)
        x_6 = random.uniform(a,b)
        x_7 = random.uniform(a,b)
        x_8 = random.uniform(a,b)
        I += f(x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8)
    return (b-a)*I/N

def funcion_2(x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8):
    return pow(2,-7)*(x_1+x_2+x_3+x_4+x_5+x_6+x_7+x_8)**2

a = 0
b = 1
N = 1000000

integral = funcion_1(funcion_2,a,b,N)
dato_valor = 25/192

#La anterior división es igual a 0,1302

resultado_integral = integral
resultado_integral = round(integral,4)

print("La integral es:",resultado_integral)










        
        
        