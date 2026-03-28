from random import randint


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merge_sort(left_half)
    merge_sort(right_half)
    
    left_idx = right_idx = arr_idx = 0
    
    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            arr[arr_idx] = left_half[left_idx]
            left_idx += 1
        else:
            arr[arr_idx] = right_half[right_idx]
            right_idx += 1
            
        arr_idx += 1
            
    while left_idx < len(left_half):
        arr[arr_idx] = left_half[left_idx]
        left_idx += 1
        arr_idx += 1
        
    while right_idx < len(right_half):
        arr[arr_idx] = right_half[right_idx]
        right_idx += 1
        arr_idx += 1
    
    return arr
    

arr = [5, 2, 4, 6, 1, 3]

size = len(arr)
print(f"The current array is: {arr}")

merge_sort(arr)
print(f"The sorted array is: {arr}")
