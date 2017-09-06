# !/usr/bin/env/ python

"""

SYPNOSIS

    Pairwise Computation

DESCRIPTION

    Given a d x m matrix X, and a d x n Matrix Y, compute an m x n matrix D, such that
    D(i, j) = ||x^i - y^j|| where x^i is the i-th column of X, and y^i is the j-th
    column of Y



"""


import numpy as np
import scipy.linalg as sp

rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
d = input("key in d: ")
m = input("key in m: ")
n = input("key in n: ")
X = np.random.rand(d, m)
Y = np.random.rand(d, n)

print("Generating x, y...")
print(X)
print(Y)

print("Calculating euclidean pairwise distances...")
print("D = ")

# create zero Matrix D
D = np.zeros((m,n))
# sort row first, then column


for j in range(n):
    for i in range(m):
        # D(i, j) = || x^i - y^j ||
        D[i, j] = sp.norm(X[:,i] - Y[:,j])

print D
