import csv
import calendar
import time
from api import api
api = api()

'''
Takes a date and file name, returns an hourly print out of historical weather
data, including humidity, temperature, wind speed, wind direction
'''

def print_column_headings(headers, file_name):
    with open(file_name, 'wb') as initial_file:
        w = csv.writer(initial_file, quoting=csv.QUOTE_ALL)
        w.writerow(headers)
    initial_file.close()


def print_one_day_of_weather_data(year, month, day, max_rows, file_to_write):

    url = api.get_url() + ',' + year + '-' + month + '-' + day + 'T00:00:00'
    parsed_json = api.get_and_load_data(url)

    all_obs = parsed_json['hourly']['data']

    null = 'null'

    # if we reach the end of the observations
    for n in range(0, len(all_obs)):
        # or we exceed the max rows desired
        if n > max_rows:
            return 0
        else:
            b = all_obs[n]

            time = b['time']

            temperature = b.get('temperature', null)
            visibility = b.get('visibility', null)
            pressure = b.get('pressure', null)
            windSpeed = b.get('windSpeed', null)
            windBearing = b.get('windBearing', null)
            humidity = b.get('humidity', null)
            date_data = api.get_correct_date(time)
            year = date_data.year
            month = date_data.month
            day = date_data.day
            hour = date_data.hour


            params = [time, year, month, day, hour, temperature, windSpeed, windBearing, humidity, visibility, pressure]

            # print params

            with open(file_to_write, 'a') as csvfile:
                w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                w.writerow(params)

            csvfile.close()


# print_one_day_of_weather_data("2014", "01", "04", 30, "test.csv")

headers = (
    "time", "year", "month", "day", "hour", "temperature", "windSpeed", "windBearing", "humidity", "visibility", "pressure")


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
		time.sleep(0)


# gen_entire_month("bj", 01, 2012, True)









