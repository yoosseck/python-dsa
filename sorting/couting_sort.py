from random import randint


def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    sorted_arr = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        index = num - min_val
        position = count[index] - 1
        sorted_arr[position] = num
        count[index] -= 1

    return sorted_arr


# Demo


test_arr = []

for i in range(8):
    test_arr.append(randint(1, 15))

print(f"test_arr: {test_arr}")
print(counting_sort(test_arr))
