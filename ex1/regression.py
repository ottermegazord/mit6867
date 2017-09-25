
#!/usr/bin/env/ python

"""
SYNOPSIS

    Linear regression model

DESCRIPTION

    Implementation of regression model from scratch
    Goal:
    find w (weight parameters/coefficients) that minimizes squared loss

"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import math
import pandas as pd

def getData(csvfile):
    csv = pd.read_csv(csvfile, delimiter=",")
    csv.insert(0, 'Ones', 1)
    csv.drop(csv.columns[0], axis=1)
    data = csv.loc[:,'TV': 'Sales':1]
    data.insert(0, 'Ones', 1)
    return data


#create data frame to store log values
data = getData('Advertising.csv')
cols = data.shape[1]

X = np.array(data.iloc[:, 0:4])
y = np.array(data.iloc[:, 4])
print y

xTx = X.T.dot(X)
XtX = np.linalg.inv(xTx)
XtX_xT = XtX.dot(X.T)
theta = XtX_xT.dot(y)
print theta

plt.plot(X[:,1], theta[1]*X[:,1] + theta[0])
plt.scatter(X[:,1], y)
plt.axis([0, 300, 0, 25])
plt.show()