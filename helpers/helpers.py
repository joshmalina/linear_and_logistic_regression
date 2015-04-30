__author__ = 'Jorge Cotillo'

import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '../entity')
import os
import math


class Helpers(object):

    @staticmethod
    def get_binary_training_data_from_csv(file_name, x_column_names, y_column_name, scale=False, omit_header=False):

        # moving up folder, this is because helpers is inside folder helpers, and we want the to retrieve the csv
        # from data folder instead

        os.chdir("..")

        # call pandas and get all the columns

        # first, temporally append y_column_name into x_column_names in order to retrieve all the columns
        temp_all_columns = []

        for i in range(len(x_column_names)):
            temp_all_columns.append(x_column_names[i])

        temp_all_columns.append(y_column_name)

        if omit_header:
            raw_result = pd.read_csv(file_name, names=temp_all_columns, header=0)
        else:
            raw_result = pd.read_csv(file_name, names=temp_all_columns)

        # retrieve only x columns (features)
        xs = np.matrix(raw_result[x_column_names])

        # get as many ones as m examples exists in our training data
        ones = np.matrix(np.ones(xs.shape[0])).T

        # append ones to the initial list of x features to conform to n + 1 features
        xs = np.hstack([ones, xs])

        if scale:
            xs = Helpers.feature_list_scaler(xs)

        ys = np.matrix(raw_result[y_column_name]).T

        return xs, ys

    # scale features so that gradient descent converges more quickly
    # doesn't apply to x0 = ones
    @staticmethod
    def feature_scaler(col): 
        avg = np.mean(col)
        std = np.std(col)

        # for each x, subtract by the column mean and divide by the standard dev
        scale = np.vectorize(lambda x: (x - avg) / std)

        return scale(col)

    # scale all features
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

    @staticmethod
    def get_single_col(path_to, file_name, param):

        # get data
        df = pd.read_csv(path_to + file_name, header=0)

        # get linear predictor variables
        keep = df[param]        

        # arrange data
        xs = np.array(keep)

        return xs

    # takes a vector of wind_degrees, returns corresponding columns of
    # sin and cos values
    # since sin/cos are already in range (-1, 1), don't need to be scaled
    # also should only be used with other scaled values
    @staticmethod
    def get_and_prep_wind_deg(deg_col=None):

        if deg_col is None:
            deg_col = Helpers.get_single_col('../Data/', 'wp_remove_null_2014.csv', 'wind_bearing_deg')

        # takes a single degree, returns sin/cos
        def to_sin_cos(deg):
            rad = math.radians(deg)
            return math.sin(rad), math.cos(rad)        

        to_both = np.vectorize(lambda x: to_sin_cos(x))

        return to_both(deg_col)

    @staticmethod
    def include_prepped_wind_deg(ready_set):

        sines, cosines = Helpers.get_and_prep_wind_deg()

        ready_set.insert(1, 'sin_wind_dir', sines)
        ready_set.insert(2, 'cos_wind_dir', cosines)

        return ready_set

    @staticmethod
    def get_and_prep_hourly_data(deg_col=None):

        if deg_col is None:
            deg_col = Helpers.get_single_col('../Data/', 'wp_remove_null_2014.csv', 'Hour')

        def calc_sin(hr):
            return math.sin(2 * math.pi * (hr - .5) / 23)


        def calc_cos(hr):
            return math.cos(2 * math.pi * (hr - .5) / 23)


        def to_sin_cos(deg):            
            return calc_sin(deg), calc_cos(deg) 

        to_both = np.vectorize(lambda x: to_sin_cos(x))

        return to_both(deg_col)

    @staticmethod
    def include_prepped_hourly_data(ready_set):

        sines, cosines = Helpers.get_and_prep_hourly_data()

        ready_set.insert(1, 'sin_hourly', sines)
        ready_set.insert(2, 'cos_hourly', cosines)

        return ready_set


    @staticmethod
    def get_and_prep_monthly_data(deg_col=None):

        if deg_col is None:
            deg_col = Helpers.get_single_col('../Data/', 'wp_remove_null_2014.csv', 'Month')

        def calc_sin(hr):
            return math.sin(2 * math.pi * (hr - .5) / 11)

        def calc_cos(hr):
            return math.cos(2 * math.pi * (hr - .5) / 11)

        def to_sin_cos(deg):            
            return calc_sin(deg), calc_cos(deg) 

        to_both = np.vectorize(lambda x: to_sin_cos(x))

        return to_both(deg_col)

    @staticmethod
    def include_prepped_monthly_data(ready_set):

        sines, cosines = Helpers.get_and_prep_hourly_data()

        ready_set.insert(1, 'sin_monthly', sines)
        ready_set.insert(2, 'cos_monthly', cosines)

        return ready_set


    @staticmethod
    def get_data_2(path_to, file_name, y_param, x_param_list, scale=False):

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

        keep = Helpers.include_prepped_wind_deg(keep)
        keep = Helpers.include_prepped_hourly_data(keep)
        keep = Helpers.include_prepped_monthly_data(keep)

        # arrange data
        xs = np.array(keep)

        if scale:
            xs = Helpers.feature_list_scaler(xs)

        return xs, ys





