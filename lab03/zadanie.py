import random
from timeit import default_timer as timer
import sys

sys.setrecursionlimit(1000000)


def generator_niekorzystne(m):
    macierz = []
    for i in range(m):
        macierz.append(i)
    return macierz


def generator_losowe(m):
    macierz = []
    for i in range(m):
        macierz.append(random.randint(-100, 100))
    return macierz


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r+1):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    if i < r:
        return i
    else:
        return i - 1


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q)
        quicksort(array, q+1, r)


def quicksort_insertionsort(array, p, r):
    c = len(array) ** (1/2)
    if p < r:
        if (r - p + 1) <= c:
            insertionsort(array[p:(r + 1)])
        else:
            q = partition(array, p, r)
            quicksort_insertionsort(array, p, q)
            quicksort_insertionsort(array, q+1, r)


def insertionsort(array):
    n = len(array)
    for j in range(1, n):
        temp = array[j]
        i = j - 1
        while i >= 0 and array[i] > temp:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = temp


print("---Testy---\n")
m = 9
# test_insertion = generator_losowe(m)
test_quicksort = generator_losowe(m)
test_quicksort_insertionsort = generator_losowe(m)
# print('InsertionSort:')
# print(test_insertion)
# insertionsort(test_insertion)
# print(test_insertion, '\n')
print('QuickSort:')
print(test_quicksort)
quicksort(test_quicksort, 0, len(test_quicksort) - 1)
print(test_quicksort, '\n')
print('QuickSort-InsertionSort:')
print(test_quicksort_insertionsort)
quicksort_insertionsort(test_quicksort_insertionsort, 0, len(test_quicksort_insertionsort) - 1)
print(test_quicksort_insertionsort, '\n')

nn = [500, 1000, 1500, 2000, 2500]
print("---Quicksort---\n")
print("Dane losowe:")
for n in nn:
    start = timer()
    tablica = generator_losowe(n)
    quicksort(tablica, 0, n - 1)
    stop = timer()
    Tn = stop - start
    print(n, Tn)

print("\nDane niekorzystne:")
for n in nn:
    start = timer()
    tablica = generator_niekorzystne(n)
    quicksort(tablica, 0, n - 1)
    stop = timer()
    Tn = stop - start
    print(n, Tn)


print("\n---Quicksort-Insertionsort---\n")
print("Dane losowe:")
for n in nn:
    start = timer()
    tablica = generator_losowe(n)
    quicksort_insertionsort(tablica, 0, n - 1)
    stop = timer()
    Tn = stop - start
    print(n, Tn)

print("\nDane niekorzystne:")
for n in nn:
    start = timer()
    tablica = generator_niekorzystne(n)
    quicksort_insertionsort(tablica, 0, n - 1)
    stop = timer()
    Tn = stop - start
    print(n, Tn)


#                        DANE LOSOWE
# .---------.-----------------------.-------------------------.
# | Rozmiar |       QuickSort       | QuickSort-InsertionSort |
# :---------+-----------------------+-------------------------:
# |     500 | 0.0017993999999999996 |   0.0014281000000000432 |
# :---------+-----------------------+-------------------------:
# |    1000 | 0.0028698999999999947 |   0.0024185999999999375 |
# :---------+-----------------------+-------------------------:
# |    1500 |  0.004423400000000001 |    0.003750799999999943 |
# :---------+-----------------------+-------------------------:
# |    2000 |             0.0072686 |     0.00588450000000007 |
# :---------+-----------------------+-------------------------:
# |    2500 |  0.008899599999999994 |    0.008473799999999976 |
# '---------'-----------------------'-------------------------'


#             DANE NIEKORZYSTNE (ROSNĄCE)
# .---------.----------------------.-------------------------.
# | Rozmiar |      QuickSort       | QuickSort-InsertionSort |
# :---------+----------------------+-------------------------:
# |     500 | 0.016339199999999998 |    0.015309899999999876 |
# :---------+----------------------+-------------------------:
# |    1000 |  0.06491949999999999 |     0.06351119999999999 |
# :---------+----------------------+-------------------------:
# |    1500 |  0.15735230000000003 |     0.15635659999999985 |
# :---------+----------------------+-------------------------:
# |    2000 |  0.30648349999999996 |     0.37629939999999995 |
# :---------+----------------------+-------------------------:
# |    2500 |   0.4116837000000001 |      0.5857727000000001 |
# '---------'----------------------'-------------------------'
