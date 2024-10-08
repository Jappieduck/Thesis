import math as m
import point as P
import Drawing as D
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, point, soort):
        self.basis = point
        self.soort = soort

    def getType(self):
        return self.soort

    def getPoint(self):
        return self.basis

    def getConnect(self):
        p = self.getPoint()
        x1, y1 = p.getX(), p.getY()
        if self.getType() == 'beta':
            left = x1 - 1, y1
            top = x1 + (1 / 2), y1 + (m.sqrt(3) / 2)
            bottom = x1 + (1 / 2), y1 - (m.sqrt(3) / 2)
            return [Vertex(P.Point(left), 'alpha'), Vertex(P.Point(top), 'alpha'), Vertex(P.Point(bottom), 'alpha')]
        else:
            right = x1 + 1, y1
            top = x1 - (1 / 2), y1 + (m.sqrt(3) / 2)
            bottom = x1 - (1 / 2), y1 - (m.sqrt(3) / 2)
            return [Vertex(P.Point(right), 'beta'), Vertex(P.Point(top), 'beta'), Vertex(P.Point(bottom), 'beta')]

    def equal(self, p):
        if self.getPoint().equals(p.getPoint()) and self.getType() == p.getType():
            return True
        else:
            return False

    def present(self, lst):
        for p in lst:
            if self.equal(p):
                return True
        return False

    def drawBase(self):
        p = self.getPoint()
        if self.getType() == 'alpha':
            plt.plot(p.getPoint().getX(), p.getPoint().getY(), color='white', marker='o', markeredgecolor='black')
            txt = (p.getPoint().getX(), p.getPoint().getY() + 0.1)
            plt.annotate(r'$\alpha$', xy=txt)
        else:
            p.draw('black', 'o')
            txt = (p.getPoint().getX() + 0.1, p.getPoint().getY())
            plt.annotate(r'$\beta$', xy=txt)

    def drawEdges(self):
        for p in self.getConnect():
            D.connect(self.getPoint(), p.getPoint(), 'black', '-')

    def drawFull(self):
        self.drawEdges()
        self.drawBase()