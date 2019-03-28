# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO
    answer_arr = []
    for i in range(elements):
        if len(arrA) == 0:
            answer_arr.extend(arrB)
            break
        elif len(arrB) == 0:
            answer_arr.extend(arrA)
            break
        elif arrA[0] < arrB[0]:
            answer_arr.append(arrA[0])
            del arrA[0]
        else:
            answer_arr.append(arrB[0])
            del arrB[0]

    return answer_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    print(left, right)
    return merge(left, right)


arr1 = [11, 23, 1, 300, 43, 15]
print(merge_sort(arr1))

# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
