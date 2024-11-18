import sympy as sp
from sympy import latex


def toLTX(expr):
    return latex(expr)


def writeMatrix(matrix):
    newstring = "\\begin{pmatrix}\n"
    n, m = sp.shape(matrix)
    for i in range(n):
        newstring = newstring + "   "
        for j in range(m):
            newstring = newstring + toLTX(matrix[i, j]) + " "
            if j != m - 1:
                newstring = newstring + "& "
        if i != n-1:
            newstring = newstring + "\\" + "\\" + "\n"
        else:
            newstring = newstring + "\n"
    newstring = newstring + "\\end{pmatrix}"
    return newstring
