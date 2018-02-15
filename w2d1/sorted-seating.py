'''
sorted seating
Jane is hosting a birthday party. In order to treat her guests fairly, she planned on seating them around a circular table, in alphabetical order.
Jane decided to write a program to keep track of the table plan as her guests RSVP'd. She wanted to run the program as the guests arrived and allow
them to enter their name and find out who the two people the guest will be sitting next to. Help Jane out by writing a class that will:
Level 1:
allow guests to be added via .add(name) in O(n) time
allow guests to retrieve a 2 element list of the names of the guests seated next to them, ordered [left, right] via .get(name) in O(n) time
use native arrays/objects as underlying data structure - no high level structures
Level 2:
implement a .delete(name) method that allows Jane to remove guests who dont show up in O(n) time
Level 3:
increase the performance of any of the 3 methods to O(log n)?
'''
class ListGuest(object):
    def __init__(self):
        self.array = []

    def add(self, name):
        
