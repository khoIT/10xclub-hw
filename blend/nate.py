mapping = {
    '0': None,
    '1': None,
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i']
}
"""
'232': ['a','b','c'], ['d','e','f'], ['a','b','c']
'22': ['a','b','c'], ['a','b','c']
string = 'ada','aea'
"""

def letter_generation(number_string):
    char_list_list = []
    for char in number_string:
        if char == '0' or char == '1':
            continue
        else:
            if char in mapping:
                char_list_list.append(mapping.get(char))

    res = [""]
    for char_list in char_list_list:
        new_res = []
        for char in char_list:
            for string in res:
                new_res.append(string + char)
        res = new_res
        new_res = []
    print len(res)
    return res

if __name__=="__main__":
    print letter_generation('22')
    print letter_generation('23')
    print letter_generation('232')
