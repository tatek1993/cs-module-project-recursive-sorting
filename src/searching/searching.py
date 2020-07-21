# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # If start is less than end, meaning we haven't checked every index/incremented middle as far as we can
    if start <= end:
        #declare middle var
        middle = (start + end) // 2

        #declare our base case (if target is middle)
        if arr[middle] == target:
            return middle

        # if middle is greater than target / target is in right subtree
        elif arr[middle] > target:
            end = middle - 1
            return binary_search(arr, target, start, end)

        # if middle is less than target / if in left subtree
        elif arr[middle] < target:
            start = middle + 1
            return binary_search(arr, target, start, end)

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
