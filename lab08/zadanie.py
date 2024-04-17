def tabele_podciag(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n + 1)]
         for j in range(m + 1)]
    b = [[0 for i in range(n + 1)]
         for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # print(i, j)
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "\\\\"
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "||"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "--"
    return c, b


def print_tabelka(x, y):  # kolumny, wiersze
    tables = tabele_podciag(x, y)
    numbers = tables[0]
    signs = tables[1]
    result = [[' \\\\\\', ' 0 '], []]
    for letter in y:
        result[0].append(' ' + letter + ' ')
    for i in range(len(numbers[0]) + 1):
        if i == 0:
            result[1].append('  0 ')
        else:
            result[1].append(' 0 ')
    for letter in x:
        result.append(['  ' + letter + ' ', ' 0 '])
    for i in range(1, len(numbers)):
        for j in range(1, len(numbers[0])):
            result[i + 1].append(str(numbers[i][j]) + signs[i][j])
    wynik = '\n'
    for i in range(len(result)):
        for j in range(len(result[0])):
            wynik += result[i][j]
            if j != len(result[0]) - 1:
                wynik += ' │ '  # dekoracje
        wynik += '\n'
        if i != len(result) - 1:  # dekoracje
            wynik += '─────' + '┼─────' * (len(y) + 1) + '\n'
    return wynik


def _print_podciag(x, c, b, i, j):
    acc = set()
    if i == 0 or j == 0:
        acc.add("")
        return acc
    if b[i][j] == '\\\\':
        temp = _print_podciag(x, c, b, i - 1, j - 1)
        for elem in temp:
            acc.add(elem + x[i - 1])
    else:
        if c[i - 1][j] >= c[i][j - 1]:  # jeżeli l >= p to liczy lewą odnogę
            acc = _print_podciag(x, c, b, i - 1, j)
        if c[i][j - 1] >= c[i - 1][j]:  # jeżeli p >= l to liczy prawą odnogę
            temp = _print_podciag(x, c, b, i, j - 1)
            for elem in temp:
                acc.add(elem)
        # jeżeli l == p to przejdzie po obu odnogach
    return acc


def print_podciag(x, y):
    data = tabele_podciag(x, y)
    elems = _print_podciag(x, data[0], data[1], len(x), len(y))
    return elems


slowo1 = 'abbaac'
slowo2 = 'bacbacba'
lista = print_podciag(slowo1, slowo2)
print(print_tabelka(slowo1, slowo2))
# print(lista)
for podciag in lista:
    print(podciag)
