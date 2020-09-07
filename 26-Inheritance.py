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