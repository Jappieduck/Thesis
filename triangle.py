import math as m
import point as P
import Drawing as D


class Triangle:
    def __init__(self, centre, soort):
        self.soort = soort
        self.centre = centre

    def getSoort(self):
        return self.soort

    def getCentre(self):
        return self.centre

    def getVertices(self):
        C = self.getCentre()
        if self.getSoort() == "alpha":
            a = P.Point((-m.sqrt(3)/3, 0)).plus(C)
            b = P.Point((m.sqrt(3)/6, 1/2)).plus(C)
            c = P.Point((m.sqrt(3)/6, -1/2)).plus(C)
        else:
            a = P.Point((m.sqrt(3)/3, 0)).plus(C)
            b = P.Point((-m.sqrt(3)/6, 1/2)).plus(C)
            c = P.Point((-m.sqrt(3)/6, -1/2)).plus(C)
        return [a, b, c]

    def equals(self, T):
        if self.getSoort() == T.getSoort() and self.getCentre().equals(T.getCentre()):
            return True
        else:
            return False

    def draw(self, color, soort):
        vert = self.getVertices()
        vert[0].connect(vert[1], color, soort)
        vert[1].connect(vert[2], color, soort)
        vert[0].connect(vert[2], color, soort)