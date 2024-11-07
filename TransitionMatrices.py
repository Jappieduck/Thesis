import sympy as sp

a11, a12, a13, a21, a22, a23, a31, a32, a33 = sp.symbols("a11 a12 a13 a21 a22 a23 a31 a32 a33")
b11, b12, b13, b21, b22, b23, b31, b32, b33 = sp.symbols("b11 b12 b13 b21 b22 b23 b31 b32 b33")
A = sp.Matrix([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
B = sp.Matrix([[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]])
z = sp.symbols("z")


def a(i, j):
    return A[i - 1, j - 1]


def b(i, j):
    return B[i - 1, j - 1]


def mod(r, k):
    if k % r == 0:
        return 1
    else:
        return k%r


def T(k, x):
    return sp.Matrix([[a(k, 1), b(k, 1), 0], [0, a(k, 2), b(k, 2)], [b(k, 3) * x, 0, a(k, 3)]])


def T2(k, x):
    return sp.Matrix(
        [[b(1, k) / a(1, k), 1 / a(1, k), 0], [0, b(2, mod(3, k + 1)) / a(2, mod(3, k + 1)), 1 / a(2, mod(3, k + 1))],
         [x / a(3, mod(3, k + 2)), 0, b(3, mod(3, k + 2)) / a(3, mod(3, k + 2))]])


def T3(k, x):
    return 0


def W(x, type):
    if type == "LR":
        return T(1, x) * T(2, x) * T(3, x)
    elif type == "LORB":
        return T3(1, x) * T3(2, x) * T3(3, x)
    elif type == "ROLB":
        return T2(1, x) * T2(2, x) * T2(3, x)


def printMatrix(matrix):
    rows, cols = sp.shape(matrix)
    matrixString = ""
    for i in range(cols):
        for j in range(rows):
            matrixString = matrixString + str(matrix[i, j])
            matrixString = matrixString + " | "
        matrixString = matrixString + "\n"
    print(matrixString)


printMatrix(W(z, 'ROLB').applyfunc(sp.simplify))
