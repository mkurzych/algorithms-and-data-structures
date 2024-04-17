
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_insert(self, x):
        x.next = self.head
        self.head = x

    def list_search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def list_delete(self, x):
        if x is not None:
            x.key = x.next.key
            x.next = x.next.next

    def list_print(self):
        x = self.head
        nodes = []
        while x is not None:
            nodes.append(x.key)
            x = x.next
        print(" -> ".join(nodes))

    def list_no_repetitions(self):
        wynik = LinkedList()
        x = self.head
        while x is not None:
            if wynik.list_search(x.key) is None:
                wynik.list_insert(Node(x.key))
            x = x.next
        return wynik


def list_scale(l1, l2):
    x = l1.head
    while x.next is not None:
        x = x.next
    x.next = l2.head


l = LinkedList()
for elem in ['ala', 'ma', 'kota', 'kot', 'ma', 'alę']:
    l.list_insert(Node(elem))
    l.list_print()
l.list_delete(l.list_search('kotta'))
l.list_print()
w = l.list_no_repetitions()
w.list_print()
list_scale(l, w)
l.list_print()
