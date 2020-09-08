#Define a Subclass
class Store():
    def __init__(self):
        self.owner = "Qossim"

    def exclaim(self):
        return "Lots of stuff to buy, come inside!"

class CoffeeShop(Store):
    pass

starbuck = CoffeeShop()
print(starbuck.owner)
print(starbuck.exclaim())
#Exercise
# Declare a HardwareStore subclass that inherits from the Store superclass.
# Do not define any attributes and methods on the subclass. 
# Use the pass keyword to avoid a class body in HardwareStore.
# Instantiate a new instance of the HardwareStore class and assign it to a home_depot variable.
# Access the value of the "owner" attribute on your HardwareStore instance.
# Invoke the exclaim instance method on your HardwareStore instance.

class Store():
    def __init__(self):
        self.owner = "Boris"
  
    def exclaim(self):
        return "I'm defined in the superclass!"

class HardwareStore(Store):
    pass

home_depot = HardwareStore()
print(home_depot.owner)
print(home_depot.exclaim())

#New method on Subclasses

#Override an inherited Method on a Subclass
class Teacher():
    def teach_class(self):
        print("Teaching a Class")

    def grab_lunch(self):
        print("Yum yum yum!")
    
    def grade_test(self):
        print("A! A! A!")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray! I'm an author")

    def grade_test(self):
        print("F! F! F!")

teacher = Teacher()
professor = CollegeProfessor()

teacher.teach_class()
teacher.grade_test()
teacher.grab_lunch()

professor.teach_class()
professor.grab_lunch()
professor.grade_test()
professor.publish_book()

#Exercise
# Define a Clothing superclass with wear and sell instance methods.
# The wear method should return the string “I'm wearing this fashionable piece of clothing!”
# The sell method should return the string “Buy my piece of clothing!”

# Define a Socks subclass that inherits from the Clothing superclass.
# It should define a lose_one instance method that 
# returns the string “Where did my other one go?”
# It should override the wear method to 
# return the string “Take a look at my socks! They're gorgeous!”
# It should override the sell method to 
# return the string “Buy my socks!”

class Clothing():
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"

    def sell(self):
        return "Buy my piece of clothing!"

class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"

    def wear(self):
        return "Take a look at my socks! They're gorgeous!"

    def sell(self):
        return "Buy my socks!"

clothing = Clothing()
socks = Socks()

print(socks.sell())
print(clothing.sell())

#Super function
class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return F"{self.name} is enjoying the {food}"

class Cat(Animal):
    def __init__(self, name, sleep):
        super().__init__(name)
        self.sleep = sleep

hurayra = Cat("hurayra", 10)
print(hurayra.name)
print(hurayra.sleep)

#Exercise
# Declare a Musician class that accepts a name argument in its initialization.
# The initialization should assign a name argument to a name attribute. 
# In addition, each Musician object should have an "albums" attribute 
# that begins as an empty list.
# Define a release_album instance method on a Musician that accepts a title (string). 
# It should append the string to the end of the list held by the
# albums attribute (see examples below).
#
# Declare a Drummer subclass than inherits from the Musician superclass. 
# In addition to a name, a drummer should also have a stamina attribute 
# represented by an integer. 
# The subclass should invoke the Musician superclass’s initialization procedure
# and pass it the drummer’s name.
# It should also set the stamina attribute in its own initialization process.
#
# EXAMPLE:
# lars = Drummer(name = "Lars", stamina = 2)
# print(lars.name)   # "Lars"
# print(lars.stamina) # 2
# print(lars.albums) # []
#
# lars.release_album("Ride the Lightning")
# print(lars.albums) # ["Ride the Lightning"]
#
# lars.release_album("Master of Puppets")
# print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']

class Musician():
    def __init__(self, name):
        self.name = name
        self.albums = []

    def release_album(self,title):
        return self.albums.append(title)

class Drummer(Musician):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina

lars = Drummer(name = "Lars", stamina = 2)
print(lars.name)   # "Lars"
print(lars.stamina) # 2
print(lars.albums) # []

lars.release_album("Ride the Lightning")
print(lars.albums) # ["Ride the Lightning"]

lars.release_album("Master of Puppets")
print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
        leap = True

    else: 
        leap = False
    
    return leap
year = 1800
print(is_leap(year))



