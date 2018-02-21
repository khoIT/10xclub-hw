import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_start(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return value

    def add_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return value

    def add_at(self, index, value):
        ''' Only supporting index in 0 < index < len(linkedlist)'''
        node = Node(value)
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        if not curr:
            self.head = self.tail = node
            return index
        if curr.prev:
            curr.prev.next = node
            node.prev = curr.prev
        else:
            self.head = node
        curr.prev = node
        node.next = curr
        return index

    def delete_start(self, value):
        return True
    def delete_end(self, value):
        return True
    def delete_at(self, value):
        return True

    def get(self, index):
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        if curr:
            return curr.value
        else:
            return "None"

    def index_of(self, value):
        return True
    def print_to_file(self, filename):
        return True

def main(argv):
    double_link = LinkedList()
    double_link.add_at(1, 1)
    double_link.add_start(3)
    # double_link.add_start(2)
    # double_link.add_start(1)
    # double_link.add_end(5)
    # double_link.add_at(3, 4)
    # double_link.add_at(0, 0)
    for i in xrange(0, 5):
        print("Element index {} of list is: {}".format(i, double_link.get(i)))

if __name__ == '__main__':
    main(sys.argv[1:])
