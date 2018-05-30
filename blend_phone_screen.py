#Create a fcn that calls an elevator in the most efficient way possible. ie. minimum amount of
#wait time for the caller. This function should take in a floor and return the correct elevator.

# Assumptions:
#  - 2 elevators
#  - 5 seconds to get to a floor
#  - instantly stops on a floor and can move to the next
#  - 9 floors
#  - the elevator must finish its trip before it can come get you


# New Assumptions:
#  - 3 elevators
#  - 5 seconds to get to a floor
#  - 10 seconds to stop on a floor
#  - 20 floors
#  - the elevator must finish its trip before it can come get you

# Assumptions:
#  - 3 elevators
#  - 5 seconds to get to a floor
#  - 10 seconds to stop on a floor
#  - 40 floors
#  - the elevator must finish its trip before it can come get you



class Elevator(object):
    def __init__(self, id, position, destination):
        self.id = id
        self.position = position
        self.destination = destination


e1 = Elevator(id=1, position=0, destination=4)
e2 = Elevator(id=2, position=4, destination=2)
elevators=[e1, e2]

def time_to_floor(floor, ele):
    time_per_floor = 5
    stop_time = 10
    if ele.destination == ele.position:
        stop_time = 0
    current_trip_time = time_per_floor*abs(ele.destination-ele.position)
    to_floor_time =  time_per_floor*abs(floor-ele.destination)
    return  current_trip_time + stop_time + to_floor_time

def elevator(floor, elevators):
    chosen_ele = elevators[0]
    min_time = time_to_floor(floor, chosen_ele)

    for ele in elevators:
        if time_to_floor(floor, ele) < min_time:
            min_time = time_to_floor(floor, ele)
            chosen_ele = ele
    return chosen_ele.id

print time_to_floor(2, e1) == 40
print time_to_floor(2, e2) == 20
print elevator(2, elevators) == e2.id

print time_to_floor(0, e2) == 30
print time_to_floor(0, e1) == 50
print elevator(0, elevators) == e2.id

 # - E1 being on floor 2 going to 4
 #  - E2 being on floor 6 at standstill
 #  Call an elevator from floor 1
e1 = Elevator(id=1, position=2, destination=4)
e2 = Elevator(id=2, position=6, destination=6)
print time_to_floor(1, e1) == 35
print time_to_floor(1, e2) == 25
print elevator(1, [e1,e2]) == e2.id


#- E1 being on floor 2 going to 6      -> 35
#- E2 being on floor 9 going to 20     -> 130
#- E3 being on floor 13 at standstill  -> 30
#   call an elevator from floor 7
#   Answer: it calls E3

e1 = Elevator(id=1, position=2, destination=6)
e2 = Elevator(id=2, position=9, destination=20)
e3 = Elevator(id=3, position=13, destination=13)
print time_to_floor(7, e1) == 35
print time_to_floor(7, e2) == 130
print time_to_floor(7, e3) == 30
print elevator(7, [e1,e2,e3]) == e3.id
