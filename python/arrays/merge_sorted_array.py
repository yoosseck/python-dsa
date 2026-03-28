'''
Merge sorted arrays.

We can assume 2 arrays as a parameter, just array1, array2.
`
# input
array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

# output
result = [0, 3, 4, 4, 6, 30, 31]
`

'''


def merge_sorted_arrays(array1, array2):

    if (not (isinstance(array1, list) and
             isinstance(array2, list))):
        raise Exception('Both the inputs should be of an array')

    result = []

    first_idx = 0
    second_idx = 0

    while first_idx < len(array1) and second_idx < len(array2):
        if array1[first_idx] <= array2[second_idx]:
            result.append(array1[first_idx])
            first_idx += 1
        else:
            result.append(array2[second_idx])
            second_idx += 1

    # Append remaining elements
    result.extend(array1[first_idx:])
    result.extend(array2[second_idx:])

    return result


if __name__ == '__main__':
    result = merge_sorted_arrays(
        [0, 3, 4, 31],
        [4, 6, 30]
    )

    print(result)
