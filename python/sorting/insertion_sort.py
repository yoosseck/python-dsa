numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # shift elements that are greater than key to the right
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # insert key in its correct place
        array[j + 1] = key

    return array


# # Example usage
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# print(insertion_sort(numbers))


# def insertion_sort(array):
#     length = len(array)

#     for i in range(1, length):
#         current = array[i]

#         # Case 1: Move to first position if smaller than the first element
#         if current < array[0]:
#             array.pop(i)              # remove at i
#             array.insert(0, current)  # insert at front
#         else:
#             # Case 2: Find the right spot
#             for j in range(1, i):
#                 if array[i] < array[j]:
#                     array.pop(i)             # remove at i
#                     array.insert(j, current) # insert at position j
#                     break

#     return array


# # Example usage
# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# print(insertion_sort(numbers))
