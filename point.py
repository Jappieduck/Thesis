import matplotlib.pyplot as plt
import math as m


# A class to easily work with points
class Point:
    # Only needs its x and y coordinates
    def __init__(self, coord):
        x, y = coord
        self.x = x
        self.y = y

    # returns the coordinates
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # define a way to add points together
    def plus(self, p):
        return Point((self.getX() + p.getX(), self.getY() + p.getY()))

    # scalar multiplication
    def times(self, c):
        return Point((c * self.getX(), c * self.getY()))

    # check if two points represent the same points
    def equals(self, p):
        return self.getX() == p.getX() and self.getY() == p.getY()

    # Draw the point
    def draw(self, col, mark):
        x, y = self.getX(), self.getY()
        plt.plot(x, y, color=col, marker=mark)

    # connect two points
    def connect(self, p, color, style):
        x1, y1 = self.getX(), self.getY()
        x2, y2 = p.getX(), p.getY()
        plt.plot([x1, x2], [y1, y2], color=color, linestyle=style)

    # Look if the point is inside a list
    def find(self, lst):
        for value in lst:
            if self.equals(value):
                return True
        return False
