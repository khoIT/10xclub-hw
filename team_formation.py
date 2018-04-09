"""
Team Formation
n - is the number of scores of employees to choose from
arr - is the list of employees' score
team - is the number of team members to be chosen
m - is the number of first or last elements of the arr to choose from
"""

def teamFormation_naive(score, team, m):
    count = 0
    sum_score = 0
    while count < team:
        sum_score += max_score_naive(score, m)
        count += 1
    return sum_score

def max_score_naive(score, m):
    index = 0
    max_index = 0
    max_ele = score[max_index]
    if len(score) < m:
        while index < len(score):
            if score[index] > max_ele:
                max_ele = score[index]
                max_index = index
            index += 1
    else:
        while index < m and index <= len(score)/2:
            if score[index] > max_ele:
                max_ele = score[index]
                max_index = index
            if score[len(score)-1-index] > max_ele:
                max_ele = score[len(score)-1-index]
                max_index = len(score)-1-index
            index += 1
    del score[max_index]
    return max_ele

def teamFormation(score, team, m):
    count = 0
    sum_score = 0
    index = 0
    while count < team:
        if m > len(arr)/2
            working_arr = score
        else:
            working_arr = score[:m] + score[-m:]
        working_arr = sorted(working_arr, reverse=True)
        sum_score += working_arr[0]

        # trace back in original arr
        while index < m and index <= len(score)/2:
            if score[index] > max_ele:
                max_ele = score[index]
                max_index = index
            if score[len(score)-1-index] > max_ele:
                max_ele = score[len(score)-1-index]
                max_index = len(score)-1-index
            index += 1

        count += 1
    return sum_score

if __name__ == "__main__":
    print teamFormation([17, 12, 10, 2, 7, 2, 11, 20, 8], 3 ,4) == 49

    # 18 + 18 + 14 + 12 + 10 + 9
    print teamFormation([6, 18, 8, 14, 10, 12, 18, 8, 9], 8 ,4) == 97
    # [6,  8, 8]

    # 18 + 7 + 9 + 15 + 11 = 60
    print teamFormation([18, 5, 15, 18, 11, 15, 9, 7], 5, 1) == 60
