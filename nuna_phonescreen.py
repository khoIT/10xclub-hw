"""
HIGHEST SCORING WORDS
=====================

Given a list of words:

    EXAMPLE WORD LIST:
    - red
    - cat
    - kitten
    - purple
    - frog

Write a function that outputs the pair that satisfies the following two requirements:

1. The pair of words do not share any characters.
2. Given a score function of `len(word_1) * len(word_2) = score`, the pair of words must have the highest score of all pairs that satisfy the first condition.

    cat + kitten  => not candidates, overlapping letters
    kitten + frog => best answer

"""
"""
words = ['red','cat','kitten','purple','frog']

sorted_words = arr = ['kitten','purple','frog','red','cat']
arr[0]*arr[2] >= arr[0] * arr[3..n]
              >= arr[1]*arr[2]
"""


seen_by_word = {}

def is_valid_pair(word_1, word_2):
    seen = {}
    if word_1 in seen_by_word:
        seen = seen_by_word[word_1]
    else:
        for char in word_1:
            seen[char] = 1
    for char in word_2:
        if char in seen:
            return False
    return True

def highest_score_pair(words):
    word_1, word_2 = words[0], words[1]
    max_score = 0
    idx = 0
    while idx < len(words):
        j_idx = idx+1
        while j_idx < len(words):
            if is_valid_pair(words[idx], words[j_idx]):
                score = len(words[idx]) * len(words[j_idx])
                if score > max_score:
                    max_score = score
                    word_1 = words[idx]
                    word_2 = words[j_idx]
            j_idx += 1
        idx += 1

    return word_1, word_2

words = ['red','cat','kitten','purple','frog']
print is_valid_pair('cat','rat') == False
print is_valid_pair('cat','') == True
print is_valid_pair('red','cat') == True
print highest_score_pair(words) == ('kitten','frog')
