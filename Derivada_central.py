# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 17:21:30 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,num=401)
ecuation=lambda x: 1/np.sqrt(1+np.exp(-x**2))
derivada_real=lambda x: (np.exp(-x**2)*x)/((1+np.exp(-x**2))**(3/2))

def derivada_central(x,f,h=0.05):
    return (f(x+h)-f(x-h))/(2*h)

derivada=derivada_central(x,ecuation)
fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax1 = fig.add_subplot(1,2,2)
ax.scatter(x,derivada)
ax1.scatter(x,abs(derivada_real(x)-derivada))
ax.set_title('Derivada central')
ax1.set_title('Error')
ax.set_xlabel('X')
ax.set_ylabel("f'(X)")
ax1.set_xlabel('X')
ax1.set_ylabel('Error')
plt.show()