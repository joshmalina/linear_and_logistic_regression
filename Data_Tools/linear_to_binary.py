import pandas as pd
import numpy as np
from pylab import *
import csv

df = pd.read_csv('wp_remove_null_2014.csv', header=0)

ys = df['Value']
ys = np.array(ys)
keep = df[['wind_speed_mph']]
keep.insert(0, 'x0', ([1.0] * len(df)))
xs = np.array(keep)

print xs

binary_value = ones(len(ys))

for indx, y in enumerate(ys):
	binary = 0
	if y >= 100:
		binary = 1
	else:
		binary = 0
	binary_value[indx] = binary

print binary_value

binary_value = np.array(binary_value)

keep.insert(2, "binary", binary_value)

keep.to_csv("binary_value.csv", sep=",", index=False)