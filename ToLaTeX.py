import sympy as sp
from sympy import latex


# Transform sympy symbol expression to latex code
def toLTX(expr):
    return latex(expr)


# transform a sympy matrix to code for latex
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


def mathfrak(string):
    replacing = ["{a}", "{b}", "{c}"]
    for letter in replacing:
        string = string.replace(letter, "\\mathfrak" + letter)
    return string