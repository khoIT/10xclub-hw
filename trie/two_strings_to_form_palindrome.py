def two_strings_palindrome(arr):
    reversed = {}
    for string in arr:
        if string in reversed:
            return reversed.get(string), string
        if len(string) > 1:
            reversed[string[::-1]] = string
            reversed[string[:-1][::-1]] = string
    for string in arr:
        if string in reversed:
            return reversed.get(string), string

if __name__ == "__main__":
    print two_strings_palindrome(['abc', 'ta', 'ba','cba'])
    print two_strings_palindrome(['abc', 'cd', 'c', '123', '3', 'cba'])
    print two_strings_palindrome(['abc', 'ba']) # {'cba': 'abc'; 'ba': 'abc'}
