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

bob = Student(maths = 90, physics = 90, writing = 90)
moe = Student(maths = 100, physics = 90, writing = 80)
joe = Student(maths = 45, physics = 40, writing = 50)

print(bob > joe)
print(bob + joe)
print(bob - joe)
print(joe <= bob)
print(bob <= joe)

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



