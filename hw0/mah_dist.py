#!/usr/bin/env/ python

"""
SYNOPSIS

    Compute Mahalabonis Distances

DESCRIPTION

    Given a center vector c, a covariance matrix S, and a set of n vectors as columns in matrix X,
    compute the distances of each column in X to c using this formula:

    D(i) = (x^i - c)^T*S^-1*(x^i-c)

    where D is a row vector of length n

STATUS
    IndexError: too many indices Line 33

"""

import numpy as np

# generate numpy arrays of zeros for D

rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
n = input("key in n of C: ")
c= input("key in c: ")
T= input("key in T: ")
D = np.zeros(n) # row vector
X = np.zeros(n)
S= np.random.rand(n) # covariance matrix

for i in range(n):
    Z = X[:, i] - c
    D[i] = np.dot(np.dot(Z.T, np.linalg.inv(S)), Z)

print("Generating D...")
print(D)
print(X)
