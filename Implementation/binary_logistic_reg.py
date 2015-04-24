__author__ = 'Jorge Cotillo'

import entity.training_set_entity as tse
import helpers.helpers as hlprs


class BinaryLogisticRegression(object):

    #def __init__(self):

    @staticmethod
    def get_training_set(self):
        x_input_variables = ['wind_speed_mph']
        training_set_list = hlprs.Helpers.get_binary_training_data_from_csv('binary_value.csv',
                                                                            x_input_variables,
                                                                            'binary')
        return training_set_list