
def dict_to_string(str):
    dict = {}
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def find_a_minimum_substring(start, end, to_find, str):
    to_find_dict = dict_to_string(to_find)

    while len(to_find_dict) > 0:
        if end == len(str):
            return 0, 0
        if str[end] in to_find_dict:
            if to_find_dict[str[end]] > 1:
                to_find_dict[str[end]] -= 1
            else:
                del to_find_dict[str[end]]
        end += 1

    to_find_dict = dict_to_string(to_find)
    substring_dict = dict_to_string(str[start:end])

    # remove unnecessary chars
    while str[start] in to_find_dict and substring_dict[str[start]] > to_find_dict[str[start]] or str[start] not in to_find_dict:
        substring_dict[str[start]] -= 1
        start += 1
    return start, end

def minimumSubstring(str, to_find):
    start, end = 0, 0
    minimumWindow = len(str)
    minimumStart, minimumEnd = 0, len(str)

    while end < len(str):
        start, end = find_a_minimum_substring(start, end, to_find, str)
        if start == end == 0:
            break
        if start and end:
            if end - start < minimumWindow:
                minimumWindow = end - start
                minimumStart = start
                minimumEnd = end
            start = end
    if start == end == 0:
        return "No substring found"
    return minimumStart, minimumEnd

if __name__ == "__main__":
    print minimumSubstring("daadcbddbadac", "abc")

    print minimumSubstring("zxcvbnm","as")
    print minimumSubstring("asdfg","g")

    print minimumSubstring("qwertyuiopwrypwqor","wr")
    print minimumSubstring("qwerwuiopwaypwqor","wr")
