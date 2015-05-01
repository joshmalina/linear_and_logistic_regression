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

    @staticmethod
    def info(col):
        return np.mean(col), np.std(col)

    # scale all features
    @staticmethod
    def feature_list_scaler(xs):
        num_features = xs.shape[1]
        # skips first feature, x0 = ones
        # skips first seven features
        for i in range(7, num_features):
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


    @staticmethod
    def transform_unit(unit, divisor):

        def transform(unit):
            return (2 * math.pi * (unit - .5) / divisor)

        return math.sin(transform(unit)), math.cos(transform(unit))


    @staticmethod
    def trans(param, divisor, f):

        to_both = np.vectorize(lambda x: f(x, divisor))

        return to_both(param)



    @staticmethod
    def transformWind(deg, divisor=None):
        rad = math.radians(deg)
        return math.sin(rad), math.cos(rad)    

    @staticmethod
    def get_and_prep_circular_data2(param, divisor, f):

        deg_col = Helpers.get_single_col('../Data/', 'wp_remove_null_2014.csv', param)        

        to_both = np.vectorize(lambda x: f(x, divisor))

        return to_both(deg_col)


    @staticmethod
    def prep_circular_data(ready_set):

        sin_month, cos_month = Helpers.get_and_prep_circular_data2('Month', 12, Helpers.transform_unit)
        sin_hour, cos_hour = Helpers.get_and_prep_circular_data2('Hour', 24, Helpers.transform_unit)
        sin_wind, cos_wind = Helpers.get_and_prep_circular_data2('wind_bearing_deg', -999, Helpers.transformWind)

        ready_set.insert(1, 'sin_monthly', sin_month)
        ready_set.insert(2, 'cos_monthly', cos_month)
        ready_set.insert(3, 'sin_hourly', sin_hour)
        ready_set.insert(4, 'cos_hourly', cos_hour)
        ready_set.insert(5, 'sin_wind_dir', sin_wind)
        ready_set.insert(6, 'cos_wind_dir', cos_wind)

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

        keep = Helpers.prep_circular_data(keep)

        # arrange data
        xs = np.array(keep)

        if scale:
            xs = Helpers.feature_list_scaler(xs)

        return xs, ys       


    @staticmethod
    def default_vals():

        x_param_list = ['wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']

        xs, ys = Helpers.get_data_2('../Data/', 'wp_remove_null_2014.csv', 'Value', x_param_list, True)

        ws_m, ws_sd = Helpers.info(xs[:, 7])
        temp_m, temp_sd = Helpers.info(xs[:, 8])
        pressure_m, pressure_sd = Helpers.info(xs[:, 9])
        vis_m, vis_sd = Helpers.info(xs[:, 10])

        info = {'ws_m': ws_m, 'ws_sd' : ws_sd, 'temp_m' : temp_m, 'temp_sd' :temp_sd, 
        'pre_m' : pressure_m, 'pre_sd' : pressure_sd, 'vis_m' : vis_m, 'vis_sd' : vis_sd}

        return info

    @staticmethod
    def scale(x, m, sd):
        r = (x - m) / sd
        print r
        return r

    @staticmethod
    def get_averages():

        x_param_list = ['wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']

        xs, ys = Helpers.get_data_2('../Data/', 'wp_remove_null_2014.csv', 'Value', x_param_list, True)

        full_list = ['x0', 'monthly_sin', 'monthly_cos', 'hourly_sin', 'hourly_cos', 'wind_dir_sin', 'wind_dir_cos', 'wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']
        
        averages={}
        for i in range(0, 11):
            averages[full_list[i]] = np.mean(xs[:, i])
        return averages









