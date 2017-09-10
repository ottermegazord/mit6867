#!/usr/bin/env/ python

"""
SYNOPSIS

    2-D Gaussian

DESCRIPTION

    Generate 1000 pointw froma  2D Gaussian distribution with mean u = [4,2] and
    covariance [[1,2],[1.5,3]]

STATUS
    print int matplotlib.pyplot

"""

import numpy as np
import matplotlib.pyplot as plt

#generate Guassian distrubtion from parameters given

u = [4,2]
c = [[1,1.5] , [1.5,3]]

R = np.random.multivariate_normal(u, c, 1000)
#R = np.random.multivariate_normal([4, 2], [[1, 1.5], [1.5,3]], 1000)
print (R)
plt.plot(*(zip(*R)),marker='.', ls = '')
plt.show()
