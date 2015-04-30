import sys
sys.path.insert(0, '../helpers')
sys.path.insert(0, '../interfaces')
import helpers as _helpers
import regression_abstract as _abstract
import numpy as np
from pylab import *

class MultipleVariableLinearRegression(_abstract.RegressionAbstract):

    def __init__(self):
        self.alpha = 0.01
        xs, ys = self.retrieve_training_set()
        self.theta = self.train_algorithm(xs, ys, 1500)

    def retrieve_training_set(self):
    	x_param_list = ['wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']
    	xs,ys = _helpers.Helpers.get_data_2('../Data/', 'wp_remove_null_2014.csv', 'Value', x_param_list, True)        
        return xs,ys

    def train_algorithm(self, xs, ys, n):

		# initialize theta parameters according to how many features we are evaluating
		theta = zeros(shape=(xs.shape[1], 1))

		num_points = len(ys)
		num_thetas = len(theta)

		# stop at some arbitrary point when we think we've reached
		# the minimum
		for i in range(n):

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
	            theta[j] -= 1 * sum(e_at_given_x) / num_points

		return theta

    def predict(self, x_vector):
    	return x_vector.dot(self.theta)[0]

x = MultipleVariableLinearRegression()

print x.theta
print x.alpha
print x.predict(x.retrieve_training_set()[0][0])
