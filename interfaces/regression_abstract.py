__author__ = 'Jorge Cotillo'

from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

class RegressionAbstract:
    __metaclass__ = ABCMeta

    _alpha = 1.0
    _theta = []

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

    def predict(self, x_vector=None):
        # get initial x and y matrix
        xs, ys = self.retrieve_training_set()

        # now that we know the length of the sample data (observations) let's proceed to initialize theta matrix
        self.theta = np.matrix(np.zeros(xs.shape[1])).T

        # call train algorithm in order to receive theta
        new_theta = self.train_algorithm(xs, ys, 5000)

        # retrieve cost (log likelihood)
        # cost = self.get_cost(xs, ys)

        return new_theta

    @abstractmethod
    def retrieve_training_set(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def train_algorithm(self, xs, ys, n=None):
        pass

    @abstractmethod
    def get_gradient_descent(self, xs=None, ys=None, step_size=None, when_stop=None):
        pass

    @abstractmethod
    def set_hypothesis(self):
        pass
