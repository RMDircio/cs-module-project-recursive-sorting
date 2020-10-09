# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # set the middle
    middle_index = (end - start) // 2 + start
    # print(f"{middle_index} = ({end} - {start}) // 2 + {start}")

    # If the index is invalid (below zero) then the target was not found
    if middle_index < 0:
        return -1

    # check if target is the middle index
    elif arr[middle_index] == target:
        return middle_index
    
    # check is middle index is first index
    elif middle_index == start:
        if arr[end] == target:
            return end
        else:
            return -1
    
    # if middle index is less than target
    elif arr[middle_index] < target:
        return binary_search(arr, target, middle_index, end)
    
    # if middle index is greater than target
    elif arr[middle_index] > target:
            return binary_search(arr, target, start, middle_index)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass