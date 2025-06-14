from random import shuffle


def selection_sort(nums):
    index_for_min = 0

    for i in range(len(nums) - 1):

        for j in range(i + 1, len(nums), 1):

            if nums[index_for_min] > nums[j]:
                index_for_min = j

        if nums[i] != nums[index_for_min]:
            temp = nums[i]
            nums[i] = nums[index_for_min]
            nums[index_for_min] = temp

    return nums


numbers = list(range(15))
nums_copy = numbers.copy()
shuffle(numbers)
sorted_numbers = selection_sort(nums=nums_copy)
print('unsorted:', numbers)
print('sorted:', sorted_numbers)
