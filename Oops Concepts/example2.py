"""
Dunder methods or attributes: double under score methods
__init__
__str__
__repr__
__name__
__closure__
__doc__
__call__
__iter__
"""


class Student:


    def __init__(self, name, ht):
        self.name = name
        self.ht = ht

    def display(self):
        print("Name: {} Ht: {}".format(self.name, self.ht))

    #tostring method
    def __str__(self):
        return("Name: {} Ht: {}".format(self.name, self.ht))


s1 = Student("S1", "24")

s2 = Student("S2", "25")
print(s2)  # Returns address of an object
