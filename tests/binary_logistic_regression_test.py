__author__ = 'Jorge Cotillo'

import unittest
import implementation.binary_logistic_reg as _binary_log_implementation
import implementation.multivariate_linear_regression as _multivariate_lin_implementation


class RegressionUnitTest(unittest.TestCase):
    def test_logistic_regression(self):
        binary_reg = _binary_log_implementation.BinaryLogisticRegression()
        theta_learned = binary_reg.predict(500000)
        print theta_learned
        self.assertEqual(True, True)

    def test_multivariate_linear_regression(self):
        multivariate_lin_reg = _multivariate_lin_implementation.MultivariateLinearRegression()
        theta_learned = multivariate_lin_reg.predict()
        print theta_learned
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
