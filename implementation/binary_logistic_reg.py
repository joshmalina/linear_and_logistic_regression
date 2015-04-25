__author__ = 'Jorge Cotillo'

import entity.training_set_entity as _tse
import helpers.helpers as _helpers
import interfaces.i_logistic_regression as interface


class BinaryLogisticRegression(interface.ILogisticRegression):

    _alpha = 1.0

    def __init__(self, alpha):
        if alpha is not None:
            _alpha = alpha

    def predict(self):
        training_set = self.retrieve_training_set()
        return 1

    def retrieve_training_set(self):
        x_input_variables = ['wind_speed_mph']
        training_set_list = _helpers.Helpers.get_binary_training_data_from_csv('binary_value.csv',
                                                                               x_input_variables,
                                                                               'binary')
        return training_set_list

    def get_cost(self):
        return self.get_cost_intern(1, 2, 3)

    @staticmethod
    def __get_cost_intern(self, param1, param2, param3):
        return 2.0

    def set_hypothesis(self):
        return self.set_hypothesis_intern(1, 2, 3)

    @staticmethod
    def __set_hypothesis_intern(self, param1, param2, param3):
        return 3.0

    def get_gradient_descent(self):
        return self.get_gradient_descent_intern(1, 2, 3)

    @staticmethod
    def __get_gradient_descent_intern(self, param1, param2, param3):
        return 5.0

