__author__ = 'Jorge Cotillo'

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '../entity')
import os


class Helpers(object):

    @staticmethod
    def get_binary_training_data_from_csv(file_name, x_column_names, y_column_name):

        # moving up folder, this is because helpers is inside folder helpers, and we want the to retrieve the csv
        # from data folder instead

        os.chdir("..")

        # call pandas and get all the columns

        # first, temporally append y_column_name into x_column_names in order to retrieve all the columns
        temp_all_columns = []

        for i in range(len(x_column_names)):
            temp_all_columns.append(x_column_names[i])

        temp_all_columns.append(y_column_name)

        raw_result = pd.read_csv(file_name, names=temp_all_columns)

        # retrieve only x columns (features)
        xs = np.matrix(raw_result[x_column_names])

        # get as many ones as m examples exists in our training data
        ones = np.matrix(np.ones(xs.shape[0])).T

        # append ones to the initial list of x features to conform to n + 1 features
        xs = np.hstack([ones, xs])

        ys = np.matrix(raw_result[y_column_name]).T

        return xs, ys

    # scale features so that gradient descent converges more quickly
    # doesn't apply to x0 = ones
    @staticmethod
    def feature_scaler(col): 
        avg = np.mean(col)
        std = np.std(col)

        # for each x, subtract by the column mean and divide by the standard dev
        scale = np.vectorize(lambda x : (x - avg) / std)

        return scale(col)

    @staticmethod
    def feature_list_scaler(xs):
        num_features = xs.shape[1]
        # skips first feature, x0 = ones
        for i in range(1, num_features):
            xs[:, i] = Helpers.feature_scaler(xs[:, i])

        return xs

    @staticmethod
    def get_data(path_to, file_name, y_param, x_param_list, scale=False):

        # get data
        df = pd.read_csv(path_to + file_name, header=0)

        # get dependent variable
        ys = df[y_param]

        # arrange data
        ys = np.array(ys)

        # get linear predictor variables
        keep = df[x_param_list]

        # add an initial column of ones for the cost function   
        keep.insert(0, 'x0', ([1.0] * len(df)))

        # arrange data
        xs = np.array(keep)

        if scale:
            xs = Helpers.feature_list_scaler(xs)

        return xs, ys



