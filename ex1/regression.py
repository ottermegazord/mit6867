
#!/usr/bin/env/ python

"""
SYNOPSIS

    Linear regression model

DESCRIPTION

    Implementation of regression model from scratch

"""


import pandas as pd
import matplotlib.pyplot as plt
import csv

def getData(fileName):

    csv = pd.read_csv(fileName)
    return csv

df = getData('Advertising.csv')
ax = plt.scatter(df['TV'], df['Sales'])
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()
