import math as m
import centroid as C
import point as P
import triangle as T
import lozenge as L
import random
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


# Here are some methods used to draw different grids or repeating structures and methods needed to do so
def get_Centroids(zeshoek):
    black = []
    white = []
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    v0 = P.Point((0, 1))
    shift = P.Point((m.sqrt(3) / 6, 0.5))
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
        for j in range(i - n, 2 * n):
            b = (v0.times(j)).plus(v1.times(i)).plus(v2.times(n)).plus(shift)
            b = C.Centroid((b.getX(), b.getY()), 'beta')
            colB.append(b)
            w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
            w = C.Centroid((w.getX(), w.getY()), 'alpha')
            colW.append(w)
        black.append(colB)
        white.append(colW)
    colW = []
    for j in range(n, 2 * n):
        b = (v0.times(j)).plus(v1.times(2 * n)).plus(v2.times(n)).plus(shift)
        w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
        w = C.Centroid((w.getX(), w.getY()), 'alpha')
        colW.append(w)
    white.append(colW)
    return black, white


# Fill a hexagon with triangles, and if needed also all the centroids
def fillHexagon(zeshoek, centroidType):
    center = True
    if centroidType != "black" or centroidType != "white":
        center = False
    n = zeshoek.getLength()
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
        if center:
            for col in alpha:
                for c in col:
                    c.drawPoint()
    for i in range(n):
        c = alpha[i][0]
        punt = P.Point((alpha[i][0].getX(), alpha[i][0].getY()))
        driehoek = T.Triangle(punt, c.getSoort())
        vert = driehoek.getVertices()
        vert[0].connect(vert[2], 'gray', 'dashed')
        if center:
            c.drawPoint()

        c = alpha[i][-1]
        punt = P.Point((c.getX(), c.getY()))
        driehoek = T.Triangle(punt, c.getSoort())
        vert = driehoek.getVertices()
        vert[0].connect(vert[1], 'gray', 'dashed')
        if center:
            c.drawPoint()

    col = alpha[-1]
    for c in col:
        punt = P.Point((c.getX(), c.getY()))
        driehoek = T.Triangle(punt, c.getSoort())
        vert = driehoek.getVertices()
        vert[2].connect(vert[1], 'gray', 'dashed')


# Give all the triangles of a certain type their enumeration
def naming(zeshoek, gridLength, centroidType):
    n = zeshoek.getLength()
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    v0 = P.Point((0, 1))
    for i in range(-gridLength, n):
        for j in range(-gridLength, n + i + gridLength):
            if centroidType == "black":
                p = (((v2.times(n)).plus(v0.times(j))).plus(v1.times(i))).plus(P.Point((m.sqrt(3) / 6, 1 / 2)))
                text = "$b_{" + str(i) + "," + str(j) + "}$"
                plt.annotate(text, (p.getX() - 0.16, p.getY() - 0.09))
    for i in range(n, 2 * n + gridLength):
        for j in range(i - gridLength - n, 2 * n + gridLength):
            if centroidType == "black":
                p = (((v2.times(n)).plus(v0.times(j))).plus(v1.times(i))).plus(P.Point((m.sqrt(3) / 6, 1 / 2)))
                text = "$b_{" + str(i) + "," + str(j) + "}$"
                plt.annotate(text, (p.getX() - 0.16, p.getY() - 0.09))


