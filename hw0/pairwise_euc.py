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
from sklearn.metrics.pairwise import euclidean_distances

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
A = euclidean_distances(X, Y)
print A
