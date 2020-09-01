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
print(c)
print(str(c))
print(repr(c))

print(c.__str__())
print(c.__repr__())
