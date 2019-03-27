'''
# Selection Sort
***Selection Sort*** is an algorithm that many of you have probably used before when sorting things in your everyday lives. Imagine that you have several books you want to arrange on a shelf from shortest to tallest. You start off by looking for the shortest book, and when you find it, put it on the far left side of the shelf. Then, you look for the second shortest book and insert it directly to the right of the first book. You repeat this process, selecting the next shortest book and moving it next to the most recently placed book, until you have moved all books into the correct place. This is ***Selection Sort***.

An example of this algorithm being applied to an array with 10 numerical elements can be seen in the video below.

[(VIDEO) Select-sort with Gypsy folk dance](https: // www.youtube.com/watch?v=Ns4TPTC8whw)

[![(VIDEO) Select-sort with Gypsy folk dance](https://i.ytimg.com/vi/Ns4TPTC8whw/hqdefault.jpg)](https: // www.youtube.com/watch?v=Ns4TPTC8whw)

# Algorithm
1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop

# Implementation in Python
'''


def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# try it out
my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
# print(my_arr)
# arr = selectionSort(my_arr)
print(selectionSort(my_arr))
# print(my_arr)
