__author__ = 'Jorge Cotillo'

import unittest
import implementation.binary_logistic_reg as impl


class MyTestCase(unittest.TestCase):
    def test_something(self):
        binary_reg = impl.BinaryLogisticRegression(None)
        binary_reg.predict()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
