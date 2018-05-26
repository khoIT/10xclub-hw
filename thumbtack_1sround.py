# Enter your code here. Read input from STDIN. Print output to STDOUT
# addEvent
# deleteEvent
# getEventsForDay

class Event(object):
    last_id = 0
    def __init__(self, eventTitle, startTime, endTime):
        self.id = Event.last_id
        self.eventTitle = eventTitle
        self.startTime = startTime
        self.endTime = endTime
        Event.last_id += 1

"""
data = {
    '2018-05-08': [event1, event2]
}
"""

def addEvent(date, event):
    if date in data:
        data[date].append(event)
    else:
        data[date] = [event]
    # events[event.id] = event
    return data

def deleteEvent(date, eventId):
    if date in data:
        for idx, event in enumerate(data[date]):
            if event.id == eventId:
                del data[date][idx]


def getEventsForDay(date):
    return data[date]


data = {}
# events = {}
event0 = Event('Joe x Khoi', '11:00', '12:00')
print event0.id == 0
print Event.last_id # debug
addEvent('2018-05-08', event0)
# print len(events) == 1
print len(data['2018-05-08']) == 1

event1 = Event('Lunch', '12:00', '12:30')
print event1.id == 1
addEvent('2018-05-08', event1)
# print len(events) == 2

deleteEvent('2018-05-08', 0)
# print len(events) == 1
print data['2018-05-08'][0].id
print data['2018-05-08'] == [event1]


event2 = Event('Joe x Khoi', '11:00', '12:00') # id = 2
addEvent('2018-05-08', event2)
deleteEvent('2018-05-08', 2)
print data['2018-05-08'] == [event1]
