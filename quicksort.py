def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i >= pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([8,9,1241324,2143123412,1,2,3,4,5,6,7]))

