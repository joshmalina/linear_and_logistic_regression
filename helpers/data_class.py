import sys
sys.path.insert(0, '../helpers')
import helpers as h
sys.path.insert(0, '../interfaces')
import pandas as pd
import numpy as np

class DataClass(object):

	def __init__(self, path_and_name):
		self._features, self._target = self.prep_data(path_and_name)

	def prep_data(self, path_and_name):
		a = pd.read_csv(path_and_name, header=0)
		target = a['Value']

		onez = np.ones((target.shape))
		features = pd.DataFrame(onez)

		sm, cm = h.Helpers.trans(a['Month'], 12, h.Helpers.transform_unit)
		features.insert(1, 'sin_month', sm)
		features.insert(2, 'cos_month', cm)

		sh, ch = h.Helpers.trans(a['Hour'], 24, h.Helpers.transform_unit)
		features.insert(3, 'sin_hour', sh)
		features.insert(4, 'cos_hour', ch)

		sw, cw = h.Helpers.trans(a['wind_bearing_deg'], -999, h.Helpers.transformWind)
		features.insert(5, 'sin_wind_dir', sh)
		features.insert(6, 'cos_wind_dir', ch)

		
		

		return features, target 
 
	def get_avg(self, feature):
		return np.mean(self._features[feature])

	def get_std(self, feature):
		return np.std(feature)

	# useful for scaling individual values, as in from new values
	def scale_val(self, feature, val):
		return (val - self.get_avg(feature)) / self.get_std(feature)


x = DataClass('../Data/wp_remove_null_2014.csv')

print x.get_avg('cos_month')
