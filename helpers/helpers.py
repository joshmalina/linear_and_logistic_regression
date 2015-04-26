__author__ = 'Jorge Cotillo'

import pandas as pd
import numpy as np
import entity.training_set_entity as tse
import os
from StringIO import StringIO


class Helpers(object):

    @staticmethod
    def get_binary_training_data_from_csv(self, file_name, x_column_names, y_column_name):

        # moving up folder, this is because helpers is inside folder helpers, and we want the to retrieve the csv
        # from data folder instead

        os.chdir("..")

        # call pandas
        raw_result = pd.read_csv(file_name)

        training_set_list = []

        # translate csv data into a list of training_set_entity
        for i in range(0, len(raw_result)):
            # x_column_list will contain all the columns we are going to utilize in our equation,
            # for logistic regression this usually is only one input variable
            x_input_variables = []
            for ii in range(0, len(x_column_names)):
                x_input_variables.append(raw_result[x_column_names[ii]].values[i])
            # initialize training set entity and pass a boolean
            training_set = tse.TrainingSetEntity()
            training_set.set_x = x_input_variables
            training_set.set_y = raw_result[y_column_name].values[i]
            training_set_list.append(training_set)
        return training_set_list

    '''
        Takes a column of a numpy array, returns a scaled column; don't apply
        this to x0 = ones
    '''
    def feature_scaler(col): 
        avg = np.mean(col)
        std = np.std(col)

        # for each x, subtract by the column mean and divide by the standard dev
        scale = np.vectorize(lambda x : (x - avg) / std)

        return scale(col)



