import matplotlib.pyplot as plt


class Point:
    def __init__(self, coord):
        x, y = coord
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def plus(self, p):
        return Point((self.getX() + p.getX(), self.getY() + p.getY()))

    def times(self, c):
        return Point((c * self.getX(), c * self.getY()))

    def equals(self, p):
        return self.getX() == p.getX() and self.getY() == p.getY()

    def draw(self, col, mark):
        x, y = self.getX(), self.getY()
        plt.plot(x, y, color=col, marker=mark)

    def connect(self, p, color, style):
        x1, y1 = self.getX(), self.getY()
        x2, y2 = p.getX(), p.getY()
        plt.plot([x1, x2], [y1, y2], color=color, linestyle=style)

    def find(self, lst):
        for value in lst:
            if self.equals(value):
                return True
        return False
