def merge_sort(array):
    # Base case: if array has only 1 element, it's already sorted
    if len(array) == 1:
        return array

    # Split array into left and right halves
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    # Recursively sort both halves and merge them
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Compare elements from left and right and build sorted list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add remaining elements from left (if any)
    result.extend(left[left_index:])
    # Add remaining elements from right (if any)
    result.extend(right[right_index:])

    return result


# Example usage
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
answer = merge_sort(numbers)
print(answer)
