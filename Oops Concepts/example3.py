"""
OOPS Principles
    - Inhertance
            Enhancing the existing class features
    - Polymorphsim
            Samething(same method) in many forms
    - Encapsulation
            Binding a data with methods
    - Abstraction
            Hiding the data
"""

class Shape:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return ("x: {} y: {}".format(self.x, self.y))

#s1 = Shape(10, 20)
#print(s1)

class Rect:

    def __init__(self, xcor, ycor, ht, width):
        self.x = xcor
        self.y = ycor
        self.h = ht
        self.w = width

    def __str__(self):
         return ("x: {} y: {} h: {} w: {}".format(self.x, self.y, self.h, self.w))
        

r1 = Rect(10, 20, 30, 40)
print(r1)




