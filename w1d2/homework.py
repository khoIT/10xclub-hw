# digital_root
def sum_digit(num):
  if num < 10:
    return num
  return num % 10 + sum_digit(num/10)
def digital_root(num):
  while num > 9:
    num = sum_digit(num)
  return num

# fibs
def fibs(num):
    if num == 0:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    arr = [1, 1]
    for i in xrange(2, num):
        arr.append(arr[i-1] + arr[i-2])
    return arr

# pair_sum
def add_in_order(arr, pair):
    if pair[0] > pair[1]:
        arr.append([pair[1], pair[0]])
    else:
        arr.append([pair[0], pair[1]])
    return arr

def pair_sum(arr, k):
    returned_list = []
    for number in arr:
        if k-number in arr:
            returned_list = add_in_order(returned_list, [number, k-number])
            arr.remove(number)
            arr.remove(k-number)
    return returned_list

# pair_sum_used_set
def pair_sum(arr, k):
    seen = Set()
    returned_list = []
    for number in arr:
        if k-number in seen:
            returned_list = add_in_order(returned_list, [number, k-number])
            seen.remove(k-number)
        else:
            seen.add(number)
    return returned_list
