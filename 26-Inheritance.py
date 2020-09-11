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

#Polymorphism
class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height

values = [
    "Boris",
    [1, 2, 3],
    [4, 5, 6, 7],
    {"a": 1, "b": 3},
    Person(name = "Qossim", height = 71)
]

for value in values:
    print(len(value))
import random

class Player():
    def __init__(self, game_played, victories):
        self.game_played = game_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.game_played

class HumanPlayer(Player):
    def make_move(self):
        print("Let player make the decision!")

class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move!")

hp = HumanPlayer(30, 15)
cp = ComputerPlayer(game_played = 1000, victories = 999)
print(hp.win_ratio)
print(cp.win_ratio)    

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move()

#exercise
# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.

# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"

# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"

# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"

# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
# Instantiate an instance of a Floss and assign it a "floss" variable.
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.

# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.
 
# Import the "random" module (see last lesson for reference). 
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list. 
# This will mutate the list, randomizing the order of its elements.

# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.

class DentalHealthItem():
    def __init__(self, price):
        self.price = price 

class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"
    
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"

class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"

toothbrush = Toothbrush(15)
floss = Floss(20)
mouthwash = Mouthwash(10)

dental_health_kit = [toothbrush, floss, mouthwash]
item = random.shuffle(dental_health_kit)
actions = [value.use() for value in dental_health_kit]
# print(item.use())
print(actions)

#Name Mangling for Privacy
class Nonsense():
    def __init__(self):
        self.__some_attributes = "Hello"

    def __some_methods(self):
        print("This is coming from some methos!")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()
# print(n.__some_attributes)
# print(sn.some_attributes)
# n.__some_methods()
# sn.__some_methods()
print(n._Nonsense__some_attributes)
n._Nonsense__some_methods()
sn._Nonsense__some_methods()
print(sn._Nonsense__some_attributes)

# Multiple Inheritance
class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")

    def store(self):
        print("Putting in the Refrigerator")

class Desert():
    def add_weight(self):
        print("Putting on the pounds!")
    def store(self):
        print("Putting in the Freezer!")

class IceCream(FrozenFood, Desert):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store()

print(IceCream.mro())

#Multiple Inheritance: depth first search and bread first search
class Restaurant():
    def make_reservation(self, party_size):
        print(F"Booked a table for {party_size}")

class Stakehouse(Restaurant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(F"Booked a Lounge for {party_size}")

class BarAndGrill(Stakehouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)
print(BarAndGrill.mro())

#Multiple Inheritance: Diamond-Shaped Inheritance
class Filmaker():
    def give_interview(self):
        print("I love making movies")

class Director(Filmaker):
    pass

class Screenwriter(Filmaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(Director, Screenwriter):
    pass

stallone = JackOfAllTrades()
stallone.give_interview()
print(JackOfAllTrades.mro())

#Exercise
class A():
    def dispatch(self):
        return "apple"

class B(A):
    pass

class C(A):
    def dispatch(self):
        return "banana"

class D(B, C):
    pass

my_obj = D()
print(my_obj.dispatch())

