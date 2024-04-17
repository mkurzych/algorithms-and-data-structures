tests = open("./3700.txt", 'r')


def cleanup(file):
    temp = file.readlines()
    array = []
    for elem in temp:
        array.append(elem[:-1])
    return array


def s(word):
    index = 0
    for letter in word:
        index += ord(letter)
    return index


def w(word):
    index = hash(word)
    return index


def d(word):
    index = 0
    for letter in word:
        index = index + ord(letter)
        if letter != word[-1]:
            index = index * 111
    return index


def make_t(n):
    t = []
    for i in range(n):
        t.append([])
    return t


def fill_t(array, func, n):
    t = make_t(n)
    # print(len(array))
    for i in range(2 * n):
        # print(i)
        index = func(array[i]) % n
        t[index].append(array[i])
    return t


def test_t(t):
    longest = 0
    count = 0
    for elem in t:
        if len(elem) > 0:
            count += 1
            if len(elem) > longest:
                longest = len(elem)
    return len(t) - count, longest, (len(t) * 2) / count


def run_test_t(data, size, function, times):
    results = [0, 0, 0]
    for i in range(times):
        temp = test_t(fill_t(data, function, size))
        results[0] += temp[0]
        results[1] += temp[1]
        results[2] += temp[2]
    return (results[0]/times, results[1]/times, results[2]/times)


functions = [[w, d, s], ['W', 'D', 'S']]
sizes = [17, 1031, 1024]
data = cleanup(tests)

for size in sizes:
    counter = 0
    # print('\n' + str(size))
    for function in functions[0]:
        results = run_test_t(data, size, function, 1000)
        # print(str(functions[1][counter]))
        # print(results)
        print('\n' + str(functions[1][counter]) + str(size))
        print('ilość pustych list:', results[0])
        print('maksymalna długość listy:', results[1])
        print('średnia długość niepustych list:', results[2])
        counter += 1

# zadanie 1
# Rozmiar 1031 dawał marginalnie lepsze wyniki od rozimaru 1024

# zadanie 2
# Tak, rodzaj funkcji haszującej wpływał na jakość wyniku.
# Przy dużym rozmiarze tablicy funkcja W była najlepsza, D trochę gorsza, a S wypadała najgorzej.
# Ta zależność nie występowała dla małych wielkości tablicy.

# wyniki
# W17
# ilość pustych list: 3.0
# maksymalna długość listy: 4.0
# średnia długość niepustych list: 2.4285714285714124
#
# D17
# ilość pustych list: 4.0
# maksymalna długość listy: 5.0
# średnia długość niepustych list: 2.615384615384619
#
# S17
# ilość pustych list: 1.0
# maksymalna długość listy: 4.0
# średnia długość niepustych list: 2.125
#
# W1031
# ilość pustych list: 140.0
# maksymalna długość listy: 7.0
# średnia długość niepustych list: 2.314253647587025
#
# D1031
# ilość pustych list: 159.0
# maksymalna długość listy: 7.0
# średnia długość niepustych list: 2.364678899082562
#
# S1031
# ilość pustych list: 325.0
# maksymalna długość listy: 13.0
# średnia długość niepustych list: 2.9206798866856163
#
# W1024
# ilość pustych list: 135.0
# maksymalna długość listy: 8.0
# średnia długość niepustych list: 2.30371203599547
#
# D1024
# ilość pustych list: 145.0
# maksymalna długość listy: 9.0
# średnia długość niepustych list: 2.32992036405009
#
# S1024
# ilość pustych list: 325.0
# maksymalna długość listy: 13.0
# średnia długość niepustych list: 2.9298998569384285