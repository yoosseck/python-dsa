def quick_select(nums, k):
    
    target_idx = k - 1
    
    def partition(left, right):
        pivot = nums[right]
        fill_ptr = left
        
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill_ptr], nums[i] = nums[i], nums[fill_ptr]
                fill_ptr += 1
            
        nums[fill_ptr], nums[right] = nums[right], nums[fill_ptr]
        return fill_ptr
    
    def select(left, right):
        if left == right:
            return nums[left]
        
        pivot_idx = partition(left, right)
        
        if pivot_idx == target_idx:
            return nums[pivot_idx]
        elif pivot_idx > target_idx:
            return select(left, pivot_idx - 1)
        else:
            return select(pivot_idx + 1, right)
        
    
    return select(0, len(nums) - 1)

arr = [65, 2, 49, 96, 12, 3]

print(f'test array: {arr} \b')

result = quick_select(arr, 6)
print(f"result: {result}")
print(f"arr: {arr}")