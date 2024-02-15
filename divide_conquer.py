def sum_recursive(arr):
    if arr == []:
        return 0
    return arr[0] + sum_recursive(arr[1:])

print(sum_recursive([1,2,3]))

def count_recursive(arr):
    if arr == []:
        return 0
    return 1 + count_recursive(arr[1:])

print(count_recursive([1,2,3,4,5]))

def max_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_arr(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max_arr([1,2,3,4,5,50]))