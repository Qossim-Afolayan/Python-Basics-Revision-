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

#



