#Instance method
class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaaar!")

    def describe(self):
        print(f"I am a {self.name}. I am a {self.specialty} Pokemon")

    def take_damage(self, amount):
        self.health -= amount


squirtle = Pokemon("Squirtle", "water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 110)
squirtle.roar()
charmander.roar()
squirtle.describe()
charmander.describe()
print(squirtle.health)

squirtle.take_damage(10)
print(squirtle.health)

#Exercise 1
class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income

    def enter_club(self):
        if self.age < 21:
            return "Accedd denied!"
        else:
            return "Access granted!"

    def play_show(self):
        self.income += 5

cliff = Musician(age = 27, income = 0)
print(cliff.age)
print(cliff.enter_club())
print(cliff.income)
cliff.play_show()
print(cliff.income)
cliff.play_show()
print(cliff.income)

#Protected Attributes and Methods
class Smartphone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10

    def get_os_version(self):
        return self._firmware
    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1

iphone = Smartphone()
print(iphone._firmware)
print(iphone._company)
iphone.update_firmware()
print(iphone._firmware)

#practice
print(iphone._firmware)
samsung = Smartphone()
print(samsung._firmware)

#Exercise 2
class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

    def copyright(self):
        return F"Copyright {self._author}, {self._publisher}"
        

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        else:
            self.page_count = 0

book = Book(author = "Grant Cardone", publisher = "10X Expression", page_count = 10)

print(book.copyright())
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)
book.rip_in_half()
print(book.page_count)

# Defining properties with property method
class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12
    
    feet = property(_get_feet, _set_feet)

h = Height(5)
print(h.feet)

h.feet = 6
print(h.feet)

h.feet = -10
print(h.feet)

#Defining Properties with Decorators
class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

h = Currency(10000)
print(h.dollars)

h.dollars = 500000
print(h.dollars)

h.dollars = -10000
print(h.dollars)


#Exercise 2
class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    @property
    def slices_eaten(self):
        return self._slices_eaten

    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten

    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices

cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage)

cheese.slices_eaten = 4
print(cheese.slices_eaten)

cheese.slices_eaten  = 10
print(cheese.percentage)

# cheese.percentage = 0.5 
# print(cheese.percentage)

#The geattr and the setattr Functions
stats = {
    "name": "BBQ Chicken",
    "size": "Extra Large",
    "price": 19.99,
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
    }

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)
bbq = Pizza(stats)
print(bbq.size)
print(bbq.ingredients)

for attr in  ["name", "ingredients", "diameter", "discounted"]:
    print(getattr( bbq, attr, "Unknown"))

#The hasattr and delattr Functions
stats = {
    "name": "BBQ Chicken",
    "size": "Extra Large",
    "price": 19.99,
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
    }

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)
bbq = Pizza(stats)
print(bbq.size)
stats_to_delete = ["size", "diameter", "discounted", "ingredients"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

#print(bbq.size)
print(bbq.price)
class Coffee():
    def __init__(self, cream, sugar, half_and_half):
        self.cream = cream
        self.sugar = sugar
        self.half_and_half = half_and_half

morning_joe = Coffee(True, False, True)
for val in ["cream",
    "pumpkin spice",
    "cinnamon",
    "sugar",
    "half_and_half"]:
    if hasattr(morning_joe, val):
        setattr(morning_joe, val, not getattr(morning_joe,val))

print(morning_joe.cream, morning_joe.sugar, morning_joe.half_and_half)

#Class Method
class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon = 0, tuna = 2, shrimp = 3, squid = 0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon = 1, tuna = 10, shrimp = 0, squid = 1)

boris = SushiPlatter(salmon = 0, tuna = 4, shrimp = 5, squid= 10)
print(boris.salmon)
print(boris.shrimp)

print(SushiPlatter.lunch_special_A().tuna)
print(SushiPlatter.tuna_lover().tuna)

class RicePlatter():
    def __init__(self, rice, chicken, fish, plantain):
        self.rice = rice
        self.chicken = chicken
        self.fish = fish
        self.polantain = plantain

    @classmethod
    def fish_lover(cls):
        return cls(rice = 5, chicken = 1, fish = 3, plantain = 1)

    @classmethod
    def chicken_lover(cls):
        return cls(rice = 5, fish = 1, chicken = 3, plantain = 1)

qossim = RicePlatter(rice = 6, chicken = 4, fish = 0, plantain = 1)
print(qossim.chicken)

fish_lover_A = RicePlatter.fish_lover()
print(fish_lover_A.chicken)

#Exercise
class Chocolate():
    def __init__(self, cocoa_content):
        self.cocoa_content = cocoa_content

    @classmethod
    def sweet(cls):
        return cls(cocoa_content = 30)

    @classmethod
    def semi_sweet(cls):
        return cls(cocoa_content = 50)

    @classmethod
    def bittersweet(cls):
        return cls(cocoa_content = 70)

    @classmethod
    def bitter(cls):
        return cls(cocoa_content = 99)

print(Chocolate.bitter().cocoa_content)
print(Chocolate.bittersweet().cocoa_content)

#Class Attributes 
class Counter():
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counter = (cls(), cls())
        print(f"New Numnber of objects created: {cls.count}")
        return two_counter

print(Counter.count)
c1 = Counter()
print(Counter.count)

c2, c3 = Counter.create_two()
print(Counter.count)

print(c1.count)
print(c2.count)
print(c3.count)

#Attribute lookup order
class Example():
    data = "Class Attribute!"

e1 = Example()
e2 = Example()

print(e1.data)
print(e2.data)

e1.data = "Instance Attribute!"
print(e1.data)
print(e2.data)

#print(e1.nonsense)

#Static method
class WeatherForecast():
    def __init__(self, temperatures):
        self.temperatures = temperatures

    @staticmethod
    def convert_farh_to_cels(farh):
        calculation = (5/9) * (farh - 32)
        return round(calculation, 2)

    def in_celsius(self):
        return [self.convert_farh_to_cels(temp) for temp in self.temperatures]

wf = WeatherForecast([100, 200, 300, 40, 50])
print(wf.in_celsius())

print(WeatherForecast.convert_farh_to_cels(100))
