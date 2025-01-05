import math as m
import point as P


# A class for representing lozenge tiles
class Lozenge:
    # We define the lozenge by its black point and what kind of lozenge it is, type L1, L2 or L3 in the paper
    def __init__(self, beta, alpha):
        self.beta = beta
        self.alpha = alpha

    # some getters
    def getBeta(self):
        return self.beta

    def getAlpha(self):
        return self.alpha

    # Find and return the vertices of the lozenge
    def getVertices(self):
        a = P.Point((m.sqrt(3) / 3, 0))
        b = P.Point((-m.sqrt(3) / 6, 0.5))
        c = P.Point((-m.sqrt(3) / 6, -0.5))
        black = self.getBeta()
        white = self.getAlpha()
        vert = []
        if white.getX() < black.getX():
            vert.append(black.plus(b))
            vert.append(black.plus(a))
            vert.append(black.plus(c))
            vert.append(white.plus(a.times(-1)))
        elif black.getY() < white.getY():
            vert.append(white.plus(a.times(-1)))
            vert.append(white.plus(c.times(-1)))
            vert.append(white.plus(b.times(-1)))
            vert.append(black.plus(c))
        elif black.getY() > white.getY():
            vert.append(black.plus(a))
            vert.append(white.plus(b.times(-1)))
            vert.append(white.plus(a.times(-1)))
            vert.append(black.plus(b))
        return vert

    # Draw the dimer corresponding to the lozenge tile
    def drawDime(self):
        centres = [self.getBeta(), self.getAlpha()]
        centres[0].connect(centres[1], 'red', '-')

    # Draw the lozenge tile
    def draw(self):
        color = 'black'
        style = '-'
        vert = self.getVertices()
        for i in range(4):
            vert[i].connect(vert[(i + 1) % 4], color, style)

    # Draw the path of the path system going through the lozenge, depending on what type of path construction used
    def drawPath(self, soort):
        color = 'red'
        colP = 'green'
        style = '-'
        mark = 'o'
        lozSoort = 'Down'
        beta = self.getBeta()
        alpha = self.getAlpha()
        if beta.getY() < alpha.getY():
            lozSoort = 'Up'
        if alpha.getX() < beta.getX():
            lozSoort = 'Left'
        hoekpunten = self.getVertices()
        if lozSoort == 'Up':
            if soort == 'LR':
                m1 = hoekpunten[0].plus(hoekpunten[3]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[2]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
            elif soort == 'ROLB':
                m1 = hoekpunten[0].plus(hoekpunten[1]).times(1 / 2)
                m2 = hoekpunten[2].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
        elif lozSoort == 'Down':
            if soort == 'LORB':
                m1 = hoekpunten[0].plus(hoekpunten[3]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[2]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
            elif soort == 'LR':
                m1 = hoekpunten[0].plus(hoekpunten[1]).times(1 / 2)
                m2 = hoekpunten[2].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
        elif lozSoort == 'Left':
            if soort == 'ROLB':
                m1 = hoekpunten[0].plus(hoekpunten[3]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[2]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
            elif soort == 'LORB':
                m1 = hoekpunten[0].plus(hoekpunten[1]).times(1 / 2)
                m2 = hoekpunten[2].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)