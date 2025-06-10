def binary_search(arr, key):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (high + low) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
            
        print(low, mid, high)
            
    return "Not Found"


arr = range(1, 40, 3)
print(arr)

for i in arr:
    print(i)
key = 31

result = binary_search(arr, key)
print(result)