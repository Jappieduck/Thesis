import centroid as C
import gridForm as D
import matplotlib.pyplot as plt
import point as P
import hexagon as H
import triangle as T
import math as m

# Some constant, namely the origin and where to save figures.
O = P.Point((0, 0))
pad = r'D:\School\2de jaar Master\Thesis\LaTeX\Thesis\Paper\Afbeeldingen\\'


# Draw the triangular grid inside a hexagon, and the black and white centroids if wanted
# centers is a boolean here
def gridInHexagon(length, centroidType):
    zeshoek = H.Hexagon(O, length)
    eps = 0
    if centroidType != "black" and centroidType != "white":
        eps += 1
    D.fillHexagon(H.Hexagon(O, length + eps), centroidType)
    zeshoek.draw('black')
    plt.axis('equal')
    plt.axis('off')
    name = 'GridInHexagon.png'
    if centroidType == "black" or centroidType == "white":
        D.naming(zeshoek, 0, centroidType)
        name = 'Enumeration.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the bipartite graph
def bipartiteGraph(length, weight):
    zeshoek = H.Hexagon(O, length)
    D.drawBipartitGraph(zeshoek, weight)
    plt.axis('equal')
    plt.axis('off')
    name = 'BipartiteGraph.png'
    if weight:
        name = "bipartiteWeights.png"
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


bipartiteGraph(2, True)


# Draw a random dimer covering
def randomDimes(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
    D.drawBipartitGraph(zeshoek, False)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for col in beta:
        for c in col:
            c.drawPoint()
    for col in alpha:
        for c in col:
            c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'DimerModel.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw a random tiling
def randomTiles(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
    for loz in lozenges:
        loz.draw()
    plt.axis('equal')
    plt.axis('off')
    if length == 1:
        name = 'LozengePresentation.png'
        i = 1
        for loz in lozenges:
            centroids = loz.getCentroids()
            punt = centroids[0].plus(centroids[1]).times(1 / 2)
            plt.annotate("$L_" + str(i) + "$", (punt.getX(), punt.getY()))
            i += 1
    else:
        name = 'RandomTiling.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# draw the dimer model of a random tiling on top of that random tiling
def dimersOnTiling(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
    D.drawBipartitGraph(zeshoek, False)
    D.drawLozenges(lozenges)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for col in beta:
        for c in col:
            c.drawPoint()
    for col in alpha:
        for c in col:
            c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'TilingAndDimers.png'
    if weight:
        name = "dimerWeight.png"
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the path system of a certain construction on top of random tiling
# LR is iota = 1, ROLB is iota = 2 and LORB is iota = 3
def plotPathSystem(length, construct):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
    D.drawLozenges(lozenges)
    for loz in lozenges:
        loz.drawPath(construct)
    plt.axis('equal')
    plt.axis('off')
    name = 'PathSystem' + construct + '.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the dimers of the tiles of a random tiling
def dimerOfTiling(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
    D.drawLozenges(lozenges)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for col in beta:
        for c in col:
            c.drawPoint()
    for col in alpha:
        for c in col:
            c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'DimersOfTiling.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the grid corresponding to a certain path system construction on top of a hexagon with it triangular grid
def pathGrid(length, soort, weight, enum):
    zeshoek = H.Hexagon(O, length)
    if not weight:
        D.fillHexagon(zeshoek, False)
    zeshoek.draw('black')
    name = "padSystemGraph" + soort + ".png"
    if weight:
        name = "padSystemWithWeight" + soort + ".png"
    if enum:
        name = "padSystemEnumerated" + soort + ".png"
    D.drawPathGrid(zeshoek, soort, weight, enum)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def driehoeken():
    b = C.Centroid((0, 0), "beta")
    w = C.Centroid((-m.sqrt(3) / 3, 0), "alpha")
    driehoekB = T.Triangle(b, "beta")
    driehoekW = T.Triangle(w, "alpha")
    driehoekB.draw('black', '-')
    driehoekW.draw('black', '-')
    b.drawPoint()
    w.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(pad + "Driehoeken.png", bbox_inches='tight')
    plt.show()
