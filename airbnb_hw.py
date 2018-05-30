def lookupChar(char, to_find):
    if char in to_find:
        if to_find[char] >= 1:
            to_find[char] -= 1
        if to_find[char] == 0:
            del to_find[char]
def alphabet_to_dict(alphabet):
    to_find = {}
    for char in alphabet:
        if char in to_find:
            to_find[char] += 1
        else:
            to_find[char] = 1
    return to_find

def find_char_in_to_find(char, to_find):
    if char in to_find:
        return to_find[char]
    else:
        return -1

def minimumSubstring(st, alphabet):
    to_find = alphabet_to_dict(alphabet)
    start, end = 0,0
    windows = []

    while end < len(st):
        new_hash = {}
        while len(to_find) > 0:
            if end == len(st):
                return ""
            if st[end] in new_hash:
                new_hash[st[end]] += 1
            else:
                new_hash[st[end]] = 1
            lookupChar(st[end], to_find)
            end += 1

        to_find = alphabet_to_dict(alphabet)
        while new_hash[st[start]] > find_char_in_to_find(st[start],to_find):
            new_hash[st[start]] -= 1
            start += 1
        windows.append((start, end))
        if end < len(st):
            end -= 1
            start = end

    min = len(st)
    min_substring = st
    for start, end in windows:
        if end-start < min:
            min = end-start
            min_substring = st[start:end]
    if min < len(st):
        return min_substring
    else:
        return ""


if __name__ == "__main__":
    print minimumSubstring("daadcbddbadac", "abc")

    print minimumSubstring("zxcvbnm","as")
    print minimumSubstring("asdfg","g")

    print minimumSubstring("qwertyuiopwrypwqor","wr")
    print minimumSubstring("qwerwuiopwaypwqor","wr")
