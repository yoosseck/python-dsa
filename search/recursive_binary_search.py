def recursive_binary_search(arr, key, low, high):

    while low <= high:

        mid = (high + low) // 2

        print(f"key: {key}", mid, high, low)

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return recursive_binary_search(arr, key, low, mid - 1)
        elif arr[mid] < key:
            return recursive_binary_search(arr, key, mid + 1, high)

        print(low, mid, high)

    return "Not Found"


arr = range(1, 400, 4)
key = 225

result = recursive_binary_search(arr, key, 0, len(arr) - 1)
print(result)
print(f"Okay, the index that it said was was {result}")
print(f"And then, to confirm the key was: {arr[result]}")
