class Shape:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return ("x: {} y: {}".format(self.x, self.y))


class Rect(Shape):

    def __init__(self, xcor, ycor, ht, width):
        #self.x = xcor
        #self.y = ycor
        Shape.__init__(self, xcor, ycor)
        self.h = ht
        self.w = width

    def __str__(self):
         return ("x: {} y: {} h: {} w: {}".format(self.x, self.y, self.h, self.w))


r1 = Rect(100, 200, 300, 400)
print(r1)
