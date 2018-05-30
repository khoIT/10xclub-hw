# Question 1:
# Calculate the average word length.
# For the given set of words return the average word length.

# def avg_word_length(words):
#     # Your code here
#     if len(words) == 0:
#         return None
#     words = words.strip().split(' ')
#     total_length = 0
#     for word in words:
#         total_length += len(word)

#     result = float(total_length) / float(len(words))
#     return result

# assert avg_word_length('') == None
# assert avg_word_length('ibm') == 3
# assert avg_word_length('ibm microsoft') == 6
# assert avg_word_length(' Hello World ') == 5
# assert avg_word_length('The movie ends with The-end') == 4.6
# print('passed')

# Question 2:
# Check if a given IP address is valid.
# A valid IP address must be in the form of xxx.xxx.xxx.xxx,
# where xxx is a number from 0-255

# For example:
#           - 256.1.2.3 is not a valid IP address because the
#             first octet number is greater than 255
#           - 245.1.2 is not a valid IP address because
#             it has only 3 octets

# Note: We recommend you do NOT use regex to solve this question
# as it can be difficult and time consuming to debug. You may however, do
# so if you wish.

# def is_valid_IP(check_ip):
#     # Your code here
#     if check_ip is None:
#         return False

#     elements = check_ip.split('.')
#     if len(elements) != 4:
#         return False

#     for ele in elements:
#         if ele.isdigit() is False:
#             return False
#         if int(ele) > 255 or int(ele) < 0:
#             return False
#     return True

# assert is_valid_IP('') == False
# assert is_valid_IP('127.0.0.1') == True
# assert is_valid_IP('127.0.0.100') == True
# assert is_valid_IP('192.34.0.0.1') == False
# assert is_valid_IP('192.3.0.1') == True
# assert is_valid_IP('192.289.25.10') == False
# assert is_valid_IP('192.289.25') == False
# assert is_valid_IP('a12.A.29.5') == False
# print('passed')

# Question 3:
# Calculate the number of friends for each person
# given a relationship graph.
#
#
# For example:
#   The relationships amongst a set of friends
#   are shown in the graph below, where a line
#   between 2 nodes represents a friendship:
#
#                A ----- B ----- D
#                |      /
#                |   /
#                | /
#                C              E
#
#   This graph is represented as a list of
#   lists:
#      graph = [[A,B],[A,C],[C,B],[B,D],[E]]
#
#   The function "count_friends(graph)" should return
#   a dictionary object, where the Key is the
#   person's name and the Value is the number of
#   friends.
#
#   In the above example, the function should
#   return the following output:
#     {'A': 2, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

# def count_friends(input_graph):
#     # Your code here
#     return_dict = {}
#     for rel in input_graph:
#         if len(rel) == 1:
#             return_dict[rel[0]] = 0
#             continue
#         if rel[0] in return_dict:
#             return_dict[rel[0]] += 1
#         else:
#             return_dict[rel[0]] = 1
#         if rel[1] in return_dict:
#             return_dict[rel[1]] += 1
#         else:
#             return_dict[rel[1]] = 1
#     return return_dict



# def check_results(dict1, dict2):
#     if len(dict1.keys()) != len(dict2.keys()):
#         return 1
#     for i in dict1.keys():
#         if dict1[i] != dict2[i]:
#             return 1
#     return 0


# assert check_results(count_friends([['A'],['B'],['C'],['D'],['E']]), {'A': 0, 'C': 0, 'B': 0, 'D': 0, 'E': 0}) == 0
# assert check_results(count_friends([['A','B'],['C','D'],['E','F']]), {'A': 1, 'C': 1, 'B': 1, 'E': 1, 'D': 1, 'F': 1}) == 0
# assert check_results(count_friends([['A','B'],['A','C'],['A','D'],['E']]), {'A': 3, 'C': 1, 'B': 1, 'E': 0, 'D': 1}) == 0
# assert check_results(count_friends([['A','B'],['A','C'],['C','B']]), {'A': 2, 'C': 2, 'B': 2}) == 0
# assert check_results(count_friends([['A','B'],['A','C'],['C','B'],['B','D'],['E']]), {'A': 2, 'C': 2, 'B': 3, 'E': 0, 'D': 1}) == 0
# print('passed')
"""
Loops
for x in l:  "Iterate on x for each value in list"
for i in range(0,5): "Iterate on i from value 0 to 4"
for k, v in d.items(): "Iterate on each key, value pair in dict"

Lists (Array)
l = []  "Define an empty list"
l[i]  "Return value at index i in list"
len(l) "Return length of list"
pop() "Remove and return the last item in the list"
l.append(x) "Add value x to the end of list"
l.sort() "Sort values in list - in place sort, returns None"
sorted(l) "Return sorted copy of list"
x in l: "Evaluate True if x is contained in the list"

Dictionary (HashMap)
d = {}  "Define an empty Dictionary"
d[x]  "Return value for key x"
d[x] = 1 "Set value for key x to 1"
d.keys()  "Return list of keys"
d.values() "Return list of values"

Tuple
tup = ()
tup = (1,2) + tup

Other functions
reversed(n)  "reverse a list"
random.random()  "random number between 0 and 1"
isinstance(x, list)     "returns True is x is instance of list"
int() "Return an integer object constructed from a number or string x"
isdigit()    "returns true if all characters in the string are digits
split()    "returns a list of all the words in the string"
ceil()    "returns the smallest integer value greater than or equal to x"
"""

# Question:
# Return True if a given string containing the
# following kinds of brackets is balanced
# else return False
#    (, )
#    [, ]
#    {, }
#    <, >
# For example:
#           - "{Hello}(World)" is balanced
#              because every kind of opening bracket
#              has a corresponding closing bracket.
#           - "{Hi(There)" is not balanced
#              because '{' does not have a
#              corresponding closing '}' bracket.
#           - "}Balanced{(Not)" is not balanced
#              because '}' is before the
#              corresponding opening '{' bracket.
#           - "Balanced{(Not})" is not balanced
#              because '}' is closed before the
#              currently open "(" bracket.

# def is_balanced(input_str):
#     # Your code here
#     mapping = {
#         ']': '[',
#         '}': '{',
#         '>': '<',
#         ')': '('
#     }

#     if len(input_str) == 0:
#         return None
#     paren = []
#     for char in input_str:
#         if char in ['(','{','[','<']:
#             paren.append(char)
#         print paren
#         print char
#         if char in [')','}',']','>']:
#             if len(paren) == 0:
#                 return False
#             else:
#                 if paren.pop() != mapping[char]:
#                     return False


#     if len(paren) != 0:
#         return False

#     return True




# # assert is_balanced('') == None
# # assert is_balanced('This<might>not(be{balanced}') == False
# assert is_balanced('{(<[SimpleExampleForBalanced]>)}') == True
# assert is_balanced('{)(<[This]is>not)balanced}') == False
# assert is_balanced('{(<[simple])>}') == False
# assert is_balanced('{Another{Example<of>Unbalanced}String') == False
# assert is_balanced('(This)is<how>balanced{string}with[paranthesis]canbe') == True
# print('passed')
