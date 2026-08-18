def find_max_subarray_sum(arr):

    # for an empty list
    if len(arr) == 0:
        return 0

    max_so_far = arr[0]
    current_max = arr[0]

    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)

    return max_so_far

""" 
    --- Complexity Analysis ---
    
    The basic operation is the set of actions including 
    one addition and two comparisons performed inside the loop
    for each element of the array. These actions takes constant
    amount of time for each iteration.
    
    Calculation:
    
    - Initialization of the max_so_far and current_max variables takes 
    constant time, O(1).
    - The for loop runs from the second element to the last element.
    Since the array has n elements, the loop will execute n−1 times.
    - The operations inside the loop are all constant time, O(1).
    
    Therefore,

    T(n) = O(1) + (n−1)×O(1) = O(1) + O(n−1) = O(n)
    
    since n dominates as n becomes larger and in Big-O notation, we drop
    constant and lower order terms.
    
    """