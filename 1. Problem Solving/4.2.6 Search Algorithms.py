import time

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def linear_search(input_list: list, target: int) -> int:
    """If available, returns the index of the item in the list, else returns -1"""
    start = time.time() # start time of function
    item_index = -1 # default return index, just in case the item isn't found
    for item in range(len(input_list)): # iterates through the list
        if input_list[item] == target: # checks if the target is found
            item_index = item # sets the target index to the current one
            break
    end = time.time() # end time of function
    time_taken = end-start # calculates the time taken
    return item_index, time_taken # returns both the target index, and time taken

def binary_search(input_list: list, target: int) -> int:
    start = time.time() # start time of function

    lowest = 0 # start of list
    highest = len(input_list)-1 # end of list

    while lowest <= highest:
        middle = (lowest + highest) // 2 # calculates the middle value
        if input_list[middle] == target: # checks if the target is found
            item_index = middle
        elif target > input_list[middle]: # checks whether the target is higher
            lowest = middle + 1
        elif target < input_list[middle]: # or lower than the middle
            highest = middle - 1
        else: # if the target isn't found, return -1
            item_index = -1
    end = time.time() # end time of function
    time_taken = end-start # calculates time taken
    return item_index, time_taken # returns both the target index, and time taken

binary_found_index, binary_time_taken = binary_search(sorted_list, 1_000_000)
print(f"(Binary Search) Index of item: {binary_found_index}\nTime taken: {binary_time_taken}")

import random # does this really need explanation?

unsorted_list = sorted_list # just so we don't shuffle the sorted list directly
random.shuffle(unsorted_list) # shuffles the sorted list to use for Linear Search

linear_found_index, linear_time_taken = linear_search(unsorted_list, 871)
print(f"(Linear Search) Index of item: {linear_found_index}\nTime taken: {linear_time_taken}")