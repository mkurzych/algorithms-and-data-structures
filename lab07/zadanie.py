import random


class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None
        # self.amount = 1


class binarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, x, k):
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def insert(self, z):
        if self.root is None:
            self.root = z
            return

        x = self.root
        y = None
        while x is not None:
            y = x
            if z.key == x.key:
                # x.amount += 1
                return
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        # if z.key == y.key:
        #   y.amount += 1
        if z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if not node:
            return None
        elif key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            # if node.amount > 1:
            #     node.amount -= 1
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self.bst_minimum(node.right)
                node.key = min_node.key
                # node.count = min_node.amount
                node.right = self._delete(min_node.key, node.right)
        return node

    def bst_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def print(self):
        self._print(self.root, self.height())

    def print_part(self, res):
        self._print(self.root, res)

    def _print(self, node, res, level=0):
        if node is not None and level <= res:
            self._print(node.right, res, level + 1)
            print(" " * 6 * level + str(node.key))
            self._print(node.left, res, level + 1)

    # def _print(self, node, res, level=0):
    #     if node is not None and level <= res:
    #         self._print(node.right, res, level + 1)
    #         print(" " * 6 * level + str(node.key) + f"({node.amount})")
    #         self._print(node.left, res, level + 1)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left = self._height(node.left)
            right = self._height(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1


# dane
data = []
with open('words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        data.append(word)
# w tym pliku są alfabetycznie,
# więc dla lepszych wyników
# randomizujemy listę
random.shuffle(data)

# testy
bst = binarySearchTree()
amount = [0, 500, 1000, 1500, 2000]
for i in range(4):
    words = data[amount[i]:amount[i + 1]]
    for word in words:
        bst.insert(Node(word))
    print('-' * 50)
    print('Liczba elementów w drzewie:', amount[i+1], '\nWysokość drzewa:', bst.height())
print('-' * 50)
print('Drzewo do poziomu 3:')
bst.print_part(3)
print('-' * 50)

# test delete
# bst.delete(data[0])
# bst.print_part(3)

# test search
# print(bst.search(bst.root, data[5]).key)
# print(data[5])

# --------------------------------------------------
# Liczba elementów w drzewie: 500
# Wysokość drzewa: 21
# --------------------------------------------------
# Liczba elementów w drzewie: 1000
# Wysokość drzewa: 23
# --------------------------------------------------
# Liczba elementów w drzewie: 1500
# Wysokość drzewa: 24
# --------------------------------------------------
# Liczba elementów w drzewie: 2000
# Wysokość drzewa: 24
# --------------------------------------------------
# Drzewo do poziomu 3:
#                   write
#             wings
#                   wells
#       waiting
#                   thee
#             suspension
#                   moore
# marine
#                   locally
#             helmet
#                   dame
#       adventures
#                   accounts
#             academy
#                   absolutely
# --------------------------------------------------
