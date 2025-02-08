import random

def randomized_select(arr, k):
    """
    Return the kth smallest element of list arr (1-indexed: k=1 returns smallest).
    Uses the randomized Quickselect algorithm for expected linear time selection.
    
    Parameters:
        arr: List of comparable elements.
        k: 1-indexed position of the element to find (1 <= k <= len(arr)).
        
    Returns:
        The kth smallest element.
    """
    if not 1 <= k <= len(arr):
        raise IndexError("k is out of bounds")
    
    # Base case: if the list is small, sort and return kth element.
    if len(arr) <= 1:
        return arr[0]
    
    # Randomly choose a pivot.
    pivot = random.choice(arr)
    
    # Partition into three lists.
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        # kth element is pivot (handles duplicates).
        return pivot
    else:
        new_k = k - len(lows) - len(pivots)
        return randomized_select(highs, new_k)

# Example usage:
if __name__ == '__main__':
    data = [7, 10, 4, 3, 20, 15, 10, 3]  # Includes duplicate elements.
    kth = 5
    result = randomized_select(data, kth)
    print(f"Randomized: The {kth}th smallest element is {result}")
