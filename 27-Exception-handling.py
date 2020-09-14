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
