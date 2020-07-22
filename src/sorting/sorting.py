# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a, b, m = 0, 0, 0

    # Your code here
    # while we have not yet reached the end of both arrays
    while a < len(arrA) or b < len(arrB):

        # Compare the first index of both arrays
        if b < len(arrB) and (a >= len(arrA) or arrA[a] >= arrB[b]):

            # insert the smaller of the two values into merged_arr
            merged_arr[m] = arrB[b]
            # increment the index of the array that had the smaller number
            b += 1
            m += 1

        else:
            merged_arr[m] = arrA[a]
            a += 1
            m += 1

        # loop

    # ??? Profit?

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
