def quick_sort(arr):
    
    def _helper(low, high):
        if low < high:
            pivot = partition(low, high)
            _helper(low, pivot - 1)
            _helper(pivot + 1, high)      
    
    def partition(low, high):
        pivot = arr[high]
        i = low 
        
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        
        arr[i], arr[high] = arr[high], arr[i]
        
        return i
    
    _helper(0, len(arr)-1)
    
    

# Demo
arr = [5, 2, 4, 6, 1, 3]

print(f'test array: {arr} \b')

quick_sort(arr)
print(f"result: {arr}")
