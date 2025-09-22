def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # middle index
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1  # search right half
        else:
            high = mid - 1  # search left half
    return -1  # not found

arr = [2, 4, 6, 8, 10, 12, 14]  # Sorted array
key = int(input("Enter element to search: "))

result = binary_search(arr, key)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")
