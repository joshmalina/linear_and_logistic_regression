'''
	Multivariate linear regression using batch vectors. Code inspired by the coursera course, machine learning with Andrew Ng. 
	This program takes any number of parameters, including a single parameter, and outputs a projected pollution value. The linear
    model makes assumptions about the normality of the data, which may be violated, because we have outliers. For the given data set,
    we model the effect of wind speed on pollution value as something like y = -7.34x + 135.93. Not the best model, of course, since 
    we are only evaluating pollution based on one predictor. Also, not clear that the relationship between pollution and wind speed is
    strictly linear
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

# # scale down air pressure
# xs[:, 4] = dot(xs[:, 4], .1)
# #scale up relative humidty
# xs[:, 3] = dot(xs[:, 3], 10)

# feature scaling

# Initialize theta parameters according to how many features we are evaluating
theta = zeros(shape=(keep.shape[1], 1))

# def cost_f(xs, ys, theta):

#     # build a batch of all predictions
#     all_results = xs.dot(theta).T

#     # build a batch of all corresponding errors
#     all_errors = (all_results - ys) ** 2

#     # total error
#     sum_err = sum(all_errors)
 
#  	# dividing by two "makes the math easier"
#  	# dividing by length gives us some kind of average error
#     return sum_err / 2 / len(ys)

when_stop = 1500
# how big of each step
alpha = 0.01

# gradient descent algorithm for coming up with the right thetas
def theta_maker(xs, ys, theta, step_size, when_stop):
    
    num_points = len(ys)
    num_thetas = len(theta)

    # stop at some arbitrary point when we think we've reached
    # the minimum
    for i in range(when_stop):

 		# build a vector of predictions for every x given theta
        # starts at theta == all 0s
        pred = xs.dot(theta).T

        # build a vector of errors for every prediction
        # initial errors should distance of points from 0
        e = pred - ys

        # for every theta term
        for j in range(0, num_thetas):

            # multiply error by corresponding x value           
            e_at_given_x = e * xs[:, j]

            # update theta, i.e. step down if positive error / step up if neg error
            theta[j] -= step_size * sum(e_at_given_x) / num_points

    return theta

our_theta = theta_maker(xs, ys, theta, alpha, when_stop)

def hypo(x):
    return x.dot(our_theta)[0]


