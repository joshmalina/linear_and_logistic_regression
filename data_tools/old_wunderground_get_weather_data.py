import urllib2
import json
import csv 
import calendar
import time

'''
Takes a date and file name, returns an hourly print out of historical weather
data, including humidity, temperature, wind speed, wind direction, and air pressure
'''

oldkey = 'a3d4db71573f30f9'
apikey = '04fce8511db42bb2'

def print_column_headings(headers, file_name):
	with open (file_name, 'wb') as initial_file:
		w = csv.writer(initial_file, quoting=csv.QUOTE_ALL)
		w.writerow(headers)
	initial_file.close()

def print_one_day_of_weather_data(year, month, day, max_rows, file_to_write):

	# get data
	url = 'http://api.wunderground.com/api/'+apikey+'/history_' + year + month + day +'/geolookup/q/Beijing/Beijing.json'
	f = urllib2.urlopen(url)
	print url
	json_string = f.read()
	parsed_json = json.loads(json_string)

	print parsed_json

	# paramterize data
	all_obs = parsed_json['history']['observations']

	# if we reach the end of the observations
	for n in range(0, len(all_obs)):
		# or we exceed the max rows desired
		if n > max_rows:
			return 0
		else: 
			base_path = all_obs[n]
			date_path = base_path['date']
			year = date_path['year']
			month = date_path['mon']
			day = date_path['mday']
			hour = date_path['hour']
			min = date_path['min']
			humidity = base_path['hum']
			temp_f = base_path['tempi']
			windspeed_mph = base_path['wspdi']
			winddir_deg = base_path['wdird']
			air_pressure_mb = base_path['pressurem']
			metar = base_path['metar']

			if(metar):
				# utc time
				params = [year, month, day, hour, min, humidity, temp_f, windspeed_mph, winddir_deg, air_pressure_mb, metar]

				print params
			else:
				return 0

			# with open (file_to_write, 'a') as csvfile:
			# 	w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
			# 	w.writerow(params)

			# csvfile.close()


print_one_day_of_weather_data("2014", "01", "01", 30, "test.csv")

headers = ("Year", "Month", "Day", "Hour", "Min", "Humidity", "Temperature_F", "Windspeed_mph", "Wind_direction_deg", "Air_Pressure_mb")

def append_leading_zeroes(num):
	return "%02d" % (num,)

def days_in_a_month(year, month_num):
	return calendar.monthrange(year, month_num)[1]

def file_namer(city, month_num, year): 
	return "raw weather - local time " + city + "-" + calendar.month_name[month_num] + "-" + str(year) + ".csv"

def gen_entire_month(city, month, year, should_print_headers, start_at_day=1):
	file_name = file_namer(city, month, year)

	if should_print_headers:
		print_column_headings(headers, file_name)

	for day in range(start_at_day, days_in_a_month(year, month) + 1):
		print_one_day_of_weather_data(str(year), append_leading_zeroes(month), append_leading_zeroes(day), 100, file_name)		
		# if we make too many calls in a short period of time, the API refuses the calls, so pause
		time.sleep(60)

# gen_entire_month("Beijing", 1, 2014, should_print_headers=True)
