'''multi-sorted contestants

A local sports event broadcasting company wants to build an automated display to show how contestant stack up. Each contestant has 3 metrics, an age, height and weight.
They want to store the data of each contestant in a structure that allows them to easily get the order of the contestant based on any of the 3 metrics.
Help the broadcasting company out by writing a multi-handle linked list. Implement the following:

Level 1:
an add method add(name, age, height, weight), that adds a contestant, with their metrics, to the list in O(n)
a sorted method sorted(metric), that takes in either 'A', 'H', or 'W' and returns the list of competitors names sorted by that metric, in O(n), ascending
use only native arrays/objects, no high level types
Level 2:
add a delete method to remove contestants by name delete(name), which removes an item from the list.
can you add another param to sorted sorted(metric, asc), a bool flag indicating sorting direction, in O(n)
Level 3:
Can you extend this data structure to allow for any metrics?
Can you write a method that returns the position of a given contestant in each metric category?
'''
import copy
import sys

class Node(object):
    def __init__(self, name, metric_type, data):
        self.name = name
        self.type = metric_type
        self.data = data
        self.prev = None
        self.next = None

class Contestant(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.ageNode = Node(name, 'age', age)
        self.heightNode = Node(name, 'height', height)
        self.weightNode = Node(name, 'weight', weight)

class ContestantList(object):
    def __init__(self):
        self.database = {}
        self.age_front = None
        self.age_tail = None
        self.weight_front = None
        self.weight_tail = None
        self.height_front = None
        self.height_tail = None

    def __inserting_node_to_list(self, front, tail, node):
        # base case 1: empty list
        if front == None:
            front = tail = node
        # base case 2: 1 element list
        elif front == tail:
            if front.data < node.data:
                tail = node
            else:
                front = node
            front.next = tail
            tail.prev = front
        # from 2 items above
        else:
            tempNode = front
            while node.data > tempNode.data and tempNode.next != None:
                tempNode = tempNode.next
            if tempNode == front:
                tempNode.prev = node
                node.next = tempNode
                front = node
            elif node.data > tail.data:
                tempNode.next = node
                node.prev = tempNode
                tail = node
            else:
                tempNode.prev.next = node
                node.prev = tempNode.prev
                node.next = tempNode
                tempNode.prev = node
        return front, tail

    def __return_name_list(self, front, tail):
        output = []
        tempNode = copy.deepcopy(front)
        while tempNode:
            output.append(tempNode.name)
            tempNode = tempNode.next
        return output

    def add(self, name, age, weight, height):
        if name not in self.database:
            new = Contestant(name, age, weight, height)
            self.age_front, self.age_tail = self.__inserting_node_to_list(self.age_front, self.age_tail, new.ageNode)
            self.weight_front, self.weight_tail = self.__inserting_node_to_list(self.weight_front, self.weight_tail, new.weightNode)
            self.height_front, self.height_tail = self.__inserting_node_to_list(self.height_front, self.height_tail, new.heightNode)
            self.database[name] = new

    def getAge(self, name):
        person = self.database.get(name)
        return person.ageNode.data

    def sorted(self, metric):
        if metric == 'A':
            return self.__return_name_list(self.age_front, self.age_tail)
        elif metric == 'W':
            return self.__return_name_list(self.weight_front, self.weight_tail)
        elif metric == 'H':
            return self.__return_name_list(self.height_front, self.height_tail)

def main(argv):
    cl = ContestantList()
    cl.add('Andy', 17, 180, 10)
    cl.add('Bob',  32, 170, 9)
    cl.add('Jacob',30, 175, 8)
    cl.add('Mary', 20, 160, 7)
    print ("Andy's age is: {}".format(cl.getAge('Andy')))
    print ("List of competitors in order of age: {}".format(cl.sorted('A')))
    print ("List of competitors in order of weight: {}".format(cl.sorted('W')))
    print ("List of competitors in order of height: {}".format(cl.sorted('H')))
if __name__ == '__main__':
    main(sys.argv[1:])
