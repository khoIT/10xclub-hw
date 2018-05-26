"""
group_randomizer
to generate groups of names with size from 3-5
sum of all names in those groups must add up to the size of the name_list


5 => 5
6 => 3, 3
7 => 3, 4
8 => 3,5 || 4,4
9 =>


10=> 3,3,4
11=>
"""
"""
name_list = [['a','b','c'],['d','e']]
group_randomizer(name_list) = ['e','b','c'], ['d','a']
group_randomizer(name_list) = ['a','b'], ['d','a','e']
"""
from random import randrange
import copy

def temp_omitted_team_index(name_list, chosen_user):
    idx = 0
    while idx < len(name_list):
        for user in name_list[idx]:
            if user == chosen_user:
                return idx
        idx += 1
    return None

def remove_employee(name_list, flatten_name_list, index):
    # return name_list with employee removed from the original group
    removed = flatten_name_list[index]
    for group in name_list:
        idx = 0
        while idx < len(group):
            if group[idx] == removed:
                del group[idx]
                return name_list
            idx += 1
    return name_list

def restore_temp_omitted_users(original_name_list, temp_omitted_index_list, name_list):
    while idx < len(original_name_list):
        if idx in temp_omitted_index_list:
            name_list.append(original_name_list[idx])
    return name_list

def group_randomizer(name_list):
    name_list = copy.deepcopy(name_list)
    original_name_list = copy.deepcopy(name_list)
    grouping = []

    while len(name_list) > 0:
        group = []
        temp_omitted_index_list = []
        while len(group) < 3:
            if len(name_list) == 0:
                break

            flatten_name_list = []
            for group in name_list:
                for name in group:
                    flatten_name_list.append(name)
            index = randrange(0, len(flatten_name_list))
            chosen_user = flatten_name_list[index]
            group.append(chosen_user)
            name_list = remove_employee(name_list, flatten_name_list, index)

            # add back temp omitted index team
            temp_omitted_index = temp_omitted_team_index(name_list, chosen_user)
            temp_omitted_index_list.append(temp_omitted_index)
            if len(name_list) > 1:
                del name_list[temp_omitted_index]

        if len(group) >= 3:
            grouping.append(group)
            group = []
            idx = 0
            # restore temp omitted users
            name_list = restore_temp_omitted_users(original_name_list, temp_omitted_index_list, name_list)


    grouping[-1] = grouping[-1] + group
    return grouping

# grouping = group_randomizer([['a','b','c'],['d','e','f']])
# print len(grouping) == 2
# print len(grouping[0]) == 3
# print len(grouping[1]) == 3
# print grouping
#
# grouping = group_randomizer(['a','b','c','d','e','f','g'])
# print len(grouping) == 2
# print len(grouping[0]) == 3
# print len(grouping[1]) == 4
# print grouping
#
# # grouping = group_randomizer(['a','b'])
# # print len(grouping) == 1
# # print len(grouping[0]) == 2
# # print grouping
#
# grouping = group_randomizer(['a','a','b','b','c','c','d','d','e','e','f','f','g','g','h','h'])
# print len(grouping) == 5
# print len(grouping[0]) == 3
# print len(grouping[-1]) == 4
# print grouping

grouping = remove_employee([['a','b','c'],['d','e','f']],['a','b','c','d','e','f'],4)
print len(grouping) == 2
print len(grouping[0]) == 3
print len(grouping[1]) == 2
print grouping[0] == ['a','b','c']
print grouping[1] == ['d','f']
