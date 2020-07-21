# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    #declare middle var
    middle = (start + end) //2

    #declare our base case (if target is middle)
    if target == arr[middle]:
        return arr[middle]

    # if in right subtree

    # if in left subtree


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

