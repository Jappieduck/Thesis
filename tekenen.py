import Drawing as D
import matplotlib.pyplot as plt
import point as P
import triangle as T
import hexagon as H
import Centroid as C


O = P.Point((0, 0))
zeshoek = H.Hexagon(O, 'Standing', 2)
D.fillHexagon(zeshoek)
D.drawBipartitGraph(zeshoek)
plt.axis('equal')
plt.axis('off')
plt.show()