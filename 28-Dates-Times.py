from datetime import date

birthday = date(1991, 4, 12)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

# date(2025, 15, 10)
# date(2020, 1, 35)

print(birthday.year)
print(birthday.month)
print(birthday.day)

# birthday.year = 2020

today = date.today()
print(today)
print(type(today))

from datetime import time

start = time()
print(start)
print(type(start))
print(start.hour)
print(start.minute)
print(start.second)

print(time(6))
print(time(hour = 5))
print(time(hour = 10))

print(time(12, 25))
print(time(hour = 12, minute = 25))

#11:34:22PM
print(time(23, 44, 56))
evening = time(hour = 23, minute = 44, second = 26)
print(evening)
print(evening.hour)
print(evening.minute)
print(evening.second)

# time(27)
#Exercise
# Declare a titanic variable pointing to a date object representing April 14th, 1912
# Declare an independence_day variable pointing to a date object representing July 4th, 1776
# Declare an alarm_clock variable set to a time object representing 05:45:00AM
# Declare a one_second_away variable set to a time object representing 11:59:59PM

titanic = date(1912, 4, 14)
independence_day = date(1776, 7, 4)
alarm_clock = time(5, 45)
one_second_away = time(23, 59, 59)

# The datetime object
from datetime import datetime

# import datetime

# datetime.datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16))
print(datetime(1999, 7, 24, 14, 16, 58))
print(datetime(year = 1999, month = 7, day = 24, hour = 14, minute = 16, second = 58))

today = datetime.today()
print(today)
print(datetime.now())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)

print(today.weekday())

same_time_twenty_years_ago = today.replace(year = 1999)
print(same_time_twenty_years_ago)

same_time_in_january = today.replace(month = 1)
print(same_time_in_january)

start_of_january_1999 = today.replace(year = 1999, month = 1, day = 1)
print(start_of_january_1999)

#The datetime object: The strftime Method
today = datetime.today()

print(today.strftime("%m"))
print(today.strftime("%m %d"))
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%m-%d-%Y"))

print(today.strftime("%Y-%m-%d"))
print(today.strftime("%y-%m-%d"))

print(today.strftime("%A"))
print(today.strftime("%B"))
# Given the datetime object below (November 17th, 2000 at 6:00:00AM), 
# invoke the strftime to method produce the following result:

# The day of the week, abbreviated (i.e. "Fri" )

# today = datetime(2000, 11, 17, 6, 0, 0)

today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%a")) # Fri
# Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

# The full month name, the zero-padded day, the four-digit year. The day and year should be separated by a comma and a space (i.e. "November 17, 2000")

# today = datetime(2000, 11, 17, 6, 0, 0)

# today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%B %d, %Y")) # November 17, 2000
# Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

# The day of the year (i.e. "273")

# today = datetime(2000, 11, 17, 6, 0, 0)

# today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%j")) # 322
# Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

# The week number of the year (i.e. "46")

# today = datetime(2000, 11, 17, 6, 0, 0)

# today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%W")) # 46
# Given the datetime object below (November 17th, 2000 at 6:00:00AM), invoke the strftime to method produce the following result:

# The time with a zero-padded hour, zero-padded minute, zero-padded second and AM / PM designation (i.e. "06:00:00 AM")

# today = datetime(2000, 11, 17, 6, 0, 0)

today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%H:%M:%S%p")) # 06:00:00AM
#Exercise
# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 2002-02-22 09:45:23

def one_from_two(date_ob, time_ob):
    year = date_ob.year
    month = date_ob.month
    day = date_ob.day

    hour = time_ob.hour
    minute = time_ob.minute
    second = time_ob.second

    return datetime(year, month, day, hour, minute, second)

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)
print(one_from_two(some_date, some_time)) #=> datetime object representing 2002-02-22 09:45:23

#The timedelta object
from datetime import datetime, timedelta

birthday = datetime(1999, 6, 11)
today = datetime.now()
my_life_span = today - birthday
print(my_life_span)
print(type(my_life_span))

print(my_life_span.total_seconds())

five_hundred_days = timedelta(days = 500, hours = 12)
print(five_hundred_days)

print(five_hundred_days + five_hundred_days)
print(today + five_hundred_days)