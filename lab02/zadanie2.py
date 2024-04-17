import random
numbers = open('numbers.txt', 'w')
final = open('final.txt', 'w')


def heapify_iteracyjnie(array, size, i):
    temp_arr = [i]
    for j in temp_arr:
        left = (2 * j) + 1
        right = (2 * j) + 2
        if left < size and array[left] > array[j]:
            largest = left
        else:
            largest = j
        if right < size and array[right] > array[largest]:
            largest = right
        if largest != j:
            temp_arr.append(largest)
            temp = array[j]
            array[j] = array[largest]
            array[largest] = temp
    return array


def build_heap(array):
    size = len(array)
    k = int((len(array) - 2) / 2)
    for i in range(k, -1, -1):
        heapify_iteracyjnie(array, size, i)
    return array


def heap_sort(array):
    array = build_heap(array)
    size = len(array)
    for i in range(len(array) - 1, 0, -1):
        temp = array[0]
        array[0] = array[size - 1]
        array[size - 1] = temp
        size -= 1
        heapify_iteracyjnie(array, size, 0)
    return array


def generator(n, file):
    for i in range(n):
        file.write(str(random.randint(-100, 100)) + '\n')


def cleanup(file):
    temp = file.readlines()
    array = []
    for elem in temp:
        array.append(int(elem[:-1]))
    return array


def convert(array, file):
    for line in array:
        file.write(str(line) + '\n')


m = int(input('Podaj ilość liczb: '))
generator(m, numbers)
numbers.close()
numbers = open('numbers.txt', 'r')
tablica = cleanup(numbers)
heap_sort(tablica)
convert(tablica, final)
