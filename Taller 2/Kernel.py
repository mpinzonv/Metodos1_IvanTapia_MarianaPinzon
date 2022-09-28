# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 17:23:21 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,num=401)
ecuation=lambda x: 1/np.sqrt(1+np.exp(-x**2))
h=0.05
M=np.array([1,0,-1])
def convolute(kernel,f,x):
    fx_conv=np.ones(len(x))
    for n in range(1,len(x)-1):
        valor_conv=0
        for m in range(-1,len(kernel)-1):
            valor_conv+=kernel[m+1]*f(x[n-m])
        fx_conv[n]=valor_conv
    return(fx_conv)

convolucion=(1/(2*h))*convolute(M,ecuation,x)
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(1,1,1)
ax.scatter(x[1:-1],convolucion[1:-1])
ax.set_title('Deriva usando Kernel de convolución')
ax.set_xlabel('valores de X')
ax.set_ylabel("f'(x)")
plt.show()

