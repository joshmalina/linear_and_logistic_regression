'''
    Multivariate linear regression using batch vectors. Code inspired by the
    coursera course, machine learning with Andrew Ng. This program takes any
    number of parameters, including a single parameter, and outputs a projected
    pollution value. The linear model makes assumptions about the normality of
    the data, which may be violated, because we have outliers and
    collinearility.
'''

__author__ = 'Josh Malina'

import pandas as pd
import numpy as np
from pylab import *
import sys
sys.path.insert(0, '../helpers')
import helpers
sys.path.insert(0, '../interfaces')
import i_multivariate_linear_regression as interface

class MultivariteLinearRegression(interface.IMultivariateLinearRegression):

    def __init__(self):

        _alpha = 0.01
        _iters = 2500

        _xs, _ys = self.get_data()

        self._xs, self._ys = _xs, _ys

        #print self._xs[0]
        # print _xs.dtype.names

        self._theta = self.theta_maker(_xs, _ys, _alpha, _iters)

    def predict(self, x_vector):
        return x_vector.dot(self._theta)[0]

    def get_data(self):

        x_param_list = ['wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']

        xs, ys = helpers.Helpers.get_data_2('../Data/', 'wp_remove_null_2014.csv', 'Value', x_param_list, True)

        return xs, ys

    def get_cost(self):

        # build a batch of all predictions
        all_results = self._xs.dot(self._theta).T

        # build a batch of all corresponding errors
        all_errors = (all_results - self._ys) ** 2

        # total error
        sum_err = sum(all_errors)
     
        # dividing by two "makes the math easier"
        # dividing by length gives us some kind of average error
        return sum_err / 2 / len(self._ys)

    # gradient descent algorithm for coming up with the right thetas
    def theta_maker(self, xs, ys, step_size, when_stop):

        # initialize theta parameters according to how many features we are evaluating
        theta = zeros(shape=(xs.shape[1], 1))
        
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

            # print cost_f(xs, ys, theta)

        return theta    


g = MultivariteLinearRegression()
# print g._theta
# print g.get_cost()
# print g.predict(g.get_data()[0][0])