def merge_iterative(arr):    
    n = len(arr)
    width = 1
    
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            
            L = arr[left:mid]
            R = arr[mid:right]
            
            l_idx, r_idx = 0, 0
            
            for k in range(left, right):
                if l_idx < len(L) and (r_idx >= len(R) or L[l_idx] <= R[r_idx]):
                    arr[k] = L[l_idx]
                    l_idx += 1
                else:
                    arr[k] = R[r_idx]
                    r_idx += 1
        
        width *= 2
        
    return arr

arr = [5, 2, 4, 6, 1, 3]

print(f"The current array is: {arr}")

merge_iterative(arr)
print(f"The sorted array is: {arr}")
        
    