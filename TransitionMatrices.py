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
            matrix[k, k] = ai(soort, (m - 1, k))
            matrix[k, (k + 1) % n] = bi(soort, (m - 1, k))
        else:
            matrix[k, k] = ai(soort, (m - 1, k))
            matrix[k, (k + 1) % n] = bi(soort, (m - 1, k)) * var
    return matrix


def W(var, soort):
    W = 1
    for i in range(r):
        W = W * T(r, var, soort)
    return W


def checkCondition1():
    for l in range(1, 4):
        print('Soort (' + str(l) + ')')
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            if k != r - 1:
                print('        j = ' + str(k) + '&: ' + LTX.toLTX(ai(l, (0, k)) * ai(l, (1, k)) * ai(l, (2, k))) + "\\\\")
            else:
                print('        j = ' + str(k) + '&: ' + LTX.toLTX(ai(l, (0, k)) * ai(l, (1, k)) * ai(l, (2, k))))
        print('    \\end{split}')
        print('\\end{equation*}')


def checkCondition2():
    for l in range(1, 4):
        print('Soort (' + str(l) + ')')
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            if k != r - 1:
                print('        &' + LTX.toLTX(
                    bi(l, (0, k % r)) * bi(l, (1, (1 + k) % r)) * bi(l, (2, (2 + k) % r))) + "\\\\")
            else:
                print('        &' + LTX.toLTX(bi(l, (0, k % r)) * bi(l, (1, (1 + k) % r)) * bi(l, (2, (2 + k) % r))))
        print('    \\end{split}')
        print('\\end{equation*}')


def checkCondition3():
    for l in range(1, 4):
        print('Soort (' + str(l) + ')')
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            if k != r - 1:
                print('        k = ' + str(k) + '&: ' + LTX.toLTX(
                    (ai(l, (k, 1)) * ai(l, (k, 2)) * ai(l, (k, 3))) / (
                                bi(l, (k, 1)) * bi(l, (k, 2)) * bi(l, (k, 3)))) + "\\\\")
            else:
                print('        k = ' + str(k) + '&: ' + LTX.toLTX(
                    (ai(l, (k, 1)) * ai(l, (k, 2)) * ai(l, (k, 3))) / (
                            bi(l, (k, 1)) * bi(l, (k, 2)) * bi(l, (k, 3)))))
        print('    \\end{split}')
        print('\\end{equation*}')