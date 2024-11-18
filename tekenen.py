import centroid as C
import gridForm as D
import matplotlib.pyplot as plt
import point as P
import hexagon as H

O = P.Point((0, 0))

pad = r'D:\School\2de jaar Master\Thesis\LaTeX\Klad\Bewijzen\\'


def gridInHexagon(length, centers):
    zeshoek = H.Hexagon(O, 'Standing', length)
    D.fillHexagon(zeshoek, centers)
    plt.axis('equal')
    plt.axis('off')
    name = 'GridInHexagon.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def bipartiteGraphInGrid(length):
    zeshoek = H.Hexagon(O, 'Standing', length)
    D.drawBipartitGraph(zeshoek)
    plt.axis('equal')
    plt.axis('off')
    name = 'BipartiteGraph.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def getTiling(length):
    valid = False
    while not valid:
        zeshoek = H.Hexagon(O, 'Standing', length)
        lastAlpha, lozenges = D.randomTiling(zeshoek)
        if not valid:
            plt.clf()
        else:
            return zeshoek, lastAlpha, lozenges


def randomDimes(length):
    zeshoek, lastalpha, lozenges = getTiling(length)
    D.drawBipartitGraph(zeshoek)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for c in beta:
        c.drawPoint()
    for c in alpha:
        c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'DimerModel.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def randomTiles(length):
    zeshoek, lastAlpha, lozenges = getTiling(length)
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


def dimersOnTiling(length):
    zeshoek, lastAlpha, lozenges = getTiling(length)
    D.drawBipartitGraph(zeshoek)
    D.drawLozenges(lozenges)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for c in beta:
        c.drawPoint()
    for c in alpha:
        c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'TilingAndDimers.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def drawVert():
    p = C.Centroid((0, 0), 'beta')
    buren = p.getConnect()
    kleuren = ['green', 'blue', 'black']
    for i in range(len(buren)):
        p.connect(buren[i], kleuren[i], '-')
        buren[i].drawPoint()
    p.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'betaVertex.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def plotPathSystem(length, construct):
    zeshoek, lastAlpha, lozenges = getTiling(length)
    D.drawLozenges(lozenges)
    for loz in lozenges:
        loz.drawPath(construct)
    plt.axis('equal')
    plt.axis('off')
    name = 'PathSystem' + construct + '.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def dimerOfTiling(length):
    zeshoek, lasatAlpha, lozenges = getTiling(length)
    D.drawLozenges(lozenges)
    D.drawDimes(lozenges)
    beta, alpha = D.get_Centroids(zeshoek)
    for c in beta:
        c.drawPoint()
    for c in alpha:
        c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'DimersOfTiling.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


def pathGrid(length):
    zeshoek = H.Hexagon(O, 'Standing', length)
    D.fillHexagon(zeshoek, False)
    zeshoek.draw('gray')
    soort = "LR"
    D.drawPathGrid(zeshoek, soort)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


pathGrid(4)
