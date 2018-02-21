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
        self.length = 0

    def add_start(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return value

    def add_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return value

    def add_at(self, index, value):
        ''' Only supporting index in 0 <= index < len(linkedlist)
        '''
        print("Adding {} at index {}".format(value, index))
        if index > self.length or index < 0:
            return -1

        node = Node(value)
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        if not curr:
            self.head = self.tail = node
            self.length += 1
            return index
        if curr.prev:
            curr.prev.next = node
            node.prev = curr.prev
        else:
            self.head = node
        curr.prev = node
        node.next = curr
        self.length += 1
        return index

    def delete_start(self):
        print("Deleting start")
        if self.length == 0:
            return -1
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return 0
        else:
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return 0

    def delete_end(self):
        print("Deleting end")
        if self.length == 0:
            return -1
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return 0
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return 0

    def delete_at(self, index):
        print("Deleting at index {}".format(index))
        if self.length == 0 or index > self.length or index < 0:
            return -1
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        self.length -= 1
        return index

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
        curr = self.head
        index = 0
        while curr:
            if curr.value == value:
                return index
            index += 1
            curr = curr.next
        return -1

    def print_to_file(self, filename):
        return True

def main(argv):
    double_link = LinkedList()
    double_link.add_at(3, 15)
    double_link.add_start(3)
    double_link.add_start(2)
    double_link.add_start(1)
    double_link.add_end(5)
    double_link.add_at(3, 4)
    double_link.add_at(0, 0)
    for i in xrange(0, double_link.length):
        print("Element index {} of list is: {}".format(i, double_link.get(i)))

    double_link.delete_start()
    for i in xrange(0, double_link.length):
        print("Element index {} of list is: {}".format(i, double_link.get(i)))

    double_link.delete_end()
    for i in xrange(0, double_link.length):
        print("Element index {} of list is: {}".format(i, double_link.get(i)))

    double_link.add_at(0, 0)
    double_link.delete_at(3)
    for i in xrange(0, double_link.length):
        print("Element index {} of list is: {}".format(i, double_link.get(i)))
    print("Element with value {} in list is at index: {}".format(3, double_link.index_of(3)))
    print("Element with value {} in list is at index: {}".format(4, double_link.index_of(4)))
if __name__ == '__main__':
    main(sys.argv[1:])
