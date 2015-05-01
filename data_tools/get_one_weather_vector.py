import urllib2
import json
import calendar
import time
import numpy as np
from pylab import *
sys.path.insert(0, '../helpers')
import helpers as hp
import forecastio
import collections
from datetime import datetime, timedelta
from pytz import timezone
import pytz
sys.path.insert(0, '../data_tools/weather_instance')
from weather_instance import *

localtimezone = "Asia/Shanghai"

api_key = "e451fbb8fcfb9d9a2c568cf70d625420"

# approx location of pollution monitor at us embassy, beijing
lat = "39.954352"
lng = "116.466258"

url = 'https://api.forecast.io/forecast/'+api_key+'/'+lat+','+lng
f = urllib2.urlopen(url)
# print url
json_string = f.read()
parsed_json = json.loads(json_string)
c = parsed_json['currently']
date = forecastio.get_correct_date(c['time'])

def now_weather_readable():
	return c

def raw_on():
	x = WeatherInstance(weather_d=c, path_and_name_to_parent='../Data/wp_remove_null_2014.csv')
	return x.get_features()




