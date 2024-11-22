import centroid as C
import gridForm as D
import matplotlib.pyplot as plt
import point as P
import hexagon as H

# Some constant, namely the origin and where to save figures. I changed it
O = P.Point((0, 0))
# pad = 'Insert Path where you want to export your figures to'
pad = r'D:\School\2de jaar Master\Thesis\LaTeX\Klad\Bewijzen\\'


# Draw the triangular grid inside a hexagon, and the black and white centroids if wanted
# centers is a boolean here
def gridInHexagon(length, centers):
    zeshoek = H.Hexagon(O, length)
    D.fillHexagon(zeshoek, centers)
    plt.axis('equal')
    plt.axis('off')
    name = 'GridInHexagon.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the bipartite graph
def bipartiteGraph(length):
    zeshoek = H.Hexagon(O, length)
    D.drawBipartitGraph(zeshoek)
    plt.axis('equal')
    plt.axis('off')
    name = 'BipartiteGraph.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw a random dimer model
def randomDimes(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
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


# draw a random tiling
def randomTiles(length):
    zeshoek = H.Hexagon(O, length)
    lozenges = D.randomTiling(zeshoek)
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


# Draw a black point with its neighbours and connections
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


# Draw the path system of a certain construction on top of random tiling
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
    for c in beta:
        c.drawPoint()
    for c in alpha:
        c.drawPoint()
    plt.axis('equal')
    plt.axis('off')
    name = 'DimersOfTiling.png'
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


# Draw the grid cooresponding to a certain path system construction on top of a hexagon with it triangular grid
def pathGrid(length, soort, weight):
    zeshoek = H.Hexagon(O, length)
    D.fillHexagon(zeshoek, False)
    zeshoek.draw('gray')
    name = "padSystemGraph" + soort
    if weight:
        name = name + "WithWeightIndication" + weight
    D.drawPathGrid(zeshoek, soort, weight)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(pad + name, bbox_inches='tight')
    plt.show()


