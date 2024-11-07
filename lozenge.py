import triangle as T
import centroid as C
import matplotlib.pyplot as plt


class Lozenge:
    def __init__(self, beta, soort):
        self.base = beta
        self.soort = soort

    def getSoort(self):
        return self.soort

    def getBase(self):
        return self.base

    def getCentroids(self):
        base = self.getBase()
        neighbours = base.getConnect()
        soort = self.getSoort()
        centroids = [base]
        if soort == 'Up':
            centroids.append(neighbours[1])
        elif soort == 'Down':
            centroids.append(neighbours[2])
        else:
            centroids.append(neighbours[0])
        return centroids

    def getVertices(self):
        centroids = self.getCentroids()
        soort = self.getSoort()
        driehoekBeta = T.Triangle(centroids[0], 'beta')
        driehoekAlpha = T.Triangle(centroids[1], 'alpha')
        vertBeta = driehoekBeta.getVertices()
        vertAlpha = driehoekAlpha.getVertices()
        if soort == 'Up':
            vertBeta.append(vertAlpha[1])
        if soort == 'Down':
            vertBeta.append(vertAlpha[2])
        elif soort == 'Left':
            vertBeta.append(vertAlpha[0])
        return vertBeta

    def drawDime(self):
        centres = self.getCentroids()
        centres[0].connect(centres[1], 'red', '-')

    def draw(self):
        color = 'black'
        style = '-'
        vert = self.getVertices()
        soort = self.getSoort()
        if soort == 'Up':
            vert[0].connect(vert[2], color, style)
            vert[2].connect(vert[1], color, style)
            vert[1].connect(vert[3], color, style)
            vert[3].connect(vert[0], color, style)
        elif soort == 'Down':
            vert[0].connect(vert[1], color, style)
            vert[1].connect(vert[2], color, style)
            vert[2].connect(vert[3], color, style)
            vert[3].connect(vert[0], color, style)
        elif soort == 'Left':
            vert[0].connect(vert[1], color, style)
            vert[1].connect(vert[3], color, style)
            vert[3].connect(vert[2], color, style)
            vert[2].connect(vert[0], color, style)

    def drawPath(self, soort):
        color = 'red'
        colP = 'green'
        style = '-'
        mark = 'o'
        lozSoort = self.getSoort()
        hoekpunten = self.getVertices()
        if lozSoort == 'Up':
            if soort == 'LR':
                m1 = hoekpunten[0].plus(hoekpunten[3]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[2]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
            elif soort == 'ROLB':
                m1 = hoekpunten[0].plus(hoekpunten[2]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
        elif lozSoort == 'Down':
            if soort == 'LR':
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
        elif lozSoort == 'Left':
            if soort == 'ROLB':
                m1 = hoekpunten[0].plus(hoekpunten[2]).times(1 / 2)
                m2 = hoekpunten[1].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)
            elif soort == 'LORB':
                m1 = hoekpunten[0].plus(hoekpunten[1]).times(1 / 2)
                m2 = hoekpunten[2].plus(hoekpunten[3]).times(1 / 2)
                m1.connect(m2, color, style)
                m1.draw(colP, mark)
                m2.draw(colP, mark)