# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements

    # Your code here
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):

        # Sort each one and place into the result
        if left[left_index] <= right[right_index]:
            merged_arr[left_index+right_index] = left[left_index]
            left_index += 1
        else:
            merged_arr[left_index + right_index] = right[right_index]
            right_index += 1

    for left_index in range(left_index, len(left)):
        merged_arr[left_index + right_index] = left[left_index]

    for right_index in range(right_index, len(right)):
        merged_arr[left_index + right_index] = right[right_index]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here
