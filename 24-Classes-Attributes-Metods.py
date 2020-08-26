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