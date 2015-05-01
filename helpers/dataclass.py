import sys
sys.path.insert(0, '../helpers')
import helpers as h
sys.path.insert(0, '../interfaces')
import pandas as pd
import numpy as np

# a convenient way to draw on the manipulated data frame
class DataClass(object):

	def __init__(self, path_and_name):
		self._features, self._target, self._original = self.prep_data(path_and_name)

	def prep_data(self, path_and_name):
		a = pd.read_csv(path_and_name, header=0)
		original_vals = a
		target = a['Value']

		# initialize the frame with a column of all ones
		onez = np.ones((target.shape))
		features = pd.DataFrame(onez)

		# transform and insert circular month data
		sm, cm = h.Helpers.trans(a['Month'], 12, h.Helpers.transform_unit)
		features.insert(1, 'sin_month', sm)
		features.insert(2, 'cos_month', cm)

		# transform and insert circular hourly data
		sh, ch = h.Helpers.trans(a['Hour'], 24, h.Helpers.transform_unit)
		features.insert(3, 'sin_hour', sh)
		features.insert(4, 'cos_hour', ch)

		# transform and insert circular wind directional data
		sw, cw = h.Helpers.trans(a['wind_bearing_deg'], -999, h.Helpers.transformWind)
		features.insert(5, 'sin_wind_dir', sw)
		features.insert(6, 'cos_wind_dir', cw)

		# scale and insert the remain features
		features.insert(7, 'wind_speed_mph', h.Helpers.feature_scaler(a['wind_speed_mph']))
		features.insert(8, 'temperature_f', h.Helpers.feature_scaler(a['temperature_f']))
		features.insert(9, 'pressure_mb', h.Helpers.feature_scaler(a['pressure_mb']))
		features.insert(10, 'visibility_mi', h.Helpers.feature_scaler(a['visibility_miles_max_10']))

		return features, target, original_vals

	def get_avg(self, feature):
		return np.mean(self._features[feature])

	def get_std(self, feature):
		return np.std(self._features[feature])

	def get_features(self):
		return self._features

	# useful for scaling individual values, as in from new values
	# relies on this class' original avg and std
	def scale_new_val(self, feature, val):
		avg = np.mean(self._original[feature])
		std = np.std(self._original[feature])
		result = (val - avg) / std
		return result

# x = DataClass('../Data/wp_remove_null_2014.csv')

# print x.get_avg('visibility_mi')
