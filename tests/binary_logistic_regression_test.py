__author__ = 'Jorge Cotillo'

import unittest
import implementation.binary_logistic_reg as impl


class MyTestCase(unittest.TestCase):
    def test_something(self):
        binary_reg = impl.BinaryLogisticRegression()
        theta_learned = binary_reg.predict()
        print theta_learned
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
