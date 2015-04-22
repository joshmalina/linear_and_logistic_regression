# one way of minimizing the cost function; a more scalabale method would use linear algebra

# this code inspired by the coursera course, machine learning with Andrew Ng


import pandas as pd
import numpy as np
from scipy.misc import derivative
from pylab import *

df = pd.read_csv('wp_remove_null_2014.csv', header=0)

xs = df['wind_speed_mph']
ys = df['Value']

theta_0 = 0
theta_1 = 0

ALPHA = 1.0
STOP_CONVERGING_AT = 20

# hypothesis function
def hypo(x, theta_0, theta_1):
	return theta_0 + (theta_1 * x)

# cost function
def cost_f(theta_0, theta1, xs, ys):
	num_guesses = len(xs)
	if len(ys) != num_guesses:
		raise "This should not be the case"		
	sum = 0
	for x,y in zip(xs,ys):
		# the sum of all the errors squared
		sum = sum + ((((hypo(x,theta_0,theta_1)) - y) ** 2))
	# divided in half and by the number of guesses, perhaps some kind of average cost, just to make the math easier 
	return sum / (2 * num_guesses)

# from http://stackoverflow.com/questions/20708038/scipy-misc-derivative-for-mutiple-argument-function
def partial_derivative(func, var=0, point=[]):
	args = point[:]    

	def wraps(x):
	   	args[var] = x
	   	return func(*args)

	return derivative(wraps, point[var], dx = 1e-6)

# alpha is the size of the step downwards into trough (toggle for coarser or finer steps)
def gradient_descent_of_two_variables(f, alpha, xs, ys, stop_converging):

	# initialize thetas to zero
	theta_0 = 0
	theta_1 = 0

	# repeat until convergence
	for i in range(0, stop_converging): 
		# update first parameter to slide down the slope toward a trough
		temp_theta_0 = theta_0 - (alpha * partial_derivative(f, 0, [theta_0, theta_1, xs, ys]))
		temp_theta_1 = theta_1 - (alpha * partial_derivative(f, 1, [theta_0, theta_1, xs, ys]))
		theta_0 = temp_theta_0
		theta_1 = temp_theta_1

	coefs = theta_0, theta_1
	return coefs

coefs = gradient_descent_of_two_variables(cost_f, ALPHA, xs, ys, STOP_CONVERGING_AT)

def predict_y_give_x(x):	
	return coefs[0] + coefs[1] * x




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



