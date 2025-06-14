from random import randint


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temporary arrays:
    temp_arr_1 = [0] * (n1)
    temp_arr_2 = [0] * (n2)

    # copy data to the arrays
    for i in range(0, n1):
        temp_arr_1[i] = arr[left + i]

    for j in range(0, n2):
        temp_arr_2[j] = arr[mid + 1 + j]

    # initial indexes for first/second subarrays and the one of merged subarray
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if temp_arr_1[i] <= temp_arr_2[j]:
            arr[k] = temp_arr_1[i]
            i += 1
        else:
            arr[k] = temp_arr_2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = temp_arr_1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = temp_arr_2[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):

    if left < right:
        mid = left + (right - left) // 2

        # sort first and second halves and merge them
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)


arr = []

for i in range(10):
    arr.append(randint(1, 100))

size = len(arr)
print(f"The current array is: {arr}")

mergeSort(arr, 0, size - 1)
print(f"The sorted array is: {arr}")