# Draw the bipartite graph corresponding to a certain hexagon
def drawBipartitGraph(zeshoek, weight):
    beta, alpha = get_Centroids(zeshoek)
    l = zeshoek.getLength()
    for row in alpha:
        for point in row:
            point.drawPoint()
    color = 'black'
    soort = '-'
    plt.rc('text', usetex=True)
    plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{amssymb}')
    for i in range(l):
        for j in range(len(beta[i])):
            beta[i][j].connect(alpha[i][j], color, soort)
            beta[i][j].connect(alpha[i][j + 1], color, soort)
            if i > 0:
                beta[i][j].connect(alpha[i - 1][j], color, soort)
            if weight and (i < 2 and j < 2):
                text1 = "$\mathfrak{a}_{" + str(i) + "," + str(j) + "}$"
                text2 = "$\mathfrak{b}_{" + str(i) + "," + str(j) + "}$"
                plt.annotate(text1, ((beta[i][j].getX() + alpha[i][j].getX()) / 2 - 0.17,
                                     (beta[i][j].getY() + alpha[i][j].getY()) / 2 - 0.1))
                plt.annotate(text2, (
                    (beta[i][j].getX() + alpha[i][j + 1].getX()) / 2 - 0.22,
                    (beta[i][j].getY() + alpha[i][j + 1].getY()) / 2))

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
def drawPathGrid(zeshoek, soort, weight, enum):
    n = zeshoek.getLength()
    col = 'black'
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    v0 = P.Point((0, 1))

    plt.rc('text', usetex=True)
    plt.rc('text.latex', preamble=r'\usepackage{amsmath} \usepackage{amssymb}')

    a00 = "$\mathfrak{a}_{0,0}"
    a01 = "$\mathfrak{a}_{0,1}"
    a10 = "$\mathfrak{a}_{1,0}"
    a11 = "$\mathfrak{a}_{1,1}"
    A = [[a00, a01], [a10, a11]]

    b00 = "$\mathfrak{b}_{0,0}"
    b01 = "$\mathfrak{b}_{0,1}"
    b10 = "$\mathfrak{b}_{1,0}"
    b11 = "$\mathfrak{b}_{1,1}"
    B = [[b00, b01], [b10, b11]]

    if soort == "LR":
        a0 = (v0.times(0.5)).plus(v2.times(n))
        for i in range(2 * n):
            if i < n:
                for j in range(n + i):
                    punt1 = (a0.plus(v1.times(i))).plus(v0.times(j))
                    punt2 = (a0.plus(v1.times(i + 1))).plus(v0.times(j))
                    punt3 = (a0.plus(v1.times(i + 1))).plus(v0.times(j + 1))
                    punt1.arrow(punt2, col)
                    punt1.arrow(punt3, col)
                    if (i == 0 or j == 0) and enum:
                        eps1, eps2 = 0, 0
                        if i == 0:
                            eps1 = -0.6
                        else:
                            eps1 = -0.7
                            eps2 = -0.7
                        plt.annotate("$p_{" + str(i) + "," + str(j) + "}^{(1)}$",
                                     (punt1.getX() + eps1, punt1.getY() + eps2))
                    if weight and i < 2 and j < 2:
                        p1 = (punt1.plus(punt2)).times(0.5)
                        p2 = (punt1.plus(punt3)).times(0.5)
                        A[i][j] = A[i][j] + "^{(1)}$"
                        B[i][j] = B[i][j] + "^{(1)}$"
                        plt.annotate(A[i][j], (p1.getX() - 0.3, p1.getY() - 0.2))
                        plt.annotate(B[i][j], (p2.getX() + 0.1, p2.getY() - 0.2))
                    punt1.draw("red", "o")
                    punt2.draw("red", "o")
                    punt3.draw("red", "o")
            else:
                for j in range(i - n, 2 * n):
                    punt1 = (a0.plus(v1.times(i))).plus(v0.times(j))
                    punt2 = (a0.plus(v1.times(i + 1))).plus(v0.times(j))
                    punt3 = (a0.plus(v1.times(i + 1))).plus(v0.times(j + 1))
                    if (j == 0 and i == n) and enum:
                        eps1 = -0.7
                        eps2 = -0.7
                        plt.annotate("$p_{" + str(i) + "," + str(j) + "}^{(1)}$",
                                     (punt1.getX() + eps1, punt1.getY() + eps2))
                    if j > i - n:
                        punt1.arrow(punt2, col)
                        punt2.draw("red", "o")
                        punt1.draw("red", "o")
                    if j < 2 * n - 1:
                        punt1.arrow(punt3, col)
                        punt3.draw("red", "o")
                        punt1.draw("red", "o")

    if soort == "LORB":
        a0 = (v2.times(0.5)).plus(v1.times(n))
        for i in range(2 * n):
            if i < n:
                for j in range(n + i):
                    punt1 = (a0.plus(v0.times(i))).plus(v2.times(j))
                    punt2 = (a0.plus(v0.times(i + 1))).plus(v2.times(j))
                    punt3 = (a0.plus(v0.times(i + 1))).plus(v2.times(j + 1))
                    punt1.arrow(punt2, col)
                    punt1.arrow(punt3, col)
                    if (i == 0 or j == 0) and enum:
                        eps1, eps2 = 0, 0
                        if i == 0:
                            eps1 = 0.2
                            eps2 = -0.2
                        else:
                            eps1 = 0.5
                        plt.annotate("$p_{" + str(i) + "," + str(j) + "}^{(1)}$",
                                     (punt1.getX() + eps1, punt1.getY() + eps2))
                    if weight and i < 2 and j < 2:
                        p1 = (punt1.plus(punt2)).times(0.5)
                        p2 = (punt1.plus(punt3)).times(0.5)
                        plt.annotate((A[i][j] + "^{(2)}$"), (p1.getX() - 0.35, p1.getY()))
                        plt.annotate((B[i][j] + "^{(2)}$"), (p2.getX() - 0.1, p2.getY() - 0.3))
                    punt1.draw("red", "o")
                    punt2.draw("red", "o")
                    punt3.draw("red", "o")
            else:
                for j in range(i - n, 2 * n):
                    punt1 = (a0.plus(v0.times(i))).plus(v2.times(j))
                    punt2 = (a0.plus(v0.times(i + 1))).plus(v2.times(j))
                    punt3 = (a0.plus(v0.times(i + 1))).plus(v2.times(j + 1))
                    if (j == 0 and i == n) and enum:
                        eps1 = 0.5
                        plt.annotate("$p_{" + str(i) + "," + str(j) + "}^{(1)}$",
                                     (punt1.getX() + eps1, punt1.getY()))
                    if j > i - n:
                        punt1.arrow(punt2, col)
                        punt2.draw("red", "o")
                        punt1.draw("red", "o")
                    if j < 2 * n - 1:
                        punt1.arrow(punt3, col)
                        punt3.draw("red", "o")
                        punt1.draw("red", "o")

    if soort == "ROLB":
        a0 = (v1.times(0.5)).plus(v0.times(n))
        for i in range(2 * n):
            if i < n:
                for j in range(n + i):
                    punt1 = (a0.plus(v2.times(i))).plus(v1.times(j))
                    punt2 = (a0.plus(v2.times(i + 1))).plus(v1.times(j))
                    punt3 = (a0.plus(v2.times(i + 1))).plus(v1.times(j + 1))
                    punt1.arrow(punt2, col)
                    punt1.arrow(punt3, col)
                    if weight and i < 2 and j < 2:
                        p1 = (punt1.plus(punt2)).times(0.5)
                        p2 = (punt1.plus(punt3)).times(0.5)
                        plt.annotate(A[i][j], (p1.getX(), p1.getY()))
                        plt.annotate(B[i][j], (p2.getX(), p2.getY()))
                    punt1.draw("red", "o")
                    punt2.draw("red", "o")
                    punt3.draw("red", "o")
            else:
                for j in range(i - n, 2 * n):
                    punt1 = (a0.plus(v2.times(i))).plus(v1.times(j))
                    punt2 = (a0.plus(v2.times(i + 1))).plus(v1.times(j))
                    punt3 = (a0.plus(v2.times(i + 1))).plus(v1.times(j + 1))
                    if j > i - n:
                        punt1.arrow(punt2, col)
                        punt2.draw("red", "o")
                        punt1.draw("red", "o")
                    if j < 2 * n - 1:
                        punt1.arrow(punt3, col)
                        punt3.draw("red", "o")
                        punt1.draw("red", "o")
