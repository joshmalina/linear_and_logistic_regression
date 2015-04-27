__author__ = 'Jorge Cotillo'

import helpers.helpers as _helpers
import interfaces.regression_abstract as abstract
import numpy as np


class BinaryLogisticRegression(abstract.RegressionAbstract):

    def __init__(self, X, y):
        self.alpha = 0.01
        self.y = y
        self.X = X
        self.theta = np.matrix(np.zeros(X.shape[1])).T

    def retrieve_training_set(self):
        x_input_variables = ['wind_speed_mph']
        xs, ys = _helpers.Helpers.get_binary_training_data_from_csv('data/binary_training_set.csv',
                                                                    x_input_variables,
                                                                    'polluted')
        return xs, ys

    def get_cost(self, xs, ys):
        prob = self.set_hypothesis(xs * self.theta)
        cost = ys.T * np.log(prob) + (1 - ys).T * np.log(1 - prob)
        # final cost equation -1/m sum(cost)
        return float(-(1.0 / len(xs) * cost))

    def train_algorithm(self, xs, ys, n):
        # set number of iterations
        """

        :type self: object
        """
        if n is None:
            n = 5000

        for i in range(n):
            self.theta = self.theta + self.alpha * self.get_cost(xs, ys)
        return self.theta

    def set_hypothesis(self, param1):
        return self.__sigmoid_function(param1)

    @staticmethod
    def __set_hypothesis_intern(self, param1, param2, param3):
        return 3.0

    def get_gradient_descent(self):
        return self.get_gradient_descent_intern(1, 2, 3)

    @staticmethod
    def __get_gradient_descent_intern(self, param1, param2, param3):
        return 5.0

    def __sigmoid_function(self, z):
        return 1.0 / (1 + np.exp(-z))

    def sigmoid(self, z):
        return 1.0/(1 + np.exp(-z))

    def log_likelihood(self, theta):
        prob = self.sigmoid(self.X * theta)
        ll = self.y.T * np.log(prob) + (1 - self.y).T * np.log(1 - prob)
        return float(ll)

    def gradient(self, theta):
        return self.X.T * (self.y - self.sigmoid(self.X * theta))

    def hessian(self, theta):
        pass

    def error(self, theta):
        pass

    def train(self, alpha=0.001, n=1000):
        for i in range(n):
            self.theta = self.theta + alpha * self.gradient(self.theta)
        return self.theta

    def summary(self):
        pass

    def classify(self, x):
        pass

    def positive_prob(self, x):
        pass

