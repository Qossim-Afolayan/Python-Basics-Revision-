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





