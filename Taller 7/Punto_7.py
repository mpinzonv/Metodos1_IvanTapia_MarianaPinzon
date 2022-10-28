# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:36:32 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import urllib


url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv'
p_data = urllib.request.urlopen(url)
a = pd.read_csv(p_data,sep=',')
x = np.array(a["x"])
y = np.array(a["y"])


