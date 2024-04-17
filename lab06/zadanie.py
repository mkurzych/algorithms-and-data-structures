plik = open("./nazwiska.txt", 'r')


def cleanup(file):
    data = file.readlines()
    array = []
    for elem in data:
        temp = elem.split()
        array.append(make_obj(int(temp[0]), temp[1]))
    return array


def make_obj(amount, surname):
    obj = {
        'ilosc': amount,
        'nazwisko': surname
    }
    return obj


def make_t(n):
    t = []
    for i in range(n):
        t.append([])
    return t


def liniowa(elem, i, n):
    index = 0
    for letter in elem:
        if letter != elem[-1]:
            index += 111 * ord(letter)
    index = (index * 111) + ord(elem[-1]) + i
    return index % n


def kwadratowa(elem, i, n):
    index = 0
    for letter in elem:
        if letter != elem[-1]:
            index += 111 * ord(letter)
    index = (index * 111) + ord(elem[-1]) + i * i
    return index % n


def dwukrotna(elem, i, n):
    index = 0
    for letter in elem:
        if letter != elem[-1]:
            index += 111 * ord(letter)
    index = (index * 111) + ord(elem[-1])
    # index += i * hash(elem)
    temp = 0
    for letter in elem:
        temp += ord(letter)
    index += (temp * i)
    return index % n


def wstaw(t, elem, func, n):
    p = 0  # by liczyć średnią
    while True:
        index = func(elem['nazwisko'], p, n)
        if len(t[index]) == 0:
            t[index].append(elem)
            break
        p += 1  # by liczyć średnią
    return p + 1, t  # by liczyć średnią


def fill_t(array, func, n, proc):
    t = make_t(n)
    suma = 0  # by liczyć średnią
    for i in range(int(n * (proc / 100))):
        temp = wstaw(t, array[i], func, n)
        suma += temp[0]  # by liczyć średnią
        t = temp[1]
    return suma / int(n * (proc / 100)),  t


functions = [[liniowa, kwadratowa, dwukrotna], ['LINIOWA', 'KWADRATOWA', 'DWUKROTNA']]
poziomy = [50, 70, 90]
test1 = cleanup(plik)
print('DLA MAŁYCH TABLIC (ROZMIARU 7)')
counter = 0
for function in functions[0]:
    print('\n' + str(functions[1][counter]))
    for poziom in poziomy:
        temp = fill_t(test1, function, 7, poziom)
        tablica = temp[1]
        print('Zapełnienie: ' + str(poziom) + '%' + '\nŚrednia ilość prób: ' + str(temp[0]))
        for line in tablica:
            print(line)
        print()
    counter += 1

print('CZĘŚĆ TESTOWA (ROZMIAR 20011)')
counter = 0
for function in functions[0]:
    print('\n' + str(functions[1][counter]))
    for poziom in poziomy:
        temp = fill_t(test1, function, 20011, poziom)
        tablica = temp[1]
        print('Zapełnienie: ' + str(poziom) + '%' + '\nŚrednia ilość prób: ' + str(temp[0]))
    counter += 1

# DLA MAŁYCH TABLIC (ROZMIARU 7)

# LINIOWA
# Zapełnienie: 50%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# []
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 70%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 90%
# Średnia ilość prób: 1.3333333333333333
# [{'ilosc': 88932, 'nazwisko': 'Wojcik'}]
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# [{'ilosc': 89366, 'nazwisko': 'Lewandowski'}]


# KWADRATOWA
# Zapełnienie: 50%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# []
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 70%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 90%
# Średnia ilość prób: 1.3333333333333333
# [{'ilosc': 88932, 'nazwisko': 'Wojcik'}]
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# [{'ilosc': 89366, 'nazwisko': 'Lewandowski'}]


# DWUKROTNA
# Zapełnienie: 50%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# []
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 70%
# Średnia ilość prób: 1.0
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# []
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# []

# Zapełnienie: 90%
# Średnia ilość prób: 2.1666666666666665
# []
# [{'ilosc': 220217, 'nazwisko': 'Nowak'}]
# [{'ilosc': 88932, 'nazwisko': 'Wojcik'}]
# [{'ilosc': 92945, 'nazwisko': 'Dabrowski'}]
# [{'ilosc': 131940, 'nazwisko': 'Kowalski'}]
# [{'ilosc': 104418, 'nazwisko': 'Wisniewski'}]
# [{'ilosc': 89366, 'nazwisko': 'Lewandowski'}]

# CZĘŚĆ TESTOWA (ROZMIAR 20011)

# LINIOWA
# Zapełnienie: 50%
# Średnia ilość prób: 12.492253873063468
# Zapełnienie: 70%
# Średnia ilość prób: 43.900621118012424
# Zapełnienie: 90%
# Średnia ilość prób: 95.80176578377478

# KWADRATOWA
# Zapełnienie: 50%
# Średnia ilość prób: 5.454572713643178
# Zapełnienie: 70%
# Średnia ilość prób: 7.841008067394874
# Zapełnienie: 90%
# Średnia ilość prób: 11.409739574657117

# DWUKROTNA
# Zapełnienie: 50%
# Średnia ilość prób: 3.653073463268366
# Zapełnienie: 70%
# Średnia ilość prób: 5.045405868494324
# Zapełnienie: 90%
# Średnia ilość prób: 7.315009162085624


