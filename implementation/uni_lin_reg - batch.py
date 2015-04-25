'''
	A first stab at univariate linear regression using batch vectors. Code inspired by the coursera course, machine learning with Andrew Ng. 
	This program takes a wind speed and outputs a projected pollution value. The linear model makes assumptions about the normality of the 
	data, which may be violated, because we have outliers. For the given data set, we model the effect of wind speed on pollution
	value as something like y = -7.34x + 135.93. Not the best model, of course, since we are only evaluating pollution based on one predictor.
	Also, not clear that the relationship between pollution and wind speed is strictly linear
'''

import pandas as pd
import numpy as np
from pylab import *

df = pd.read_csv('wp_remove_null_2014.csv', header=0)

# number of training samples

ys = df['Value']
ys = np.array(ys)
keep = df[['wind_speed_mph']]
keep.insert(0, 'x0', ([1.0] * len(df)))
xs = np.array(keep)

# Initialize theta parameters
theta = zeros(shape=(keep.shape[1], 1))

# Some gradient descent settings
when_stop = 1500
alpha = 0.01

def cost_f(xs, ys, theta):

    # build a batch of all predictions
    all_results = xs.dot(theta).T

    # build a batch of all corresponding errors
    all_errors = (all_results - ys) ** 2

    # total error
    sum_err = sum(all_errors)
 
 	# dividing by two "makes the math easier"
 	# dividing by length gives us some kind of average error
    return sum_err / 2 / len(ys)

def gradient_descent(xs, ys, theta, alpha, when_stop):
    
    m = ys.size

    # stop at some arbitrary point when we think we've reached
    # the local minimum
    for i in range(when_stop):
 
 		# again, get all predictions
        pred = xs.dot(theta).T

 		# get vector of all errors for theta0
 		# don't need to multiply becase x[0] = 1
        errors_theta_0 = (pred - ys) * xs[:, 0]
        #print errors_theta_0

        # build vector of all errors for theta1
        errors_theta_1 = (pred - ys) * xs[:, 1]
 
 		# for as many iterations, decrease/increase theta according to
 		# the slope of the cost function

        theta[0] -= alpha * (1.0 / m) * sum(errors_theta_0)

        theta[1] -= alpha * (1.0 / m) * sum(errors_theta_1)
 
    return theta

our_theta = gradient_descent(xs, ys, theta, alpha, when_stop)
print our_theta

def hypo(x):	
	return x.dot(our_theta)[0]

print hypo(xs[0])

