def deterministic_select(arr, k):
    """
    Return the kth smallest element of list arr (1-indexed: k=1 returns smallest).
    Uses the Median of Medians algorithm for worst-case linear time selection.
    
    Parameters:
        arr: List of comparable elements.
        k: 1-indexed position of the element to find (1 <= k <= len(arr)).
        
    Returns:
        The kth smallest element.
    """
    if not 1 <= k <= len(arr):
        raise IndexError("k is out of bounds")
    
    # Base case: if the list is small, sort and return kth element.
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Partition arr into groups of at most 5 elements.
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    # Find the median of each sublist.
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # Recursively compute the pivot: the median of the medians.
    pivot = deterministic_select(medians, (len(medians) + 1) // 2)
    
    # Partition the array into three lists:
    # lows: elements less than pivot,
    # highs: elements greater than pivot,
    # pivots: elements equal to pivot.
    lows, highs, pivots = [], [], []
    for el in arr:
        if el < pivot:
            lows.append(el)
        elif el > pivot:
            highs.append(el)
        else:
            pivots.append(el)
    
    # Determine the position of the kth element.
    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        # kth element is equal to pivot.
        return pivot
    else:
        # Adjust k accordingly for the "highs" list.
        new_k = k - len(lows) - len(pivots)
        return deterministic_select(highs, new_k)

# Example usage:
if __name__ == '__main__':
    data = [7, 10, 4, 4, 3, 20, 15, 10, 3]  # Includes duplicate elements.
    kth = 4
    result = deterministic_select(data, kth)
    print(f"Deterministic: The {kth}th smallest element is {result}")
