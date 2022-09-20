import numpy as np
import matplotlib.pyplot as plt
fx=lambda x:np.exp(-x**2)
ddfx=lambda x:( (-2)*((-2)*(x**2)*np.exp(-(x**2))+np.exp(-(x**2)))                  )
n=int(np.ceil((np.sqrt(ddfx(1)/(12*0.005)))))
x=np.linspace(0, 1,num=n+1)
h,area=1/n,0
valores_f=(fx(x))
error=abs(ddfx(1)/(12*n**2))
for i in range(n):
    area+=h*((valores_f[i]+valores_f[i+1])/2)
print(f'La integral de la funcion con un error de {error} es: {area}')
