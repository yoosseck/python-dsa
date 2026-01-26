def bubble_sort(numbers):

    count = 0

    for i in range(len(numbers) - 1, 0, -1):

        for j in (range(i)):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

            count += 1

    return {
        "numbers": numbers,
        "count": count
    }


num_list = [3, 8, 2, 4, 6, 1]
print(num_list)
result = bubble_sort(numbers=num_list)
print(result)
