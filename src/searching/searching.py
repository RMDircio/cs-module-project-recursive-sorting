# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # set the middle
    middle_index = (end-start) // 2

    # check if target is the middle index
    if arr[middle_index] == target:
        return True
    
    # check is middle index is 0
    elif arr[middle_index] == 0:
        return False
    
    # if middle index is less than target
    elif arr[middle_index] < target:
        return binary_search(arr, target, middle_index, end)
    
    # if middle index is greater than target
    else:
        if arr[middle_index] > target:
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