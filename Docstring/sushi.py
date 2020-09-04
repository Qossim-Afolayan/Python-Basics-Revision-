"""
A module about the joy of sushi 
Npo fishy code found here!
"""
def fish():
    """
    Detrmines if fish is a good meal choice
    Always return True, because it always is
    """
    return True

class Salmon:
    """
    A blueprint for Salmon objects
    """
    def __init__(self):
        self.tastines = 10

    def bake(self):
        """Bake the fish in an oven
        """
        self.tastines += 1

    