# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:07:11 2022

@author: Administrator
"""

import numpy as np; np.random.seed(0)

import seaborn as sns; sns.set_theme()

uniform_data = np.array([[1, 2, 3, 4, 5,6],[4, 6,7, 8, 2, 5],[7, 5, 2, 7, 4, 9],[5, 6, 8,5, 3, 1]],np.int32)


ax = sns.heatmap(uniform_data, vmin=0, vmax=10)


