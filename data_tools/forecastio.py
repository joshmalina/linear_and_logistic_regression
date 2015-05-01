import urllib2
import json
import csv
import calendar
import time

from datetime import datetime, timedelta
from pytz import timezone
import pytz

# utc = pytz.utc
# utc_dt = utc.localize(datetime.utcfromtimestamp(1388588400))

# china_time = timezone('Asia/Shanghai')
# china_dt = china_time.normalize(utc_dt.astimezone(china_time))

# print china_dt.hour


localtimezone = "Asia/Shanghai"

api_key = "e451fbb8fcfb9d9a2c568cf70d625420"

# approx location of pollution monitor at us embassy, beijing
lat = "39.954352"
lng = "116.466258"

'''
Takes a date and file name, returns an hourly print out of historical weather
data, including humidity, temperature, wind speed, wind direction
'''

# accommodate empty keys


def f(keyo, dicto):
    if dicto.has_key(keyo):
        return dicto[keyo]
    else:
        return 'null'


def get_correct_date(timestamp):
    utc = pytz.utc
    utc_dt = utc.localize(datetime.utcfromtimestamp(timestamp))

    china_time = timezone('Asia/Shanghai')
    local_dt = china_time.normalize(utc_dt.astimezone(china_time))

    return local_dt


def print_column_headings(headers, file_name):
    with open(file_name, 'wb') as initial_file:
        w = csv.writer(initial_file, quoting=csv.QUOTE_ALL)
        w.writerow(headers)
    initial_file.close()


def print_one_day_of_weather_data(year, month, day, max_rows, file_to_write):
    # get data
    url = 'https://api.forecast.io/forecast/' + api_key + '/' + lat + ',' + lng + ',' + year + '-' + month + '-' + day + 'T00:00:00'
    f = urllib2.urlopen(url)
    # print url
    json_string = f.read()
    parsed_json = json.loads(json_string)

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

            if 'temperature' in b:
                temperature = b['temperature']
            else:
                temperature = null

            if 'visibility' in b:
                visibility = b['visibility']
            else:
                visibility = null

            if 'pressure' in b:
                pressure = b['pressure']
            else:
                pressure = null

            if 'windSpeed' in b:
                windSpeed = b['windSpeed']
            else:
                windSpeed = null

            if 'windBearing' in b:
                windBearing = b['windBearing']
            else:
                windBearing = null

            if 'humidity' in b:
                humidity = b['humidity']
            else:
                humidity = null

            date_data = get_correct_date(time)
            year = date_data.year
            month = date_data.month
            day = date_data.day
            hour = date_data.hour
            # windBearing = b['windBearing']
            # humidity = b['humidity']

            params = [time, year, month, day, hour, temperature, windSpeed, windBearing, humidity, visibility, pressure]

            print params

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
        print_one_day_of_weather_data(str(year), append_leading_zeroes(month), append_leading_zeroes(day), 100,
                                      file_name)
        # if we make too many calls in a short period of time, the API refuses the calls, so pause
        time.sleep(0)


# gen_entire_month("Beijing-no-mb-with-date-data", 4, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 5, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 6, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 7, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 8, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 9, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 10, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 11, 2014, should_print_headers=False)
# gen_entire_month("Beijing-no-mb-with-date-data", 12, 2014, should_print_headers=False)









