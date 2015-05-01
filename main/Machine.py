import sys
sys.path.insert(0, '../implementation')
import multivariate_linear_regression as mlp
sys.path.insert(0, '../data_tools')
import get_one_weather_vector as gv
import pprint
import numpy as np

# import implementation.binary_logistic_reg as binary_log_reg
# import implementation.multivariate_linear_regression as multivariate_lin_reg
# import data_tools.forecastio as forecast

print("Welcome to our machine. At the current moment in time, the forecast in beijing is: ")
print(gv.now_weather_readable())

xs = np.array(gv.raw_on())[:, 0:11]
print ("Given this data, our multivariate_linear_regression algorithm predicts that the pollution is:")
print mlp.g.predict(xs)[0]

# print("1) Linear regression:")
# print("2) Multivariate linear regression")
# print("3) Binary logistic regression:")
# algorithm = input("Your choice: ")

# regressionAlgorithm = None
# if algorithm == 2:
#     print("Thank you. What parameter would you like to run it on?")

#     print("1) wind speed")

#     parameter = input("Your choice: ")

#     print("Thank you for choosing wind speed. In Beijing, the wind never reaches higher than 33 mph. \nPlease enter a "
#           "wind speed of your choosing:")

#     speed = input("Your choice: ")

#     # pol_val = lin_reg.predict_y_give_x(speed)
#     regressionAlgorithm = multivariate_lin_reg.MultivariteLinearRegression()
# elif algorithm == 3:
#     regressionAlgorithm = binary_log_reg.BinaryLogisticRegression()

# prediction = regressionAlgorithm.predict()

# print("Our estimate for pollution levels at that speed is: ")
# print(prediction)

# print("The actual pollution levels at that speed is: (Tweeter feed)")
# forecast.gen_entire_month("Beijing-no-mb-with-date-data", 5, 2015, should_print_headers=False)
