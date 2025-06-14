def insertion_sort(numbers):

    for i in range(0, 6):
        j = i + 1

        while j < len(numbers):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp

            j += 1

    return numbers


result = insertion_sort(numbers=[5, 2, 4, 6, 1, 3])
print(result)

# Output: 1, 2, 3, 4, 5, 6
