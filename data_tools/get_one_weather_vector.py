import sys
from api import api
api = api()
sys.path.insert(0, '../data_tools/weather_instance')
from weather_instance import *

parsed_json = api.get_and_load_data(api.get_url())

c = parsed_json['currently']
date = api.get_correct_date(c['time'])

def now_weather_readable():
	first_line = c['summary'] + "\n\n" 
	h = "Relative humidity: " + str(c.get('humidity', 'NaN')) + "\n"
	a = "Air pressure (mb): " + str(c.get('pressure', 'NaN')) + "\n" 
	t = "Temperature (F): " + str(c.get('temperature', 'NaN')) + "\n"
	wd = "Wind Direction (deg): " + str(c.get('windBearing', 'NaN')) + "\n"
	ws = "Wind Speed (mph): " + str(c.get('windSpeed', 'NaN')) + "\n"
	return first_line + h + a + t + wd + ws

def raw_on():
	x = WeatherInstance(weather_d=c, path_and_name_to_parent='../Data/wp_remove_null_2014.csv')
	return x.get_features()




