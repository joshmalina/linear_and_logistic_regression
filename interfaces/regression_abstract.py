__author__ = 'Jorge Cotillo'

from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

class RegressionAbstract:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._alpha = 1.0
        self._theta = []

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    @abstractmethod
    def alpha(self, val):
        self._alpha = val

    @property
    def theta(self):
        return self._theta

    @theta.setter
    @abstractmethod
    def theta(self, val):
        self._theta = val

    def predict(self, iterations=1000):
        # get initial x and y matrix
        xs, ys = self.retrieve_training_set()

        # now that we know the length of the sample data (observations) let's proceed to initialize theta matrix
        self.theta_maker(xs)

        # call train algorithm in order to receive theta
        new_theta = self.train_algorithm(xs, ys, iterations)

        return new_theta

    @abstractmethod
    def retrieve_training_set(self):
        pass

    @abstractmethod
    def train_algorithm(self, xs, ys, n=None):
        pass

    @abstractmethod
    def theta_maker(self):
        pass
