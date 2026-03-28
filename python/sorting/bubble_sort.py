numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - 1):
            if array[j] > array[j+1]:
                # Swap the numbers
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


bubbleSort(numbers)
print(numbers)
