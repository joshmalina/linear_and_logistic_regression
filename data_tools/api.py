from pytz import timezone
import pytz
from datetime import datetime, timedelta
import urllib2
import json

# some basic methods and data for querying the forecastio api
class api(object):

	def __init__(self):
		# approx location of pollution monitor at us embassy, beijing
		# to match weather location collection with pollution collection location
		self._lat = "39.954352"
		self._lng = "116.466258"
		self._key = "e451fbb8fcfb9d9a2c568cf70d625420"
		self._localtimezone = "Asia/Shanghai"
		self._base_url = 'https://api.forecast.io/forecast/'
		self._url = self.get_base_url() + self.get_key() + '/' + self.get_lat() + ',' + self.get_lng()

	def get_lat(self):
		return self._lat

	def get_lng(self):
		return self._lng

	def get_key(self):
		return self._key

	def get_base_url(self):
		return self._base_url

	def get_url(self):
		return self._url

	def get_local_time_zone(self):
		return self._localtimezone

	def get_correct_date(self, timestamp):
	    utc = pytz.utc
	    utc_dt = utc.localize(datetime.utcfromtimestamp(timestamp))
	    china_time = timezone(self.get_local_time_zone())
	    local_dt = china_time.normalize(utc_dt.astimezone(china_time))
	    return local_dt

	def get_and_load_data(self, fully_formed_url):
		f = urllib2.urlopen(fully_formed_url)
		json_string = f.read()
		parsed_json = json.loads(json_string)
		return parsed_json

