numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(array):

    for i in range(0, len(array) - 1):
        min = i
        temp = array[i]

        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j

        array[i] = array[min]
        array[min] = temp

    return array


print(selection_sort(numbers))
