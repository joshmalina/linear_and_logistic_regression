import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '../helpers')
import helpers as h
sys.path.insert(0, '../helpers/data_class')
from dataclass import *
sys.path.insert(0, '../interfaces')
import forecastio

# inherit from the DataClass, which will be useful when
# we have missing fields
class WeatherInstance(DataClass):

	def __init__(self, weather_d, path_and_name_to_parent):
		DataClass.__init__(self, path_and_name_to_parent)		
		self._features = self.__prep_data__(weather_d)

	# override parent method
	def __prep_data__(self, d):
		onez = np.ones((1, 11))
		features = pd.DataFrame(onez)

		date = forecastio.get_correct_date(d['time'])

		# use weather data to transform and insert monthly circular data
		sm, cm = h.Helpers.trans([date.month], 12, h.Helpers.transform_unit)
		features.insert(1, 'sin_month', sm)
		features.insert(2, 'cos_month', cm)

		# use weather data to transform and insert hourly data
		sh, ch = h.Helpers.trans([date.hour], 24, h.Helpers.transform_unit)
		features.insert(3, 'sin_hour', sh)
		features.insert(4, 'cos_hour', ch)

		# use either weather or parent averages to transform and insert
		if 'windBearing' in d:
			sw, cw = h.Helpers.trans(d['windBearing'], -999, h.Helpers.transformWind)
		else:
			sw, cw = DataClass.get_avg('sin_wind_dir'), DataClass.get_avg('cos_wind_dir')

		features.insert(5, 'sin_wind_dir', sw)
		features.insert(6, 'cos_wind_dir', cw)

		def eval_instance(api_feature_name, dad_feature_name, api_data=d, dad=DataClass):
			if api_feature_name in api_data:
				ready = super(WeatherInstance, self).scale_new_val(dad_feature_name, api_data[api_feature_name])
			else:
				ready = dad.get_avg(self, dad_feature_name)
			return ready

		features.insert(7, 'wind_speed_mph', eval_instance(api_feature_name='windSpeed', dad_feature_name='wind_speed_mph'))
		features.insert(8, 'temperature_f', eval_instance('temperature', 'temperature_f'))
		features.insert(9, 'pressure_mb', eval_instance('pressure', 'pressure_mb'))
		features.insert(10, 'visibility_mi', eval_instance(api_feature_name='visibility', dad_feature_name='visibility_mi'))

		return features 

	def get_features(self):
		return self._features




