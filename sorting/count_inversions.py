from random import randint

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_and_count(arr, temp_arr, 0, len(arr)-1)

def merge_and_count(arr, temp_arr, left, right):
    inv_count = 0
    
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_and_count(arr, temp_arr, left, mid)
        inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
        
    return inv_count
    
def merge(arr, temp_arr, left, mid, right):
    left_idx = left
    right_idx = mid +1
    k = left
    inv_count = 0
    
    while left_idx <= mid and right_idx <= right:
        if arr[left_idx] <= arr[right_idx]:
            temp_arr[k] = arr[left_idx]
            left_idx += 1
        else:
            temp_arr[k] = arr[right_idx]
            inv_count += (mid - left_idx + 1)
            right_idx += 1
        
        k += 1
        
    while left_idx <= mid:
        temp_arr[k] = arr[left_idx]
        left_idx += 1
        k += 1
        
    while right_idx <= right:
        temp_arr[k] = arr[right_idx]
        right_idx += 1
        k += 1
        
    for loop_idx in range(left, right + 1):
        arr[loop_idx] = temp_arr[loop_idx]
        
    return inv_count

arr = [5, 2, 4, 6, 1, 3]

count = count_inversions(arr)
print(f"arr: {arr}, count: {count}")