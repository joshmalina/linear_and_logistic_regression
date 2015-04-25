'''
	A first stab at univariate linear regression using an iterative process; not the most scalable (that would take the form
	of something with more linear algebra). Code inspired by the coursera course, machine learning with Andrew Ng. This program
	takes a wind speed and outputs a projected pollution value. The linear model makes assumptions about the normality of the 
	data, which may be violated, because we have outliers. For the given data set, we model the effect of wind speed on pollution
	value as something like y = 97x + 0. Not the best model, of course, since we are only evaluating pollution based on one predictor.
'''

import pandas as pd
import numpy as np
from scipy.misc import derivative
from pylab import *

df = pd.read_csv('wp_remove_null_2014.csv', header=0)

xs = df['visibility_miles_max_10']
ys = df['Value']

# hypothesis function
def hypo(x, theta_0, theta_1):
	return theta_0 + (theta_1 * x)

# cost function
def cost_f(theta_0, theta1, xs, ys):

	sum = 0
	for x,y in zip(xs,ys):
		# the sum of all the errors squared
		sum += (((theta_0 + (theta_1 * x)) - y) ** 2) 
	# divided in half and by the number of guesses
	return sum / (2 * num_guesses)

# alpha is the size of the step downwards into trough (toggle for coarser or finer steps)
def gradient_descent_of_two_variables(alpha, xs, ys, stop_converging, org_theta0, org_theta1):

	temp_theta_0 = 0
	temp_theta_1 = 0

	# repeat until convergence
	for i in range(0, stop_converging): 
		# calculate the error at each point
		for x,y in zip(xs,ys):
			temp_theta_0 += (((y - (org_theta0*x + org_theta1)) / len(xs)) * alpha)
			temp_theta_1 += (((y - (org_theta0*x + org_theta1)) * x / len(xs)) * alpha)

		org_theta0 = temp_theta_0
		org_theta1 = temp_theta_1

	print "my coeffs:"
	print org_theta0, org_theta1
	return org_theta0, org_theta1

a = gradient_descent_of_two_variables(0.1, xs, ys, 100, 0, 0)

def q(theta0, theta1, x):
	return (theta0 * x) + theta1

def gradient_descent_runner(xs, ys, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, xs, ys, learning_rate)
    return [b, m]

aaa = gradient_descent_runner(xs, ys, 0, 0, .1, 100)

print aaa[0] + aaa[1] * 4.96




# print hypo(10, coefs[0], coefs[1])




#print predict_y_give_x(4.96)

# import matplotlib.pyplot as plt  

# def graph(formula, x_range, xs, ys):  
#     x = np.array(x_range)  
#     y = formula(x)  # <- note now we're calling the function 'formula' with x
#     plt.figure(1, figsize = (6,4) )

#     plt.plot(x, y, 'b-', label='regression line')
#     plt.plot(xs,ys,'ro', label='data')

#     plt.savefig('result4.png')
#     plt.show()  

# graph(predict_y_give_x, range(0, 360), xs, ys)



