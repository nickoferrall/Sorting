# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for num in range(i, len(arr)):
            if arr[smallest_index] > arr[num]:
                smallest_index = num

        # TO-DO: swap
        if smallest_index != cur_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr1 = [1, 15, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
