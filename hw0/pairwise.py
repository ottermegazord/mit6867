# !/usr/bin/env/ python

"""

SYPNOSIS

    Pairwise Computation

DESCRIPTION

    Given a vector x of length m, and a vector of y of length n, compute m x n: A and B such that
    A(i, j) = x(i) + y(j) and B(i,j) = x(i) . y(j)

"""


import numpy as np
from sklearn.metrics import pairwise_distances

rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
x = np.random.rand(2, 1)
y = np.random.rand(2, 1)

print("Generating x, y...")
print(x)
print(y)

print("Calculating pairwise distances...")
print("A = ")
A = pairwise_distances(x, y)
print A
B = np.linalg.norm(A)
print("B = ")
print(B)
