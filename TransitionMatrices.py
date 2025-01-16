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
x = sp.symbols('x')


def ai(n, soort, index):
    i0, j0 = index
    if soort == 1:
        i = i0
        j = j0
        return a[i % r, j % r]
    elif soort == 2:
        i = 2 * n - j0 - 1
        j = n + i0 - j0 - 1
        return b[i % r, j % r] / a[i % r, j % r]
    elif soort == 3:
        i = n + j0 - i0
        j = 2 * n - i0 - 1
        return 1 / b[i % r, j % r]


def bi(n, soort, index):
    i0, j0 = index
    if soort == 1:
        i = i0
        j = j0
        return b[i % r, j % r]
    elif soort == 2:
        i = 2 * n - j0 - 1
        j = n + i0 - j0 - 1
        return 1 / a[i % r, j % r]
    elif soort == 3:
        i = n + j0 - i0
        j = 2 * n - i0 - 1
        return a[i % r, j % r] / b[i % r, j % r]


def T(n, m, var, soort):
    matrix = sp.zeros(n, n)
    for k in range(0, n):
        if k != n - 1:
            matrix[k, k] = ai(n, soort, (k, m - 1))
            matrix[k, (k + 1) % n] = bi(n, soort, (k, m - 1))
        else:
            matrix[k, k] = ai(n, soort, (k, m - 1))
            matrix[k, (k + 1) % n] = bi(n, soort, (k, m - 1)) * var
    return matrix


# Method to substitute the conditions we need
def conditions(n, expr):
    newexpr = expr
    for i in range(r):
        cond1 = ai(n, 1, (0, i)) * ai(n, 1, (1, i)) * ai(n, 1, (2, i))
        newexpr = newexpr.subs(cond1, 1)
        newexpr = newexpr.subs(cond1 ** (-1), 1)
        cond3 = (ai(n, 1, (i, 0)) * ai(n, 1, (i, 1)) * ai(n, 1, (i, 2))) / (
                bi(n, 1, (i, 0)) * bi(n, 1, (i, 1)) * bi(n, 1, (i, 2)))
        newexpr = newexpr.subs(cond3, 1)
        newexpr = newexpr.subs(cond3 ** (-1), 1)
        cond2 = bi(n, 1, (0, 0 + i)) * bi(n, 1, (1, 1 + i)) * bi(n, 1, (2, 2 + i))
        newexpr = newexpr.subs(cond2, 1)
        newexpr = newexpr.subs(cond2 ** (-1), 1)
    return newexpr


def W(n, var, soort):
    W = 1
    for i in range(r):
        W = W * T(n, r, var, soort)
    for i in range(r):
        for j in range(r):
            W[i, j] = W[i, j].expand()
    return conditions(n, W)


def charpol(matrix):
    return conditions(n, conditions(n, matrix.charpoly(x)).expand())


def A(soort):
    return ai(n, soort, (0, 0)) * ai(n, soort, (0, 1)) * bi(n, soort, (1, 0)) * bi(n, soort, (1, 1))


def B(soort):
    return ai(n, soort, (0, 0)) * ai(n, soort, (1, 2)) * bi(n, soort, (1, 0)) * bi(n, soort, (0, 1))


def C(soort):
    return ai(n, soort, (1, 1)) * ai(n, soort, (1, 2)) * bi(n, soort, (0, 0)) * bi(n, soort, (0, 1))


def Q(soort):
    return conditions(n, ((A(soort) + B(soort) + C(soort)) ** 3 / (A(soort) * B(soort) * C(soort)))).simplify()


def checkPol(pol1, pol2):
    d1 = sp.degree(pol1, x)
    d2 = sp.degree(pol2, x)
    coeff1 = pol1.all_coeffs()
    coeff2 = pol2.all_coeffs()
    if d1 == d2:
        for i in range(len(coeff1)):
            if coeff1[i] != coeff2[i]:
                return False
        return True
    else:
        return False


# Checks which Ti of type 1 have same characteristic polynomial as other Tj of other types, and returns pairs that
# which have the same characteristic polynomial
def checkSimilarities():
    similars = []
    for i in range(1, r + 1):
        pol1 = T(n, i, z, 1).charpoly(x)
        for j in range(2, r + 1):
            for k in range(1, r + 1):
                pol2 = T(n, k, z, j).charpoly(x)
                if checkPol(pol1, pol2):
                    similars.append(((i, 1), (k, j)))
    return similars


