"""
#### Algorithm
1. Separate the first element from the rest of the array. 
Think about it as a sorted list of one element.

2. For all other indices, beginning with [1]:

    a. Copy the item at that index into a temp variable

    b. Iterate to the left until you find the correct index in 
    the "sorted" part of the array at which this element should be 
    inserted  
    - Shift items over to the right as you iterate
    
    c. When the correct index is found, copy temp into this position

#### Your Task
- Implement the `insertion_sort()` function in the Guided Project 
with your TA
"""


# def insertion_sort(arr):

#     def mySort(new_arr):
#         for num in range(len(new_arr) - 1):
#             if new_arr[num] > new_arr[num + 1]:
#                 new_arr[num], new_arr[num + 1] = new_arr[num + 1], new_arr[num]
#         return arr

#     filtered_arr = mySort(arr)
#     while filtered_arr != mySort(filtered_arr):
#         return mySort(filtered_arr)


# def insertion_sort(arr):
#     for num in range(len(arr) - 1):
#         current_val = arr[num + 1]
#         print("Cur:", current_val)
#         for item in range(len(arr) - 1):
#             print("Arr:", arr[num], arr[num+1])


# my_arr = [10, 2, 43, 17, 44, 9, 15]
# print(insertion_sort(my_arr))
