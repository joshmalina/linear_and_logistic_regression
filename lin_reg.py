import pandas as pd
import numpy as np
from scipy.misc import derivative
from pylab import *


df = pd.read_csv('wp_remove_null_2014.csv', header=0)

xs = df['wind_speed_mph']
ys = df['Value']

theta_0 = 0
theta_1 = 0

# hypothesis function
def hypo(x, theta_0, theta_1):
	return theta_0 + (theta_1 * x)

# cost function / squared error function
def cost_f(xs, ys, theta_0, theta_1):
	num_guesses = len(xs)

	if len(ys) != num_guesses:
		raise "This should not be the case"		

	sum = 0
	for x,y in zip(xs,ys):
		# the sum of all the errors squared
		sum += ((hypo(x, theta_0, theta_1) - y) ** 2)
	# divided in half and by the number of guesses, perhaps some kind of average cost, just to make the math easier 
	return sum / (2 * num_guesses)

# we will attempt to minimize the cost function until we get a line that reduces the errors as much as possible
# and by minimizing the cost function, we are really trying to find the right theta_0 and theta_1 that produces such a line

# we want to make the output of this function as small as possible for a given set of xs and ys
def cost_written_out(xs, ys, theta_0, theta_1):
	num_guesses = len(xs)
	if len(ys) != num_guesses:
		raise "This should not be the case"		
	sum = 0
	for x,y in zip(xs,ys):
		# the sum of all the errors squared
		sum = sum + (((theta_0 + (theta_1 * x)) - y) ** 2)
	# divided in half and by the number of guesses, perhaps some kind of average cost, just to make the math easier 
	return sum / (2 * num_guesses)

# print cost_written_out(xs, ys, theta_0, theta_1)

# print cost_f(xs, ys)

# print cost_written_out_only_theta1(-7, xs, ys)

# this algorithm takes a function of the kind f -> theta_0 -> ... theta_n
# and attempts to find values for theta_0, ... theta_1 such that f(theta_0, ... theta_1) is the least
# aka, the set of values for all thetas that returns the lowest value for the function
def gradient_descent(function_to_be_minimized): function_to_be_minimized

def f_with_xs_ys_built_in(theta_0, theta1):

	df = pd.read_csv('wp_remove_null_2014.csv', header=0)
	xs = df['wind_bearing_deg']
	ys = df['Value']

	num_guesses = len(xs)
	if len(ys) != num_guesses:
		raise "This should not be the case"		
	sum = 0
	for x,y in zip(xs,ys):
		# the sum of all the errors squared
		sum = sum + (((theta_0 + (theta_1 * x)) - y) ** 2)
	# divided in half and by the number of guesses, perhaps some kind of average cost, just to make the math easier 
	return sum / (2 * num_guesses)


def partial_derivative(func, var=0, point=[]):
    	args = point[:]    	
    	def wraps(x):
        	args[var] = x
        	return func(*args)
    	r = derivative(wraps, point[var], dx = 1e-6)
    	# print "deriv: "	
    	# print r
    	return r

# alpha is the size of the step downwards into trough (toggle for coarser or finer steps)
def gradient_descent_of_two_variables(f, alpha):

	# initialize thetas to zero
	theta_0 = 0
	theta_1 = 0

	# repeat until convergence
	for i in range(0, 200): 
		# update first parameter to slide down the slope toward a trough
		temp_theta_0 = theta_0 - (alpha * partial_derivative(f, 0, [theta_0, theta_1]))
		temp_theta_1 = theta_1 - (alpha * partial_derivative(f, 1, [theta_0, theta_1]))
		theta_0 = temp_theta_0
		theta_1 = temp_theta_1

	return theta_0, theta_1

coefs = gradient_descent_of_two_variables(f_with_xs_ys_built_in, 1.0)
print coefs

def predict_y_give_x(x):	
	return coefs[0] + coefs[1] * x

# print predict_y_give_x(4.96)

import matplotlib.pyplot as plt  

def graph(formula, x_range, xs, ys):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.figure(1, figsize = (6,4) )

    plt.plot(x, y, 'b-', label='regression line')
    plt.plot(xs,ys,'ro', label='data')

    plt.savefig('result4.png')
    plt.show()  

graph(predict_y_give_x, range(0, 360), xs, ys)

# import matplotlib.pyplot as plt

# # read data from file
# xdata, ydata = np.loadtxt('wavePulseData.txt', unpack=True)

# # create x and y arrays for theory
# x = np.linspace(-10., 10., 200)
# y = np.sin(x) * np.exp(-(x/5.0)**2)

# # create plot
# plt.figure(1, figsize = (6,4) )
# plt.plot(x, y, 'b-', label='theory')
# plt.plot(xdata, ydata, 'ro', label="data")
# plt.xlabel('x')
# plt.ylabel('transverse displacement')
# plt.legend(loc='upper right')
# plt.axhline(color = 'gray', zorder=-1)
# plt.axvline(color = 'gray', zorder=-1)

# # save plot to file
# plt.savefig('WavyPulse.pdf')

# # display plot on screen
# plt.show()

