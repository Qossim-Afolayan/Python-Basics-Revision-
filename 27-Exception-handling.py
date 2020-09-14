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