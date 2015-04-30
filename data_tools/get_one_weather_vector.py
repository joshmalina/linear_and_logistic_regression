import urllib2
import json
import calendar
import time
import numpy as np
from pylab import *
sys.path.insert(0, '../helpers')
import helpers as hp
import forecastio

from datetime import datetime, timedelta
from pytz import timezone
import pytz

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
print c


## ['x0', monthly_sin', 'monthly_cos', 'hourly_sin', 'hourly_cos', 'wind_dir_sin', 'wind_dir_cos',
# wind_speed_mph', 'temperature_f', 'pressure_mb', 'visibility_miles_max_10']

#print zeros(shape=(1, 11))

averages = hp.Helpers.get_averages()

# print averages

date = forecastio.get_correct_date(c['time'])

m_sin, m_cos = hp.Helpers.transform_unit(date.month, 12)
h_sin, h_cos = hp.Helpers.transform_unit(date.hour, 24)

if 'windBearing' in c:
	w_sin, w_cos = hp.Helpers.transformWind(c['windBearing'], -999)
else:
	w_sin, w_cos = (averages['wind_dir_sin'], averages['wind_dir_cos'])


w = {'x0':1, 'monthly_sin': m_sin, 'monthly_cos':m_cos, 'hourly_sin': h_sin, 'hourly_cos':h_cos,
'wind_dir_sin': w_sin, 'wind_dir_cos': w_cos, 'wind_speed_mph': c.get('windSpeed', averages['wind_speed_mph']),
'temperature_f': c.get('temperature', averages['temperature_f']), 'pressure_mb': c.get('pressure', averages['pressure_mb']),
'visibility_miles_max_10':c.get('visibility', averages['visibility_miles_max_10'])}

print w






