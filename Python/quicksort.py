def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quicksort(left) + [pivot] + quicksort(right)
numbers=[5,2,8,2,1,6]
sortednumbers=quicksort(numbers)
print(sortednumbers)