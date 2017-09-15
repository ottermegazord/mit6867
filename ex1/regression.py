
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

def getData(csvfile):
    csv = np.genfromtxt(csvfile, delimiter=",")
    csv = csv[1:,1:]
    return csv

def mean(values):
    return sum(values)/float(len(values))

def var(values, mean):
    return sum([(x-mean)**2 for x in values])

def cov(x, mean_x, y, mean_y):
    covariance = 0.0
    for i in range(len(x)):
        covariance += (x[i]- mean_x) * (y[i]-mean_y)
    return covariance

def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = cov(x, x_mean, y, y_mean) / var(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions


# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return math.sqrt(mean_error)


# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset, algorithm):
    test_set = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
    predicted = algorithm(dataset, test_set)
    print(predicted)
    actual = [row[-1] for row in dataset]
    rmse = rmse_metric(actual, predicted)
    return rmse

#create data frame to store log values
data = getData('Advertising.csv')
x = data[:,0]
y = data[:,3]
plt.scatter(x, y)
mean_x, mean_y = mean(x), mean(y)
var_x, var_y = var(x, mean_x), var(y, mean_y)
covar = cov(x, mean_x, y, mean_y)
print mean_x, mean_y, var_x, var_y, covar
b1, b0 = coefficients(data)
print b1, b0
rmse = evaluate_algorithm(data, simple_linear_regression)
print rmse
plt.axis([0, 300, 0, 25])
plt.show()