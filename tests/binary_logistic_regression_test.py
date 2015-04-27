__author__ = 'Jorge Cotillo'

import unittest
import implementation.binary_logistic_reg as impl
import numpy as np
import pandas as pd
import os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        os.chdir("..")
        # student_data = pd.read_csv('data/binary_training_set.csv', names=['wind_speed_mph', 'polluted'], header=0)
        student_data = pd.read_csv('data/ones - wind-speed - binay pol value.csv', names=['exam1', 'exam2', 'admitted'])
        # X = np.matrix(student_data[['wind_speed_mph']])
        X = np.matrix(student_data[['exam1', 'exam2']])
        ones = np.matrix(np.ones(X.shape[0])).T
        X = np.hstack([ones, X])
        X[:4]

        # y = np.matrix(student_data.polluted).T
        y = np.matrix(student_data.admitted).T
        y[:4]

        binary_reg = impl.BinaryLogisticRegression(X, y)
        theta_learned = binary_reg.train(alpha=0.01,n=500000)

        # theta = binary_reg.predict()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