def checkCondition1(n):
    for l in range(1, 4):
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            product = "{a}^{(" + str(l) + ")}_{0," + str(k) + "}" + "{a}^{(" + str(l) + ")}_{1," + str(
                k) + "}" + "{a}^{(" + str(l) + ")}_{2," + str(k) + "} = "
            if k != r - 1:
                print(LTX.mathfrak(
                    '        ' + product + LTX.toLTX(
                        ai(n, l, (0, k)) * ai(n, l, (1, k)) * ai(n, l, (2, k))) + " = " + LTX.toLTX(
                        conditions(n, ai(n, l, (0, k)) * ai(n, l, (1, k)) * ai(n, l, (2, k)))) + "\\\\"))
            else:
                print(LTX.mathfrak('        ' + product + LTX.toLTX(
                    ai(n, l, (0, k)) * ai(n, l, (1, k)) * ai(n, l, (2, k))) + " = " + LTX.toLTX(
                    conditions(n, ai(n, l, (0, k)) * ai(n, l, (1, k)) * ai(n, l, (2, k))))))
        print('    \\end{split}')
        print('\\end{equation*}')


def checkCondition2():
    for l in range(1, 4):
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            product = "{b}^{(" + str(l) + ")}_{0," + str(k % r) + "}" + "{b}^{(" + str(l) + ")}_{1," + str(
                (k + 1) % r) + "}" + "{b}^{(" + str(l) + ")}_{2," + str((k + 2) % r) + "} = "
            if k != r - 1:
                print(LTX.mathfrak('        ' + product + LTX.toLTX(
                    bi(n, l, (0, k % r)) * bi(n, l, (1, (1 + k) % r)) * bi(n, l, (2, (2 + k) % r))) + " = " + LTX.toLTX(
                    conditions(n, bi(n, l, (0, k % r)) * bi(n, l, (1, (1 + k) % r)) * bi(n, l,
                                                                                         (2, (2 + k) % r)))) + "\\\\"))
            else:
                print(LTX.mathfrak('        ' + product + LTX.toLTX(
                    bi(n, l, (0, k % r)) * bi(n, l, (1, (1 + k) % r)) * bi(n, l, (2, (2 + k) % r))) + " = " + LTX.toLTX(
                    conditions(n, bi(n, l, (0, k % r)) * bi(n, l, (1, (1 + k) % r)) * bi(n, l, (2, (2 + k) % r))))))
        print('    \\end{split}')
        print('\\end{equation*}')


def checkCondition3(n):
    for l in range(1, 4):
        print('\\begin{equation*}')
        print('    \\begin{split}')
        for k in range(r):
            product = ("\\frac{" + "{a}^{(" + str(l) + ")}_{" + str(k) + ",0}" + "{a}^{(" + str(l) + ")}_{" + str(
                k) + ",1}" + "{a}^{(" + str(l) + ")}_{" + str(k) + ",2}}"
                       + "{{b}^{(" + str(l) + ")}_{" + str(k) + ",0}" + "{b}^{(" + str(l) + ")}_{" + str(
                        k) + ", 1}" + "{b}^{(" + str(l) + ")}_{" + str(k) + ",2}} = ")
            if k != r - 1:
                print('        ' + LTX.mathfrak(product) + LTX.mathfrak(LTX.toLTX(
                    (ai(n, l, (k, 0)) * ai(n, l, (k, 1)) * ai(n, l, (k, 2))) / (
                            bi(n, l, (k, 0)) * bi(n, l, (k, 1)) * bi(n, l, (k, 2)))) + " = " + LTX.toLTX(
                    conditions(n, (ai(n, l, (k, 0)) * ai(n, l, (k, 1)) * ai(n, l, (k, 2))) / (
                            bi(n, l, (k, 0)) * bi(n, l, (k, 1)) * bi(n, l, (k, 2))))) + "\\\\"))
            else:
                print('        ' + LTX.mathfrak(product) + LTX.mathfrak(LTX.toLTX(
                    (ai(n, l, (k, 0)) * ai(n, l, (k, 1)) * ai(n, l, (k, 2))) / (
                            bi(n, l, (k, 0)) * bi(n, l, (k, 1)) * bi(n, l, (k, 2)))) + " = " + LTX.toLTX(
                    conditions(n, (ai(n, l, (k, 0)) * ai(n, l, (k, 1)) * ai(n, l, (k, 2))) / (
                            bi(n, l, (k, 0)) * bi(n, l, (k, 1)) * bi(n, l, (k, 2)))))))
        print('    \\end{split}')
        print('\\end{equation*}')


print(((Q(1) - Q(2)).expand()).simplify())