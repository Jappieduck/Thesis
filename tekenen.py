import centroid
import gridForm as D
import matplotlib.pyplot as plt
import point as P
import hexagon as H
import lozenge as L

O = P.Point((0, 0))

pad = r'C:\Users\user\OneDrive\Documenten\School\2de jaar Master\Thesis\LaTeX\Klad\Bewijzen\\'


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


def randomDimes(length):
    valid = False
    while not valid:
        valid = True
        zeshoek = H.Hexagon(O, 'Standing', length)
        lastAlpha, lozenges = D.randomTiling(zeshoek, 'Left')
        for alpha in lastAlpha:
            if not alpha.getConnection():
                valid = False
                plt.clf()
    plt.axis('equal')
    plt.axis('off')
    plt.show()


def randomTiles(length):
    valid = False
    while not valid:
        zeshoek = H.Hexagon(O, 'Standing', length)
        lastAlpha, lozenges = D.randomTiling(zeshoek, 'Left')
        valid = D.isValid(lastAlpha)
        if not valid:
            plt.clf()
        else:
            D.drawLozenges(lozenges)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


randomTiles(1)