#!/usr/bin/env/ python

"""
SYNOPSIS

    Regularization

DESCRIPTION

    Given an n x n matrix C, add a scalar a to each diagonal entry of C

"""

import numpy as np


rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
x = input("key in axis 0 of C: ")
y = input("key in axis 1 of C: ")
C= np.random.rand(x,y)

print("Generating C...")
print(C)

a = input("Key in scalar for regularization: ")
C[np.diag_indices_from(C)] += a
print(C)
