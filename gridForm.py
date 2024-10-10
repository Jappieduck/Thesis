import math as m
import centroid as C
import point as P
import triangle as T
import lozenge as L
import random

RB = P.Point((m.cos(m.pi / 6), m.sin(m.pi / 6)))
LB = P.Point((-m.cos(m.pi / 6), m.sin(m.pi / 6)))
B = P.Point((0, 1))


def rowNumbers(length):
    rows = []
    for i in range(length):
        rows.append(length + i)
    for i in range(length, 0, -1):
        rows.append(length + i)
    return rows


def get_Centroids(zeshoek):
    hoekenHexagon = zeshoek.getHoekpunten()

    c1 = hoekenHexagon[4]
    b1 = c1.plus(B)
    a1 = c1.plus(RB)
    P1 = a1.plus(b1).plus(c1).times(1 / 3)
    M1 = C.Centroid((P1.getX(), P1.getY()), 'beta')

    c2 = hoekenHexagon[2]
    b2 = c2.plus(B)
    a2 = c2.plus(LB)
    P2 = a2.plus(b2).plus(c2).times(1 / 3)
    M2 = C.Centroid((P2.getX(), P2.getY()), 'alpha')

    centroidsBeta = [M1]
    centroidsAlpha = [M2]
    rows = rowNumbers(zeshoek.getLength())
    ascending = True
    maximum = max(rows)
    for i in rows:
        if i == 0:
            for j in range(1, i):
                P1 = M1.plus(P.Point((0, j)))
                P2 = M2.plus(P.Point((0, j)))
                centroidsBeta.append(C.Centroid((P1.getX(), P1.getY()), 'beta'))
                centroidsAlpha.append(C.Centroid((P2.getX(), P2.getY()), 'alpha'))
            M1 = M1.plus(P.Point((m.cos(m.pi / 6), -m.sin(m.pi / 6))))
            M2 = M2.plus(P.Point((-m.cos(m.pi / 6), -m.sin(m.pi / 6))))
        else:
            if i == maximum:
                ascending = False
            if ascending:
                for j in range(i):
                    P1 = M1.plus(P.Point((0, j)))
                    P2 = M2.plus(P.Point((0, j)))
                    centroidsBeta.append(C.Centroid((P1.getX(), P1.getY()), 'beta'))
                    centroidsAlpha.append(C.Centroid((P2.getX(), P2.getY()), 'alpha'))
                M1 = M1.plus(P.Point((m.sqrt(3) / 2, -1 / 2)))
                M2 = M2.plus(P.Point((-m.sqrt(3) / 2, -1 / 2)))
            else:
                for j in range(i):
                    P1 = M1.plus(P.Point((0, j)))
                    P2 = M2.plus(P.Point((0, j)))
                    centroidsBeta.append(C.Centroid((P1.getX(), P1.getY()), 'beta'))
                    centroidsAlpha.append(C.Centroid((P2.getX(), P2.getY()), 'alpha'))
                M1 = M1.plus(P.Point((m.sqrt(3) / 2, 1 / 2)))
                M2 = M2.plus(P.Point((-m.sqrt(3) / 2, 1 / 2)))
    return centroidsBeta, centroidsAlpha


def fillHexagon(zeshoek, center):
    hoekenHexagon = zeshoek.getHoekpunten()
    hoekenHexagon[0].connect(hoekenHexagon[3], 'gray', 'dashed')
    beta, alpha = get_Centroids(zeshoek)
    for c in beta:
        punt = P.Point((c.getX(), c.getY()))
        driehoek = T.Triangle(punt, c.getSoort())
        driehoek.draw('gray', 'dashed')
        if center:
            c.drawPoint()
    zeshoek.draw('black')
    if center:
        for c in alpha:
            c.drawPoint()


def sorteer(lst, soort, lengte):
    rijen = []
    rows = rowNumbers(lengte)
    begin = 0
    for val in rows:
        newlst = []
        for i in range(begin, begin + val):
            newlst.append(lst[i])
        rijen.append(newlst[:])
        begin = begin + val
        for point in newlst:
            point.drawPoint()
    if soort == 'alpha':
        rijen.reverse()
    return rijen


