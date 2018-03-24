class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return print("{}".format(self.y/self.x))


print("Point(4,10).slope_from_origin()")
Point(4,10).slope_from_origin()
print("\nPoint(5,5).slope_from_origin()")
Point(5,5).slope_from_origin()
print("\nPoint(10,1).slope_from_origin()")
Point(10,1).slope_from_origin()