import gridForm as D
import matplotlib.pyplot as plt
import point as P
import triangle as T
import hexagon as H
import centroid as C

O = P.Point((0, 0))


def gridInHexagon(length):
    zeshoek = H.Hexagon(O, 'Standing', length)
    D.fillHexagon(zeshoek)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


def bipartiteGraphInGrid(length):
    zeshoek = H.Hexagon(O, 'Standing', length)
    D.fillHexagon(zeshoek)
    D.drawBipartitGraph(zeshoek)
    plt.axis('equal')
    plt.axis('off')
    plt.show()