#!/usr/bin/env/ python

"""
SYNOPSIS

    Largest of off-diagonal element

DESCRIPTION

    Find largest off-diagonal element in nxn matrix

"""

import numpy as np


rand_seed = input("Key in random seed: ")
np.random.seed(rand_seed)
n = input("key in n of C: ")
C = np.random.rand(n,n)

print("Generating C...")
print(C)

#Return matrices with ones along with the nth diagonal
diag_matrix = np.eye(n)
print(diag_matrix)

#Indices of off-diagonal elements
condition = 1 - diag_matrix

#Extract off-diagonal elements
off_diag = np.extract(condition, C)

#Print largest off-diagonal element in off_diag
max_element = off_diag.max()
print("Largest off-diagonal element of C is %s" % max_element)