import sys
sys.path.insert(0, '../implementation')
import multivariate_linear_regression as mlp
sys.path.insert(0, '../data_tools')
import get_one_weather_vector as gv
import pprint
import numpy as np

print("Welcome to our machine. At the current moment in time, the forecast in beijing is: ")


pprint.pprint(gv.now_weather_readable())

xs = np.array(gv.raw_on())[:, 0:11]
# print xs
# pprint.pprint(mlp.g.get_data()[0][0])

# print mlp.g.predict(mlp.g.get_data()[0][0])

print ("Given this data, our multivariate_linear_regression algorithm predicts that the pollution will be:")

print mlp.g.predict(xs)