def drawBipartitGraph(zeshoek):
    beta, alpha = get_Centroids(zeshoek)
    alpha.remove(alpha[0])
    beta.remove(beta[0])
    l = zeshoek.getLength()
    betaSorted = sorteer(beta, 'beta', l)
    alphaSorted = sorteer(alpha, 'alpha', l)
    for row in alphaSorted:
        for point in row:
            point.drawPoint()
    color = 'black'
    soort = '-'
    for i in range(len(betaSorted)):
        if i < l:
            for j in range(len(betaSorted[i])):
                betaSorted[i][j].connect(alphaSorted[i][j], color, soort)
                betaSorted[i][j].connect(alphaSorted[i][j + 1], color, soort)
                if i > 0:
                    betaSorted[i][j].connect(alphaSorted[i - 1][j], color, soort)
        else:
            for j in range(len(betaSorted[i])):
                betaSorted[i][j].connect(alphaSorted[i - 1][j], color, soort)
                if j != 0:
                    betaSorted[i][j].connect(alphaSorted[i][j - 1], color, soort)
                if j != len(betaSorted[i]) - 1:
                    betaSorted[i][j].connect(alphaSorted[i][j], color, soort)
    for c in beta:
        c.drawPoint()
    for c in alpha:
        c.drawPoint()


def isConnected(punt, lst):
    for c in lst:
        if punt.equals(c):
            return c.getConnection()


def randomTiling(zeshoek, soort):
    lozenges = []
    lengte = zeshoek.getLength()
    beta, alpha = get_Centroids(zeshoek)
    beta.remove(beta[0])
    alpha.remove(alpha[0])
    betaSorted = sorteer(beta, 'beta', lengte)
    alphaSorted = sorteer(alpha, 'alpha', lengte)
    for i in range(len(betaSorted)-1):
        if i >= lengte:
            if not betaSorted[i][len(betaSorted[i])-1].getConnection():
                betaSorted[i][-1].connect(alphaSorted[i][-1], 'red', '-')
                ruit = L.Lozenge(betaSorted[i][-1], 'Down')
                lozenges.append(ruit)
        for j in range(len(betaSorted[i])):
            c = betaSorted[i][j]
            if not c.getConnection():
                p = random.uniform(0, 1)
                kansen = [p, 1 - p]
                buren = []
                left = None
                top = None
                bottom = None
                if i > 0:
                    left = alphaSorted[i-1][j]
                if i < lengte:
                    top = alphaSorted[i][j]
                    bottom = alphaSorted[i][j+1]
                else:
                    if j == 0:
                        bottom = alphaSorted[i][j]
                    elif j < len(betaSorted[i])-1:
                        bottom = alphaSorted[i][j]
                        top = alphaSorted[i][j - 1]
                    else:
                        top = None
                if soort == 'Left':
                    if top is not None:
                        buren.append(top)
                    if bottom is not None:
                        buren.append(bottom)
                elif soort == 'Top':
                    if bottom is not None:
                        buren.append(bottom)
                    if left is not None:
                        buren.append(left)
                elif soort == 'Bottom':
                    if top is not None:
                        buren.append(top)
                    if left is not None:
                        buren.append(left)
                if len(buren) == 1:
                    buren[0].connect(c, 'red', '-')
                elif isConnected(buren[0], alpha):
                    buren[1].connect(c, 'red', '-')
                elif isConnected(buren[1], alpha):
                    buren[0].connect(c, 'red', '-')
                elif len(buren) > 1:
                    keuze = random.choices(buren, kansen)
                    punt = keuze[0]
                    punt.connect(c, 'red', '-')
        for j in range(len(alphaSorted[i])):
            punt = alphaSorted[i][j]
            if not punt.getConnection():
                if soort == 'Left':
                    punt.connect(betaSorted[i+1][j], 'red', '-')
                    lozenges.append(L.Lozenge(betaSorted[i+1][j], 'Left'))
                elif soort == 'Top':
                    punt.connect(betaSorted[i][j], 'red', '-')
                    lozenges.append(L.Lozenge(betaSorted[i][j], 'Bottom'))
                elif soort == 'Bottom':
                    lozenges.append(L.Lozenge(betaSorted[i][j], 'Top'))
    up = True
    for j in range(len(betaSorted[-1])):
        newUp = up
        c = betaSorted[-1][j]
        if c.getConnection():
            newUp = not up
        if newUp == up:
            if newUp:
                if j == len(betaSorted[-1])-1:
                    c.connect(alphaSorted[-1][j - 1], 'red', '-')
                    lozenges.append(L.Lozenge(c, 'Down'))
                else:
                    c.connect(alphaSorted[-1][j], 'red', '-')
                    lozenges.append(L.Lozenge(c, 'Up'))
            else:
                c.connect(alphaSorted[-1][j-1], 'red', '-')
                lozenges.append(L.Lozenge(c, 'Down'))
        up = newUp
    return alphaSorted[-1], lozenges


def isValid(alphas):
    for alpha in alphas:
        if not alpha.getConnection():
            return False
    return True


def drawLozenges(lst):
    for loz in lst:
        loz.draw()
