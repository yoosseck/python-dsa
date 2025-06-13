import array


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        pivot_index = partition(arr, low, high) 
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
def quick_sort_verbose(arr):
    """
    Wrapper function that shows the sorting process step by step
    """
    print(f"Starting quicksort on: {arr}")
    print("-" * 50)
    
    # Make a copy to avoid modifying original
    arr_copy = arr.copy()
    quick_sort(arr_copy)
    
    print("-" * 50)
    print(f"Final sorted array: {arr_copy}")
    return arr_copy

        
def partition(arr, low, high):
    
    pivot = arr[high]
    
    i = low - 1
    
    for j in range(low, high):
        
        if arr[j] <= pivot:
            i += 1
            
            arr[i], arr[j] = arr[j], arr[i]
            
            print(f"arr[i]: {arr[i]}, arr[j]: {arr[j]}, pivot: {pivot}")
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print("pivot at index:", pivot, i + 1)
    print(arr, ": array state", arr[low:high+1])
    
    return i + 1

# Demo

test_arr = []

for i in range(0, 8):
    from random import randint
    test_arr.append(randint(1, 100))
    
print(f'test array: {test_arr} \b')

result = quick_sort_verbose(test_arr)
print(f"result: {result}")