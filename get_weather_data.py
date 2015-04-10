import urllib2
import json
import csv 
import calendar
import time

'''
Takes a date and file name, returns an hourly print out of historical weather
data, including humidity, temperature, wind speed, wind direction, and air pressure
'''

def print_column_headings(headers, filename):
	with open (file_name, 'wb') as initial_file:
		w = csv.writer(initial_file, quoting=csv.QUOTE_ALL)
		w.writerow(headers)
	initial_file.close()

def print_one_day_of_weather_data(year, month, day, max_rows, file_to_write):

	# get data
	url = 'http://api.wunderground.com/api/a3d4db71573f30f9/history_' + year + month + day +'/geolookup/q/Beijing/Beijing.json'
	f = urllib2.urlopen(url)
	print url
	json_string = f.read()
	parsed_json = json.loads(json_string)

	# paramterize data
	all_obs = parsed_json['history']['observations']

	# if we reach the end of the observations
	for n in range(0, len(all_obs)):
		# or we exceed the max rows desired
		if n > max_rows:
			return 0
		else: 
			base_path = all_obs[n]
			date_path = base_path['utcdate']
			year = date_path['year']
			month = date_path['mon']
			day = date_path['mday']
			hour = date_path['hour']
			humidity = base_path['hum']
			temp_f = base_path['tempi']
			windspeed_mph = base_path['wspdi']
			winddir_deg = base_path['wdird']
			air_pressure_mb = base_path['pressurem']

			# utc time
			params = [year, month, day, hour, humidity, temp_f, windspeed_mph, winddir_deg, air_pressure_mb]


			print params

			with open (file_to_write, 'a') as csvfile:
				w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
				w.writerow(params)

			csvfile.close()


# generate_bj_pollution_data("2014", "02", "02", 100, "beijing-feb-02-2014.csv")

headers = ("Year", "Month", "Day", "Hour", "Humidity", "Temperature (F)", "Windspeed (mph)", "Wind direction (deg)", "Air Pressure (mb)")

def append_leading_zeroes(num):
	return "%02d" % (num,)

def days_in_a_month(year, month_num):
	return calendar.monthrange(year, month_num)[1]

def file_namer(city, month_str, year_str): 
	return city + "-" + month_str + "-" + year_str + ".csv"

def gen_entire_month(city, month, year):
	month_str = str(month)
	year_str = str(year)
	file_name = file_namer(city, str(month), str(year))

	for i in range(30, days_in_a_month(year, month) + 1):
		print_one_day_of_weather_data(year_str, append_leading_zeroes(month), append_leading_zeroes(i), 100, file_name)
		time.sleep(25)

gen_entire_month("beijing", 1, 2014)
