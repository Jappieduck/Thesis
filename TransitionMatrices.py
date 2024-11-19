import sympy as sp
import ToLaTeX as LTX

# The symbols for the weights of transition matrices
a11, a12, a13, a21, a22, a23, a31, a32, a33 = sp.symbols("a11 a12 a13 a21 a22 a23 a31 a32 a33")
b11, b12, b13, b21, b22, b23, b31, b32, b33 = sp.symbols("b11 b12 b13 b21 b22 b23 b31 b32 b33")
A = sp.Matrix([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
B = sp.Matrix([[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]])

# symbol for the parameter of transition matrices
z = sp.symbols("z")

# symbol for characteristic polynomial
x = sp.symbols('x')

# periodiscity
r = 3


# Function to receive the right a
def a(i, j):
    return A[i - 1, j - 1]


# Function to receive the right b
def b(i, j):
    return B[i - 1, j - 1]


# The transition functions depending on which level, parameter and which construction used
# this is brute forced and calculated by hand, but I couldn't find a better way to do it
def T(k, x, soort):
    if soort == "LR":
        return sp.Matrix([[a(k, 1), b(k, 1), 0], [0, a(k, 2), b(k, 2)], [b(k, 3) * x, 0, a(k, 3)]])
    if soort == "LORB":
        if k == 1:
            return sp.Matrix([[a(1, 3) / b(1, 3), 1 / b(1, 3), 0], [0, a(2, 3) / b(2, 3), 1 / b(2, 3)],
                              [x / b(3, 3), 0, a(3, 3) / b(3, 3)]])
        if k == 2:
            return sp.Matrix([[a(3, 2) / b(3, 2), 1 / b(3, 2), 0], [0, a(1, 2) / b(1, 2), 1 / b(1, 2)],
                              [x / b(2, 2), 0, a(2, 2) / b(2, 2)]])
        if k == 3:
            return sp.Matrix([[a(2, 1) / b(2, 1), 1 / b(2, 1), 0], [0, a(3, 1) / b(3, 1), 1 / a(3, 1)],
                              [x / a(1, 1), 0, a(1, 1) / b(1, 1)]])
    if soort == "ROLB":
        if k == 1:
            return sp.Matrix([[b(3, 3) / a(3, 3), 1 / a(3, 3), 0], [0, b(2, 2) / a(2, 2), 1 / a(2, 2)],
                              [x / a(1, 1), 0, b(1, 1) / a(1, 1)]])
        if k == 2:
            return sp.Matrix([[b(3, 1) / a(3, 1), 1 / a(3, 1), 0], [0, b(2, 3) / a(2, 3), 1 / a(2, 3)],
                              [x / a(1, 2), 0, b(1, 2) / a(1, 2)]])
        if k == 3:
            return sp.Matrix([[b(3, 2) / a(3, 2), 1 / a(3, 2), 0], [0, b(2, 1) / a(2, 1), 1 / a(2, 1)],
                              [x / a(1, 3), 0, b(1, 3) / a(1, 3)]])


# A method to simplify the entries of a matrix
def simplifyMatrix(matrix):
    n, m = sp.shape(matrix)
    mat = sp.zeros(n, m)
    for i in range(n):
        for j in range(m):
            mat[i, j] = matrix[i, j].simplify()
    return mat


# Calculate W = T1*T2*T3, because this is to risky to do by hand
def W(x, soort):
    matrix = T(1, x, soort) * T(2, x, soort) * T(3, x, soort)
    mat = simplifyMatrix(matrix)
    return mat


# Get the coefficients of a polynomial
def getCoef(expr):
    degr = sp.degree(expr, x)
    coefficienten = []
    if degr > 0:
        for i in range(degr + 1):
            coefficienten.append(expr.coeff(x, i))
    return coefficienten

# Some calculations to look for a relation between different W's
matrixLR = W(z, 'LR')
matrixLORB = W(z, 'LORB')

detLR = sp.det(matrixLR).simplify()
detLORB = sp.det(matrixLORB).simplify()

charLR = sp.collect(matrixLR.charpoly(x).as_expr(), x)
charLORB = sp.collect(matrixLORB.charpoly(x).as_expr(), x)

coefLR = getCoef(charLR)
coefLORB = getCoef(charLORB)

print(detLR)
print("\n")
print(detLORB)

# print(LTX.writeMatrix(matrixLR))
# print('\n\n')
# print(LTX.writeMatrix(matrixLORB))
# print('\n\n')
# print(LTX.writeMatrix(matrixROLB))
