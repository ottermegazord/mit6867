#!/usr/bin/env/ python

"""
SYNOPSIS

    2-D Gaussian

DESCRIPTION

    Generate 1000 points froma  2D Gaussian distribution with mean u = [4,2] and
    covariance [[1,2],[1.5,3]]

    Plot the points so obtained, and estimate their mean and covariance from the data.
    Find the eigenvectors of the covariance matrix and plot them centered at the sample
    mean.

STATUS
    plot eigenvectors to graph

"""

import numpy as np
import matplotlib.pyplot as plt

#Draw random samples from a multivariate normal distribution with parameters u and c

mean = [4,2]
cov = [[1,1.5] , [1.5,3]]
n = 1000

# Generate Gaussian points
R = np.random.multivariate_normal(mean, cov, n)
plt.scatter(R[:,0], R[:,1], marker='.')
#plt.show()

#Estimate sample mean of Gaussian distribution
mu_hat = np.mean(R, axis=0) # axis -> axis or axes along which the means are computed
print("Sample mean is: ")
print(mu_hat)
print('\n')

# Centering R at sample mean
mu_sample_newaxis = mu_hat[np.newaxis, :]  # each row now contains 2 x 1 matrix, as opposed to one dimensional array
                                              # length 3
# Normalization against mean
R_0 = R - mu_sample_newaxis
cov_hat = np.dot(R_0.T, R_0) # formula of covariance R.T dot R
#cov_hat = np.cov(R_0)

#Generate eigenvectors of the covariance matrix

w, v = np.linalg.eig(cov_hat) # w => ei
print('Eigenvalue: ')
print w
print('Eigenvectors: ')
print v

# Show eigenvectors on graph
plt.arrow(mu_hat[0], mu_hat[1], v[0,0], v[1,0], shape='full', lw=4, head_width=.05)
plt.arrow(mu_hat[0], mu_hat[1], v[1,0], v[1,1], shape='full', lw=4, head_width=.05)
plt.scatter(R[:,0], R[:,1], marker='.')
plt.show()

