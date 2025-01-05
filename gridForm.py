import math as m
import centroid as C
import point as P
import triangle as T
import lozenge as L
import random


# Here are some methods used to draw different grids or repeating structures and methods needed to do so
def get_Centroids(zeshoek):
    black = []
    white = []
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    v0 = P.Point((0, 1))
    shift = P.Point((m.sqrt(3)/6, 0.5))
    n = zeshoek.getLength()
    for i in range(n):
        colB = []
        colW = []
        for j in range(n + i):
            b = (v0.times(j)).plus(v1.times(i)).plus(v2.times(n)).plus(shift)
            b = C.Centroid((b.getX(), b.getY()), 'beta')
            colB.append(b)
            if i > 0:
                w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
                w = C.Centroid((w.getX(), w.getY()), 'alpha')
                colW.append(w)
        black.append(colB)
        if len(colW) > 0:
            white.append(colW)
    for i in range(n, 2 * n):
        colB = []
        colW = []
        for j in range(i-n, 2*n):
            b = b = (v0.times(j)).plus(v1.times(i)).plus(v2.times(n)).plus(shift)
            b = C.Centroid((b.getX(), b.getY()), 'beta')
            colB.append(b)
            w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
            w = C.Centroid((w.getX(), w.getY()), 'alpha')
            colW.append(w)
        black.append(colB)
        white.append(colW)
    colW = []
    for j in range(n, 2*n):
        b = (v0.times(j)).plus(v1.times(2*n)).plus(v2.times(n)).plus(shift)
        w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
        w = C.Centroid((w.getX(), w.getY()), 'alpha')
        colW.append(w)
    white.append(colW)
    return black, white


# Fill a hexagon with triangles, and if needed also all the centroids
def fillHexagon(zeshoek, center):
    hoekenHexagon = zeshoek.getHoekpunten()
    hoekenHexagon[0].connect(hoekenHexagon[3], 'gray', 'dashed')
    beta, alpha = get_Centroids(zeshoek)
    for col in beta:
        for c in col:
            punt = P.Point((c.getX(), c.getY()))
            driehoek = T.Triangle(punt, c.getSoort())
            driehoek.draw('gray', 'dashed')
            if center:
                c.drawPoint()
        zeshoek.draw('black')
        if center:
            for col in alpha:
                for c in col:
                    c.drawPoint()


# Draw the bipartite graph corresponding to a certain hexagon
def drawBipartitGraph(zeshoek):
    beta, alpha = get_Centroids(zeshoek)
    l = zeshoek.getLength()
    for row in alpha:
        for point in row:
            point.drawPoint()
    color = 'black'
    soort = '-'
    for i in range(l):
        for j in range(len(beta[i])):
            beta[i][j].connect(alpha[i][j], color, soort)
            beta[i][j].connect(alpha[i][j + 1], color, soort)
            if i > 0:
                beta[i][j].connect(alpha[i - 1][j], color, soort)
    for i in range(l, 2 * l):
        for j in range(len(beta[i])):
            if j == 0:
                beta[i][j].connect(alpha[i][j], color, soort)
                beta[i][j].connect(alpha[i - 1][j], color, soort)
            elif j == len(beta[i]) - 1:
                beta[i][j].connect(alpha[i][j - 1], color, soort)
                beta[i][j].connect(alpha[i - 1][j], color, soort)
            else:
                beta[i][j].connect(alpha[i][j], color, soort)
                beta[i][j].connect(alpha[i][j - 1], color, soort)
                beta[i][j].connect(alpha[i - 1][j], color, soort)
    for col in beta:
        for c in col:
            c.drawPoint()
    for col in alpha:
        for c in col:
            c.drawPoint()


# check in a list of centroids if a certain centroid is connected inside that list
def isConnected(punt, lst):
    for c in lst:
        if punt.equals(c):
            return c.getConnection()


# Get all possible vertices to connect with whilst constructing a random tiling
def getPossibilities(count, n, alpha, i, j):
    poss = []
    if i < n:
        if not alpha[i][j].getConnection():
            poss.append(alpha[i][j])
        if not alpha[i][j + 1].getConnection():
            poss.append(alpha[i][j + 1])
    else:
        if j == 0:
            poss.append(alpha[i][j])
        elif j == len(alpha[i]) + 1:
            poss.append(alpha[i][j - 1])
        else:
            if not alpha[i][j - 1].getConnection():
                poss.append(alpha[i][j - 1])
            if n - count < len(alpha[i]) - j:
                poss.append(alpha[i][j])
    return poss


