import math as m
import point as P


# Class to represent triangles
class Triangle:
    # We only work with two kind of triangles, so the kind of triangle and the center is enough to define it
    def __init__(self, centre, soort):
        self.soort = soort
        self.centre = centre

    # some getters
    def getSoort(self):
        return self.soort

    def getCentre(self):
        return self.centre

    # Calculate the vertices of the triangle
    def getVertices(self):
        C = P.Point((self.getCentre().getX(), self.getCentre().getY()))
        if self.getSoort() == "alpha":
            a = P.Point((-m.sqrt(3)/3, 0)).plus(C)
            b = P.Point((m.sqrt(3)/6, 1/2)).plus(C)
            c = P.Point((m.sqrt(3)/6, -1/2)).plus(C)
        else:
            a = P.Point((m.sqrt(3)/3, 0)).plus(C)
            b = P.Point((-m.sqrt(3)/6, 1/2)).plus(C)
            c = P.Point((-m.sqrt(3)/6, -1/2)).plus(C)
        return [a, b, c]

    # check if two triangles represent the same triangle
    def equals(self, T):
        if self.getSoort() == T.getSoort() and self.getCentre().equals(T.getCentre()):
            return True
        else:
            return False

    # draw the triangle
    def draw(self, color, soort):
        vert = self.getVertices()
        vert[0].connect(vert[1], color, soort)
        vert[1].connect(vert[2], color, soort)
        vert[0].connect(vert[2], color, soort)