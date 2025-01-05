import matplotlib.pyplot as plt
import gridForm as D
import hexagon as H
import point as P
import io
from PIL import Image
import math as m
import centroid as C

O = P.Point((0, 0))


def getFullCentroidGrid(n):
    black = []
    white = []
    v1 = P.Point((m.sqrt(3) / 2, -0.5))
    v2 = P.Point((-m.sqrt(3) / 2, -0.5))
    v0 = P.Point((0, 1))
    shift = P.Point((m.sqrt(3) / 6, 0.5))
    for i in range(2 * n):
        colB = []
        colW = []
        for j in range(2 * n):
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
    colW = []
    for j in range(2 * n):
        b = (v0.times(j)).plus(v1.times(2 * n)).plus(v2.times(n)).plus(shift)
        w = b.plus(P.Point((-m.sqrt(3) / 3, 0)))
        w = C.Centroid((w.getX(), w.getY()), 'alpha')
        colW.append(w)
    white.append(colW)
    return black, white


def rotatePlot(VertexType, n, black, white, plek, m):
    i, j = plek
    plt.clf()
    zeshoek = H.Hexagon(O, n)
    D.fillHexagon(zeshoek, False)
    if m > 0:
        rotatePlot(VertexType, n, black, white, plek, m - 1)
    elif j > 0:
        rotatePlot(VertexType, n, black, white, (i, j - 1), 2)
    elif i > 0:
        rotatePlot(VertexType, n, black, white, (i - 1, n - 1), 2)

    if m == 0:
        if VertexType == 'black':
            plt.scatter(black[i][j].getX(), black[i][j].getY(), color='red')
        if VertexType == 'white':
            plt.scatter(white[i][j].getX(), white[i][j].getY(), color='red')
    if m == 1:
        if VertexType == 'black':
            plt.scatter(black[2 * n - j - 1][n + i - j - 1].getX(), black[2 * n - j - 1][n + i - j - 1].getY(),
                        color='green')
        if VertexType == 'white':
            plt.scatter(white[2 * n - j - 1][n + i - j].getX(), white[2 * n - j - 1][n + i - j].getY(),
                        color='green')
    if m == 2:
        if VertexType == 'black':
            plt.scatter(black[n + j - i][2 * n - i - 1].getX(), black[n + j - i][2 * n - i - 1].getY(),
                        color='blue')
        if VertexType == 'white':
            plt.scatter(white[n + j - i - 1][2 * n - i - 1].getX(), white[n + j - i - 1][2 * n - i - 1].getY(),
                        color='blue')
    plt.axis('equal')
    plt.axis('off')


def animateRotation(n, VertexType):
    frames = []
    black, white = getFullCentroidGrid(n)
    eps = 0
    if VertexType == 'white':
        eps += 1
    for i in range(n):
        for j in range(n):
            for m in range(3):
                rotatePlot(VertexType, n, black, white, (i, j), m)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                frames.append(Image.open(buf))
    frames[0].save('rotation_animation_' + VertexType + '.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=600,
                   loop=0)
    print("Animation is Saved!")


n = 6
animateRotation(n, "black")
animateRotation(n, "white")
