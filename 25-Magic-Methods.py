#intro to Magic Method
print(3.3 + 4.4)
print(3.3.__add__(4.4))

print(len([1, 2, 3, 4]))
print([1, 2, 3, 4].__len__())

print("h" in "hello")
print("hello".__contains__("h"))

print(["a", "b", "c"][2])
print(["a", "b", "c"].__getitem__(2))

#String Representation with __str__() and __repr__() methods
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return F"{self.rank} of {self.suit}"

    def __repr__(self):
        return F'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spades")
print(c) #look up order
print(str(c))
print(repr(c))

print(c.__str__())
print(c.__repr__())

#Equality with __eq__()
class Student():
    def __init__(self, maths, physics, writing):
        self.maths = maths
        self.physics = physics
        self.writing = writing

    @property
    def grades(self):
        return self.maths + self.physics + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades

bob = Student(maths = 90, physics = 90, writing = 90)
moe = Student(maths = 100, physics = 90, writing = 80)
joe = Student(maths = 45, physics = 40, writing = 50)

print(bob.grades)
print(moe.grades)

print(bob == moe)
print(moe == bob)
print(joe == moe)
print(bob == joe)

print(joe != moe)

#Magic Methods for Comparison operation
class Student():
    def __init__(self, maths, physics, writing):
        self.maths = maths
        self.physics = physics
        self.writing = writing

    @property
    def grades(self):
        return self.maths + self.physics + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades

    def __gt__(self, other_student):
        return self.grades > other_student.grades

    def __ge__(self, other_student):
        return self.grades >= other_student.grades

    def __lt__(self, other_student):
        return self.grades < other_student.grades

    def __le__(self, other_student):
        return self.grades <= other_student.grades

    def __add__(self, other_student):
        return self.grades + other_student.grades

    def __sub__(self, other_student):
        return self.grades - other_student.grades
    def __mul__(self, other_student):
        return self.grades * other_student.grades

bob = Student(maths = 90, physics = 90, writing = 90)
moe = Student(maths = 100, physics = 90, writing = 80)
joe = Student(maths = 45, physics = 40, writing = 50)

print(bob > joe)
print(bob + joe)
print(bob - joe)
print(joe <= bob)
print(bob <= joe)
print(bob * joe)

#Exercise 1
class Bustrip():
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price

    def __str__(self):
        return F"You paid {self.price} to {self.company} to go to {self.destination}."


    def __eq__(self, other_bustrip):
        return self.destination == other_bustrip.destination and abs(self.price - other_bustrip.price) <= 3

boston1 = Bustrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = Bustrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = Bustrip(destination = "Boston", company = "Megabus", price = 49.99)
philly = Bustrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)
print(boston1 == philly)
print(boston1 == boston2)
print(boston1 == boston3)

#Truthiness with __bool__ method
class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity

my_emotional_state = Emotion(positivity = 20, negativity = 40)
if my_emotional_state:
    print("This will not print because I have more negativity than positivity")

my_emotional_state.positivity = 100
if my_emotional_state:
    print("This will print because I have more negativity than positivity")

#The namedtuple Object
import collections
# Book = collections.namedtuple("Book", ["title", "author"])
Book = collections.namedtuple("Book", "title author")

animal_farm = Book("Animal Farm", "Geoge Orwell")
gastby = Book(author = "F. Scott Fitzgerald", title = "The Great Gastby")

print(animal_farm[0]) #tuple like
print(animal_farm.title) #class type
print(gastby.author)
print(gastby[1])

#Exercise
GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])
squat = GymExercise("squat", 265, 3)

bench = GymExercise("benchpress", 185, 5)

deadlift = GymExercise("deadlift", 225, 6)

press = GymExercise("press", 120, 8)

print(press[2])
print(bench.weight)
print(deadlift[1])
print(squat.name)

Book = collections.namedtuple("Book", "title author")

animal_farm = Book("Animal Farm", "Geoge Orwell")
gastby = Book(author = "F. Scott Fitzgerald", title = "The Great Gastby")

# word = "dynasty"
# print(len(word))
# print(word.__len__())

class Library():
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library("Animal Farm")
l2 = Library("Animal Farm", "The Great Gastby")
print(len(l1))
print(len(l2))

#indexing with the getitem and setitem magic methods
pillows = {
    "soft": 79.99,
    "hard": 99.99
}

print(pillows["soft"])
print(pillows.__getitem__("soft"))

class CrayonBox():
    def __init__(self):
        self.crayons = []
    
    def add(self, crayon):
        self.crayons.append(crayon)

    def __str__(self):
        return "Yippie"

    def __getitem__(self, index):
        return self.crayons[index]
    
    def __setitem__(self, index, value):
        self.crayons[index] = value

cb = CrayonBox()
cb.add("Blue")
cb.add("Yellow")
print(cb)
print(cb.__str__())
print(cb[1])

cb[0] = "Red"
print(cb[0])

for crayon in cb:
    print(crayon)

#Exercise
# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes

# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)

class Car():
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

class Dealership():
    def __init__(self):
        self.cars = []

    def accept_delivery(self, car):
        self.cars.append(car)

    def __getitem__(self, index):
        return self.cars[index]
    
    def __setitem__(self, index, value):
        self.cars[index] = value

f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota

# __del__ magic method
import time
class Garbage():
    def __del__(self):
        print("This is a good lesson")

g = Garbage()

g = [1, 2, 3]

time.sleep(5)
print("Program done!")
#Exercise
# Declare a Newspaper class. 

# Each Newspaper will have a 'pages' attribute set to an integer 
# and a 'sections' attribute set to a dictionary.
# The keys in 'sections' will be strings representing a section (i.e. "Politics") 
# and the values will be the starting page for that section (i.e. "A5").

# The length of a newspaper should be equal to the number of pages it holds.

# Indexing the newspaper by a section should return the starting pasge for that section.

# Make it so two newspapers are considered equal if they have the 
# same number of pages AND the same number of sections
class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections

    def __len__(self):
        return self.pages
        
    def __getitem__(self, section):
        return self.sections[section]
    
    def __eq__(self, other_new):
        return self.pages == other_new.pages and len(self.sections) == len(other_new.sections)

# EXAMPLE:
monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False -- np1 has 3 sections while np2 has 2 sections
print(np1 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"






