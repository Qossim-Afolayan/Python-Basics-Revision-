#The try-except Block
def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except:
        calculation = 5
    return calculation

print(divide_5_by_number(0))
print(divide_5_by_number(10))
print(divide_5_by_number("Nonsense"))

#Catching one or more specific exceptions
def divide_5_by_number(n):
    try:
        calculation = 5 / n

    except ZeroDivisionError:
        return "You can't divide by Zero!"

    except TypeError as e:
        return f"Something went wrong the error was {e}"

    return calculation

print(divide_5_by_number(0))
print(divide_5_by_number(10))
print(divide_5_by_number("Nonsense"))

#Combining all specific exceptions
def divide_5_by_number(n):
    try:
        calculation = 5 / n

    except (TypeError, ZeroDivisionError) as e:
        return f"Something went wrong the error was {e}"

    return calculation

print(divide_5_by_number(0))
print(divide_5_by_number(10))
print(divide_5_by_number("Nonsense"))

#The raise Keyword
def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or both of the values is invalid. Both numbers must be positive")

        return a + b

    except ValueError as e:
        return F"Caught the ValueError: {e}"

print(add_positive_numbers(10, 5))
print(add_positive_numbers(-2, 3))
print(add_positive_numbers(2, -3))

#Custom Exceptions (User-Defined Exception)
class NegativeNumbersError(Exception):
    """One or more inputs are negative"""
    pass

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
        return a + b
    except:
        return "Shame on you, not valid!"

print(add_positive_numbers(10, 5))
print(add_positive_numbers(-2, 3))
print(add_positive_numbers(2, -3))

#Exception Inheritance Hierachies
class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
    print(F"Caught an error: {e}")

try:
    raise SillyMistake("super silly mistake")
except SillyMistake as e:
    print(F"Caught an error: {e}")

try:
    raise StupidMistake("Extra stupid mistake")
except Mistake as e:
    print(F"Caught an error: {e}")

try:
    raise SillyMistake("super silly mistake")
except Mistake as e:
    print(F"Caught an error: {e}")

#The else and finally Block
x = 10

try:
    print(y + 4)
except NameError:
    print("Some variable not defined")

else:
    print("This will print if there is no error in the try block")

finally:
    print("this will print with or without errors i the try block")
    print("Closing file ...")

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








