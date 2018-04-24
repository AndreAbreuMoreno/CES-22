class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):    # All we have done is renamed the method
            return "({0}, {1})".format(self.x, self.y)


class Rectangle:

    def __init__(self, pos, w, h):
        self.corner = pos
        self.w = w
        self.h = h

    def __str__(self):
        return "({}, {}, {})".format(self.corner, self.w, self.h)

    def overlapping_rectangle(self,r2):
        if (self.corner.x > (r2.corner.x + r2.w) or r2.corner.x>(self.corner.x + self.w)):
            return False

        if ((self.corner.y + self.h)< r2.corner.y or (r2.corner.y+r2.h)<self.corner.y):
            return False

        return True

r1 = Rectangle(Point(0,0),10,10)
r2 = Rectangle(Point(11,11),10,10)
r3 = Rectangle(Point(5,0),10,10)
r4 = Rectangle(Point(0,5),10,10)
print("retangulo 1 =",r1)
print("retangulo 2 =",r2, "\nretangulo 3 =",r3, "\nretangulo 4 =",r4)
print("\nTest r1.overlapping_rectangle(r2) = {}".format(r1.overlapping_rectangle(r2)))
print("\nTest r1.overlapping_rectangle(r3) = {}".format(r1.overlapping_rectangle(r3)))
print("\nTest r1.overlapping_rectangle(r4) = {}".format(r1.overlapping_rectangle(r4)))
print("\nTest r2.overlapping_rectangle(r1) = {}".format(r2.overlapping_rectangle(r1)))
print("\nTest r2.overlapping_rectangle(r3) = {}".format(r2.overlapping_rectangle(r3)))
print("\nTest r2.overlapping_rectangle(r4) = {}".format(r2.overlapping_rectangle(r4)))
print("\nTest r3.overlapping_rectangle(r1) = {}".format(r3.overlapping_rectangle(r1)))
print("\nTest r3.overlapping_rectangle(r2) = {}".format(r3.overlapping_rectangle(r2)))
print("\nTest r3.overlapping_rectangle(r4) = {}".format(r3.overlapping_rectangle(r4)))