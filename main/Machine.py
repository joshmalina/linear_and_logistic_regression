# josh environment
import sys
sys.path.insert(0, '../implementation')
import multivariate_linear_regression as mlp
sys.path.insert(0, '../data_tools')
import get_one_weather_vector as gv
import binary_logistic_reg as binary_log_reg

# jorge environment
# import data_tools.get_one_weather_vector as gv
# import implementation.binary_logistic_reg as binary_log_reg
# import implementation.multivariate_linear_regression as mlp

# common
import numpy as np

print("Welcome to our machine. At the current moment in time, the forecast in beijing is: ")
print(gv.now_weather_readable())

xs = np.array(gv.raw_on())[:, 0:11]
print ("Given this data, our multivariate_linear_regression algorithm predicts that the pollution is:")
print mlp.g.predict(xs)[0]

print("\n=======================================================================================\n")
print("Our binary logistic regression algorithm, taking wind speed as its predictor, generates the following theta values based on historical data: ")
regressionAlgorithm = binary_log_reg.BinaryLogisticRegression()
prediction = regressionAlgorithm.predict()
print("theta 0: " + str(prediction[0]))
print("theta 1: " + str(prediction[1]))
print("\n")

# print("The actual pollution levels at that speed is: (Tweeter feed)")
# forecast.gen_entire_month("Beijing-no-mb-with-date-data", 5, 2015, should_print_headers=False)
