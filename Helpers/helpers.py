__author__ = 'Jorge Cotillo'

import pandas as pd
import entity.training_set_entity as tse


class Helpers(object):

    @staticmethod
    def get_binary_training_data_from_csv(self, file_name, x_column_names, y_column_name):
        # call pandas
        raw_result = pd.read_csv(file)
        training_set_list = []

        # translate csv data into a list of training_set_entity
        for i in range(0, raw_result.length):
            # x_column_list will contain all the columns we are going to utilize in our equation,
            # for logistic regression this usually is only one input variable
            x_input_variables = []
            for ii in range(0, x_column_names.length):
                x_input_variables.append(x_column_names[ii])
            # initialize training set entity and pass a boolean
            training_set = tse.TrainingSetEntity(True)
            training_set.set_x(x_input_variables)
            training_set.set_y(raw_result[y_column_name])
            training_set_list.append(training_set)
        return training_set_list



