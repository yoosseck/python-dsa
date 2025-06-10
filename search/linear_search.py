def linear_search(arr, target):
    index = 0
    
    while arr[index] != target:
        index += 1
        
        if index == len(arr):
            print("Element Not Found")
    
    return index    
    
arr = [10, 23, 45, 70, 11, 15]
target = 71

result = linear_search(arr, target)
print(result)
