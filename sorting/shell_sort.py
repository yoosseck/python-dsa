from random import shuffle


def shell_sort(numbers):

    length = len(numbers)
    gap = int(length / 2)

    while gap > 0:

        for i in range(gap, length):
            temp = numbers[i]
            j = i

            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap

            numbers[j] = temp

        gap = int(gap/2)

    return numbers


nums = list(range(8))
nums_copy = nums.copy()
shuffle(nums_copy)
print(f"before: {nums_copy}")
sorted_nums = shell_sort(numbers=nums_copy)
print(f"after: {sorted_nums}")
