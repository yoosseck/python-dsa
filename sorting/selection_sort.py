from random import shuffle


def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
    
numbers = [5, 2, 4, 6, 1, 3]
nums_copy = numbers.copy()
shuffle(numbers)
sorted_numbers = selection_sort(arr=nums_copy)
print('unsorted:', numbers)
print('sorted:', sorted_numbers)
