class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return print("{}".format(self.y/self.x))

    def get_line_to(self, p):
        a = (self.y - p.y)/(self.x - p.x)
        b = p.y - a*p.x
        return print("({0:},{1:})".format(a,b))


print("Point(4,11).get_line_to(Point(6,15))")
Point(4,11).get_line_to(Point(6,15))
print("\nPoint(5,5).get_line_to(Point(10,10))")
Point(5,5).get_line_to(Point(10,10))
