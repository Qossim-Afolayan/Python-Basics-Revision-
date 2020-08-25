#Class Definition and instantiation
class Person():
    pass


class DatabaseConnection():
    pass

qossim = Person()
print(qossim)

db = DatabaseConnection()
print(db)

#Exercise 1
class Country():
    pass

america = Country()
canada = Country()
mexico = Country()

class Superhero():
    pass

spiderman = Superhero()
batman = Superhero()
superman = Superhero()

#The __init__ method 
class Guitar():
    def __init__(self):
        print(f"The name of the Guitar is {self}")

acoustic = Guitar()
electric = Guitar()

#Adding Attributes
class Guitar():
    def __init__(self):
        print(f"A new Guitar is being created! The object is {self}")

acoustic = Guitar()
electric = Guitar()

acoustic.wood = "Mahogany"
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)

#Setting Object attributes in the __init__ method
class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("Mahogany")
electric = Guitar("Alder")

print(electric.wood)

#Exercise 2
class Musical():
    def __init__(self, name):
        self.name = name

rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

class Shape():
    def __init__(self, sides):
        self.sides = sides

triangle = Shape(3)
square = Shape(4)
decagon = Shape(10)

#Default Values for Attributes
class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell", 19.99)
gatsby = Book("The Great Gatsby", "F. Scott Gerald")

print(animal_farm.price)
print(gatsby.price)

jude = Book(title = "Jude the Obscure", price = 24.99, author = "Thomas Hardy")

print(jude.price)

#Exercise 3
class Zombie():
    def __init__(self, health = 100, brains_eaten = 5):
        self.health = health
        self.brains_eaten = brains_eaten

bob = Zombie(80, 5)
sally = Zombie(120, 3)
benjamin = Zombie()

print(benjamin.brains_eaten)



