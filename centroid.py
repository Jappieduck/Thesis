import point as P
import math as m
import matplotlib.pyplot as plt
import triangle as T


# A class which represents an apha or beta triangle using its centroid
class Centroid(P.Point):
    # Extends the class point, since a centroid is also a point,
    # but with extra information about the triangle it represents,
    # namely which kind of triangle (alpha or beta) and if it is connected to some other point
    def __init__(self, coord, soort):
        super().__init__(coord)
        self.soort = soort
        self.connected = False

    # Some getters to get information
    def getSoort(self):
        return self.soort

    def getConnection(self):
        return self.connected

    # Setter to change its connection status
    def setConnection(self, boolean):
        self.connected = boolean

    # Find all adjecent centroids, which are of the opposite kind of centroid
    def getConnect(self):
        if self.getSoort() == 'beta':
            driehoek = T.Triangle(self, 'beta')
            hoeken = driehoek.getVertices()
            top = hoeken[0].plus(hoeken[1]).plus(hoeken[0].plus(P.Point((0, 1)))).times(1 / 3)
            bottom = hoeken[0].plus(hoeken[2]).plus(hoeken[0].plus(P.Point((0, -1)))).times(1 / 3)
            left = hoeken[1].plus(hoeken[2]).plus(hoeken[1].plus(P.Point((-m.cos(m.pi / 6), -m.sin(m.pi / 6))))).times(
                1 / 3)
            return [Centroid((left.getX(), left.getY()), 'alpha'), Centroid((top.getX(), top.getY()), 'alpha'),
                    Centroid((bottom.getX(), bottom.getY()), 'alpha')]
        else:
            driehoek = T.Triangle(self, 'alpha')
            hoeken = driehoek.getVertices()
            top = hoeken[0].plus(hoeken[1]).plus(hoeken[0].plus(P.Point((0, 1)))).times(1 / 3)
            bottom = hoeken[0].plus(hoeken[2]).plus(hoeken[0].plus(P.Point((0, -1)))).times(1 / 3)
            left = hoeken[1].plus(hoeken[2]).plus(hoeken[1].plus(P.Point((m.cos(m.pi / 6), -m.sin(m.pi / 6))))).times(
                1 / 3)
            return [Centroid((left.getX(), left.getY()), 'alpha'), Centroid((top.getX(), top.getY()), 'alpha'),
                    Centroid((bottom.getX(), bottom.getY()), 'alpha')]

    # Draw the centroid itself in black if it is of kind beta, and white if it is an alpha
    def drawPoint(self):
        if self.getSoort() == 'alpha':
            plt.plot(self.getX(), self.getY(), color='white', marker='o', markeredgecolor='black')
            txt = (self.getX(), self.getY() + 0.1)
        else:
            super().draw('black', 'o')
            txt = (self.getX() + 0.1, self.getY())

    # Method to draw the centroid and its adjacent centroids with their connection
    def draw(self, col, style):
        self.drawPoint()
        for p in self.getConnect():
            self.connect(p, col, style)

    # Method to check if two centroids represent the same triangle
    def equals(self, p):
        return super().equals(p) and self.getSoort() == p.getSoort()

    # Method to find a centroid in a list which represents the same triangle
    def find(self, lst):
        for val in lst:
            if self.equals(val):
                return True
        return False

    # A way to connect the centroid with some other point
    def connect(self, p, color, style):
        super().connect(p, color, style)
        self.setConnection(True)
        p.setConnection(True)