# Fill a hexagon randomly with lozenge tiles
# REMARK: this does not follow the probability distribution we constructed in the paper
def randomTiling(zeshoek):
    lozenges = []
    n = zeshoek.getLength()
    beta, alpha = get_Centroids(zeshoek)
    for p in beta[0]:
        p.setConnection(True)
    for i in range(len(beta)):
        count = 0
        for j in range(len(beta[i])):
            if i == 0 or alpha[i - 1][j].getConnection():
                count += 1
                pos = getPossibilities(count, n, alpha, i, j)
                if len(pos) == 1:
                    pos[0].setConnection(True)
                    lozenges.append(L.Lozenge(beta[i][j], pos[0]))
                else:
                    p = random.uniform(0, 1)
                    kansen = [p, 1 - p]
                    keuze = random.choices(pos, kansen)[0]
                    keuze.setConnection(True)
                    lozenges.append(L.Lozenge(beta[i][j], keuze))
        for j in range(len(alpha[i])):
            if not alpha[i][j].getConnection():
                lozenges.append(L.Lozenge(beta[i + 1][j], alpha[i][j]))
    return lozenges


# draw a list of lozenges
def drawLozenges(lst):
    for loz in lst:
        loz.draw()


# draw a list of dimers
def drawDimes(lst):
    for loz in lst:
        loz.drawDime()


# Draw the grid induced by the path system construction
def drawPathGrid(zeshoek, soort, weight):
    n = zeshoek.getLength()
    levels = []
    col = 'black'
    colW1 = 'blue'
    colW2 = 'green'
    style = '-'
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    up = P.Point((0, 1))
    a0 = P.Point((0, 0))
    z0 = P.Point((0, 0))
    if soort == "LR":
        a0 = a0.plus(up.times(0.5).plus(v2.times(n)))
        z0 = z0.plus(up.times(0.5).plus(v1.times(n)))
    elif soort == "ROLB":
        a0 = a0.plus(v2.times(0.5).plus(v1.times(n)))
        z0 = z0.plus(v2.times(0.5).plus(up.times(n)))
    elif soort == "LORB":
        a0 = a0.plus(v1.times(0.5).plus(up.times(n)))
        z0 = z0.plus(v1.times(0.5).plus(v2.times(n)))
    for i in range(2 * n + 1):
        level = []
        if i < n:
            if soort == "LR":
                for j in range(n + i):
                    level.append(a0.plus(v1.times(i)).plus(up.times(j)))
            elif soort == "ROLB":
                for j in range(n + i):
                    level.append(a0.plus(up.times(i)).plus(v2.times(j)))
            elif soort == "LORB":
                for j in range(n + i):
                    level.append(a0.plus(v2.times(i)).plus(v1.times(j)))
        elif soort == "LR":
            for j in range(3 * n - i):
                level.append(z0.plus(v2.times(2 * n - i)).plus(up.times(j)))
        elif soort == "LORB":
            for j in range(3 * n - i):
                level.append(z0.plus(up.times(2 * n - i)).plus(v1.times(j)))
        elif soort == "ROLB":
            for j in range(3 * n - i):
                level.append(z0.plus(v1.times(2 * n - i)).plus(v2.times(j)))
        levels.append(level.copy())

    for i in range(2 * n):
        if i < n:
            for j in range(n + i):
                if weight:
                    levels[i][j].connect(levels[i + 1][j], colW1, style)
                    levels[i][j].connect(levels[i + 1][j + 1], colW2, style)
                else:
                    levels[i][j].connect(levels[i + 1][j], col, style)
                    levels[i][j].connect(levels[i + 1][j + 1], col, style)
        else:
            for j in range(3 * n - i):
                if j == 0:
                    if weight:
                        levels[i][j].connect(levels[i + 1][j], colW2, style)
                    else:
                        levels[i][j].connect(levels[i + 1][j], col, style)
                elif j == 3 * n - i - 1:
                    if weight:
                        levels[i][j].connect(levels[i + 1][j - 1], colW1, style)
                    else:
                        levels[i][j].connect(levels[i + 1][j - 1], col, style)
                else:
                    if weight:
                        levels[i][j].connect(levels[i + 1][j], colW2, style)
                        levels[i][j].connect(levels[i + 1][j - 1], colW1, style)
                    else:
                        levels[i][j].connect(levels[i + 1][j], col, style)
                        levels[i][j].connect(levels[i + 1][j - 1], col, style)

    for level in levels:
        for punt in level:
            if weight:
                punt.draw(col, 'o')
            else:
                punt.draw("red", 'o')
