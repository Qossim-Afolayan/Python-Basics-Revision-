#Mathematical Expression
print(3 +  4)
print(5 - 6)
print(3.9 + 1.2)
print(4.2 - 1.8)
print(6 * 4)

print("Ba" + "con")
print("lolo" * 32)

print(10 + 3.8)

print(3 ** 3)
print(4 ** 2)

print(3 + 5 * 2)
print((3 + 5) * 2)

#Division, Floor Division and the Modulo operator
print(15 / 3)
print(14 / 3)

print(14 // 3)
print(-14 // 3)

print(14 % 3)
print(15 % 3)
print(16 % 3)

print(1 % 3)
print(2 % 3)
print(3 % 3)

#Boolean Data Type, The Equality Operator
print(True)
print(False)
print("True")
print("False")

print(5 == 5)
print(5 == 6)
print(8.2 == 8.2)
print(8.2 == 4.1)
print(5 == "5")

print("ham" == "ham")
print("ham" == "Ham")
print("ham" == "bacon")
print("5" == "5")
print("@#$" == "@#$")
print(" " == " ")
print("" == " ")

print(5 == 5.0)
print(5 == 5.1)

print(True == True)
print(False == False)
print(True != False)
print(False != True)

#Boolean Mathematical operators
print(5 < 8)
print(10 < 7)
print(8 <= 8)
print(8 <= 11)
print(8 <= 7)

print(9 > 5)
print(9 > 11)
print(5 >= 5)
print(5 >= 4)
print(5 >= 7)

print(5 < 8 <= 10)
print(5 < 10 <= 2)

#Type Function
print(type(5))
print(type(10))

print(type(3.7))
print(type(2.0))

print(type("Computer"))
print(type(""))

print(type(5) == type(10))
print(type("Qossim") == type("Hassan"))
print(type(True))

print(type([1, 2, 3]))
print(type({"NJ": "Trenton"}))

#Type Conversion
print(int(3.14))
print(int(3.99))
print(int(float(("3.99"))))
print(int(3))

print(float(3))
print(float("10.98"))
print(float(5.23))

print(str(3.67))
print(str(5))
print("Hello")

print(str(5) + "Hello")

print(3 + 4)
print(4.5 + 5.5)
print(3 + 5.9)

#Variable
name = "Qossim"
age = 12
handsome = True
favorite_language = "Python"

print(name)
print(handsome)
# print(occupation)

print(age + 4)
print("My name is", name, "and I am", age, "years old")

age = 10
print(age)

age = 27 + 10
print(age)

fact_or_fiction = 6 < 19
print(fact_or_fiction)

chameleon = 5
print(chameleon)

chameleon = "Some String"
print(chameleon)

chameleon = 23.5
print(chameleon)

chameleon = False
print(chameleon)

#Multiple Variable Assignment
a = b = 5

b = 10
print(b)
print(a)

a, b = 5, 10

a, b, c = 3, 5, 13
print(a)
print(b)
print(c)

#Augmented Assignment Operator
a = 1
a = a + 2
print(a)

a = 1
a += 2
print(a)

word = "race"
word = word + "car"
print(word)

word = "race"
word += "car"
print(word)

b = 5
b *= 5
print(b)

b -= 4
print(b)

b /= 3
print(b)

#Collecting User Input with input function
first_name = input("What's your first name? ")
print("It's nice to meet you", first_name)

print("Let me help you add two numbers")
first_num = input("Enter your first number ")
second_num = input("Enter your second number ")
print("The sum of the two numbers is", int(first_num) + int(second_num))
