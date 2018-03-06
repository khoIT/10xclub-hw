# geeksforgeeks testing code
def is_palindrome(string):
    idx = len(string) // 2 -1
    while idx >= 0:
        if string[idx] != string[len(string)-1-idx]:
            return False, idx
        idx -= 1
    return True, -1

def closest_palindrome(string_n):
    if int(string_n) < 10:
        return int(string_n)-1
    res, idx = is_palindrome(string_n)
    # end_idx = len(string_n) - 1 - idx
    # if string_n[end_idx] ==
    if res != True:
        diff =  int(string_n[:idx+1][::-1]) - int(string_n[len(string_n)-1-idx:])
        return int(string_n) + diff
    else:
        # this is a palindrome
        if len(string_n) % 2 != 0:
            mid = len(string_n) // 2
            if string_n[mid] == '0':
                new_int = int(string_n) - pow(10,mid)
                return closest_palindrome(str(new_int))
            elif string_n[mid] == '9':
                new_int = int(string_n) + pow(10,mid)
                return closest_palindrome(str(new_int))
            else:
                return int(string_n) - pow(10,mid)
        else:
            mid = len(string_n) // 2 - 1
            if string_n[mid] == '0':
                new_int = int(string_n) - pow(10,mid)
                return closest_palindrome(str(new_int))
            elif string_n[mid] == '9':
                new_int = int(string_n) + pow(10,mid)
                return closest_palindrome(str(new_int))
            else:
                return int(string_n) - pow(10, mid) - 1

def main():
    array = ['9', '99', '999', '500999', '500899', '11911']
    for n in array:
        print "Closest palindrome of {} is {}. Diff: {}".format(n, closest_palindrome(n), abs(int(n)-closest_palindrome(n)))

if __name__=="__main__":
    main()
