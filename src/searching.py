# STRETCH: implement Linear Search
def linear_search(arr, target):
    for item in range(len(arr)):
        if arr[item] == target:
            return item
    return -1   # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# print(linear_search(arr1, 0))
# print(linear_search(arr1, 6))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    mid = int(len(arr) / 2)
    while arr[mid] != target:
        if low == high:
            return -1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = int((high + low) / 2)
    return mid


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = int((low+high)/2)
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if low > high:
        return -1
    elif arr[middle] == target:
        return middle
    elif arr[middle] < target:
        low = middle + 1
        return binary_search_recursive(arr, target, low, high)
    else:
        high = middle - 1
        return binary_search_recursive(arr, target, low, high)
    return middle


# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []

# print(binary_search_recursive(arr1, -8, 0, len(arr1)-1))
# print(binary_search_recursive(arr1, 0, 0, len(arr1)-1))
print(binary_search_recursive(arr2, 6, 0, len(arr2)-1))
# print(binary_search_recursive(arr2, 0, 0, len(arr2)-1))


# self.assertEqual(binary_search_recursive(arr1, -8, 0, len(arr1)-1), 1)
# self.assertEqual(binary_search_recursive(arr1, 0, 0, len(arr1)-1), 6)
# self.assertEqual(binary_search_recursive(arr2, 6, 0, len(arr1)-1), -1)
# self.assertEqual(binary_search_recursive(arr2, 0, 0, len(arr1)-1), -1)
