import abc

class Sandwich(object):
    def __init__(self, bread, sauce):
        self.bread = bread
        self.sauce = sauce

    def get_bread(self):
        return "The bread is {}".format(self.bread)

    @staticmethod
    def get_sauce(sauce):
        return "The sauce is {}".format(str(sauce))

    @classmethod
    def double_sauce(cls):
        return "Double of {}".format(cls.sauce)

    @abc.abstractmethod
    def grilled_sandwich():
        pass

class GrillSandwich(Sandwich):
    def __init__(self, time):
        self.time = time

    def grilled_sandwich(self):
        return "In the oven for {} min".format(self.time)