import sushi
import math

# print(sushi.__doc__)
# print(sushi.fish.__doc__)
# print(sushi.Salmon.__doc__)
# print(sushi.Salmon.bake.__doc__)
# print(math.__doc__)
# print(math.sqrt.__doc__)

help(sushi)

class CollegeStudent():
    """
    A blueprint for a student at a higer institution
    """
    def __init__(self, university):
        self.university = university

    def sleep(self):
        """
        sleep through class
        """
        pass
    def eat(self):
        """
        Go to the Cafteria
        """
        pass
    def party(self):
        """
        Hit the books hard
        """
        pass

qossim = CollegeStudent("Python Community College")
print(qossim.sleep.__doc__)
print(qossim.eat.__doc__)
print(qossim.party.__doc__)
