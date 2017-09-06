# !/usr/bin/env/ python

"""

SYPNOSIS

    Pairwise Computation

DESCRIPTION

    Given a vector x of length m, and a vector of y of length n, compute m x n: A and B such that
    A(i, j) = x(i) + y(j) and B(i,j) = x(i) . y(j)

"""


import numpy as np

rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
m = input("key in length m: ")
n = input("key in length n: ")

x = np.random.rand(m, 1)
y = np.random.rand(n, 1)

A = x[:, np.newaxis] + y[np.newaxis, :]
print "A = "
print A

B = x[:, np.newaxis] * y [np.newaxis, :]
print "B = "
print B

