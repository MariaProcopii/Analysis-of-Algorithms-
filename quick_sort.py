def quick_sort(arr):
    # If the array has length 0 or 1, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose the first element as the pivot
    pivot = arr[0]

    # Partition the array into two sub-arrays
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort the sub-arrays
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    # Concatenate the sorted sub-arrays with the pivot and return the result
    return left_sorted + [pivot] + right_sorted
