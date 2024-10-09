import math as m

import centroid as C
import point as P
import triangle as T

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


def getCentroids(zeshoek):
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


def fillHexagon(zeshoek):
    hoekenHexagon = zeshoek.getHoekpunten()
    hoekenHexagon[0].connect(hoekenHexagon[3], 'gray', 'dashed')
    beta, alpha = getCentroids(zeshoek)
    for c in beta:
        punt = P.Point((c.getX(), c.getY()))
        driehoek = T.Triangle(punt, c.getSoort())
        driehoek.draw('gray', 'dashed')
    zeshoek.draw('black')


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
    beta, alpha = getCentroids(zeshoek)
    alpha.remove(alpha[0])
    beta.remove(beta[0])
    l = zeshoek.getLength()
    betaSorted = sorteer(beta, 'beta', l)
    alphaSorted = sorteer(alpha, 'alpha', l)
    for row in alphaSorted:
        for point in row:
            point.drawPoint()
    color = 'red'
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
