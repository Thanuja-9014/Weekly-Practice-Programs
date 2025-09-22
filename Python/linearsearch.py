def linear_search(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
    return -1


A = [2, 4, 6, 8, 10, 12, 14]
target = int(input("Enter element to search: "))


result = linear_search(A, target)

if result != -1:
    print(f"Linear Search: Element found at index {result}")
else:
    print("Linear Search: Element not found")
