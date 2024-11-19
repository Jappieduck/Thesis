import math as m
import point as P
import centroid as C


# A class for representing a regular hexagon
class Hexagon:
    # we define the hexagon based on its center, if it is 'standing" or 'lying down',
    # meaning two parallel lines being vertical respectively being horizontal, and the length of its sides
    def __init__(self, centrum, soort, length):
        self.centre = centrum
        self.soort = soort
        self.length = length

    # Some getters
    def getCentre(self):
        return self.centre

    def getSoort(self):
        return self.soort

    def getLength(self):
        return self.length

    # calculate the vertices of the hexagon
    def getHoekpunten(self):
        B = P.Point((0, 1))
        O = P.Point((0, -1))
        L = P.Point((-1, 0))
        R = P.Point((1, 0))
        if self.getSoort() == 'Standing':
            l = self.getLength()
            c = self.getCentre()
            p1 = c.plus(B.times(l))
            p2 = c.plus(P.Point((m.cos(m.pi / 6), m.sin(m.pi / 6))).times(l))
            p3 = c.plus(P.Point((m.cos(m.pi / 6), -m.sin(m.pi / 6))).times(l))
            p4 = c.plus(O.times(l))
            p5 = c.plus(P.Point((-m.cos(m.pi / 6), -m.sin(m.pi / 6))).times(l))
            p6 = c.plus(P.Point((-m.cos(m.pi / 6), m.sin(m.pi / 6))).times(l))
        else:
            l = self.getLength()
            c = self.getCentre()
            p1 = c.plus(R.times(l))
            p2 = c.plus(P.Point((m.cos(m.pi / 3), -m.sin(m.pi / 3))).times(l))
            p3 = c.plus(P.Point((-m.cos(m.pi / 3), -m.sin(m.pi / 3))).times(l))
            p4 = c.plus(L.times(l))
            p5 = c.plus(P.Point((-m.cos(m.pi / 3), m.sin(m.pi / 3))).times(l))
            p6 = c.plus(P.Point((m.cos(m.pi / 3), m.sin(m.pi / 3))).times(l))
        return [p1, p2, p3, p4, p5, p6]

    # draw the hexagon the data represents
    def draw(self, color):
        vert = self.getHoekpunten()
        kleurpunten = []
        for i in range(len(vert)):
            vert[i].connect(vert[(i + 1) % 6], color, '-')
