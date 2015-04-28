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
import interfaces.regression_abstract as _abstract
import helpers.helpers as _helpers


class MultivariateLinearRegression(_abstract.RegressionAbstract):

    def __init__(self):
        self.alpha = 0.01
        # _iters = 1500
        # _xs, _ys = self.get_data()
        # self._theta = self.theta_maker(_xs, _ys, _alpha, _iters)

    # def predict(self, x_vector):
        # return x_vector.dot(self._theta)[0]

    def retrieve_training_set(self):
        x_input_variables = x_param_list = ['wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']
        xs, ys = _helpers.Helpers.get_binary_training_data_from_csv('data/wp_remove_null_2014.csv',
                                                                    x_input_variables,
                                                                    y_column_name='value',
                                                                    scale=True,
                                                                    omit_header=True)
        return xs, ys

    def train_algorithm(self, xs, ys, n):
        if n is None:
            n = 500000

        num_points = len(ys)
        num_thetas = len(self.theta)

        # stop at some arbitrary point when we think we've reached
        # the minimum
        for i in range(n):

            # build a vector of predictions for every x given theta
            # starts at theta == all 0s
            pred = xs.dot(self.theta).T

            # build a vector of errors for every prediction
            # initial errors should distance of points from 0
            e = pred - ys

            # for every theta term
            for j in range(0, num_thetas):

                # multiply error by corresponding x value
                e_at_given_x = e * xs[:, j]

                # update theta, i.e. step down if positive error / step up if neg error
                self.theta[j] -= self.alpha * sum(e_at_given_x) / num_points

            # print cost_f(xs, ys, theta)

        return self.theta