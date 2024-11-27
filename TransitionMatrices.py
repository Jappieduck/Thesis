import sympy as sp
import ToLaTeX as LTX

# The symbols for the weights of transition matrices

r = 3
n = 3

a = sp.IndexedBase('a')
b = sp.IndexedBase('b')
c = sp.IndexedBase('c')

i, j = sp.symbols('i j', cls=sp.Idx)
z = sp.symbols('z')


def ai(soort, index):
    i0, j0 = index
    if soort == 1:
        i = i0
        j = j0
        return a[i, j] / c[i, j]
    elif soort == 2:
        i = 2 * n - j0 - 1
        j = i0 + i - n
        return b[i % r, j % r] / a[i % r, j % r]
    elif soort == 3:
        if j0 + 1 >= i0:
            i = n + j0 - i0
            j = 2 * n - j0 - 1 + i - n
        else:
            i = n + j0 - i0
            j = 2 * n - i0 - 1
        return c[i % r, j % r] / b[i % r, j % r]


def bi(soort, index):
    i0, j0 = index
    if soort == 1:
        i = i0
        j = j0
        return b[i, j] / c[i, j]
    elif soort == 2:
        i = 2 * n - j0 - 1
        j = i0 + i - n
        return c[i % r, j % r] / a[i % r, j % r]
    elif soort == 3:
        if j0 + 1 >= i0:
            i = n + j0 - i0
            j = 2 * n - j0 - 1 + i - n
        else:
            i = n + j0 - i0
            j = 2 * n - i0 - 1
        return a[i % r, j % r] / b[i % r, j % r]


def T(m, var, soort):
    matrix = sp.zeros(n, n)
    for k in range(0, n):
        if k != n - 1:
            matrix[k, k] = ai(soort, (m-1, k))
            matrix[k, (k + 1) % n] = bi(soort, (m-1, k))
        else:
            matrix[k, k] = ai(soort, (m-1, k))
            matrix[k, (k + 1) % n] = bi(soort, (m-1, k)) * var
    return matrix


def W(var, soort):
    W = 1
    for i in range(r):
        W = W * T(r, var, soort)
    return W


