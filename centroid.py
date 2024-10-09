import point as P
import math as m
import matplotlib.pyplot as plt
import triangle as T


class Centroid(P.Point):
    def __init__(self, coord, soort):
        super().__init__(coord)
        self.soort = soort

    def getSoort(self):
        return self.soort

    def getConnect(self):
        x1, y1 = self.getX(), self.getY()
        if self.getSoort() == 'beta':
            driehoek = T.Triangle(self, 'beta')
            hoeken = driehoek.getVertices()
            top = hoeken[0].plus(hoeken[1]).plus(hoeken[0].plus(P.Point((0, 1)))).times(1 / 3)
            bottom = hoeken[0].plus(hoeken[2]).plus(hoeken[0].plus(P.Point((0, -1)))).times(1 / 3)
            left = hoeken[1].plus(hoeken[2]).plus(hoeken[1].plus(P.Point((-m.cos(m.pi / 6), -m.sin(m.pi / 6))))).times(1 / 3)
            return [Centroid((left.getX(), left.getY()), 'alpha'), Centroid((top.getX(), top.getY()), 'alpha'), Centroid((bottom.getX(), bottom.getY()), 'alpha')]
        else:
            driehoek = T.Triangle(self, 'beta')
            hoeken = driehoek.getVertices()
            top = hoeken[0].plus(hoeken[1]).plus(hoeken[0].plus(P.Point((0, 1)))).times(1 / 3)
            bottom = hoeken[0].plus(hoeken[2]).plus(hoeken[0].plus(P.Point((0, -1)))).times(1 / 3)
            left = hoeken[1].plus(hoeken[2]).plus(hoeken[1].plus(P.Point((m.cos(m.pi / 6), -m.sin(m.pi / 6))))).times(1 / 3)
            return [Centroid((left.getX(), left.getY()), 'alpha'), Centroid((top.getX(), top.getY()), 'alpha'), Centroid((bottom.getX(), bottom.getY()), 'alpha')]

    def drawPoint(self):
        if self.getSoort() == 'alpha':
            plt.plot(self.getX(), self.getY(), color='white', marker='o', markeredgecolor='black')
            txt = (self.getX(), self.getY() + 0.1)
        else:
            super().draw('black', 'o')
            txt = (self.getX() + 0.1, self.getY())

    def draw(self, col, style):
        self.drawPoint()
        for p in self.getConnect():
            self.connect(p, col, style)

    def equals(self, p):
        return super().equals(p) and self.getSoort() == p.getSoort()

    def find(self, lst):
        for val in lst:
            if self.equals(val):
                return True
        return False
