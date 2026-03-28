# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return None


def first_recurring_character(input: list):

    if len(input) < 2:
        raise Exception(f'The input should be of an list type: {input}')

    key_table: dict = {}

    for item in input:

        if item in key_table:
            return item

        key_table[item] = item

    return None


# Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2
first_repeated_char = first_recurring_character([2, 4, 5, 2, 3, 5, 1, 2, 4])
print(first_repeated_char)
first_repeated_char = first_recurring_character([2, 3, 4, 5])
print(first_repeated_char)
first_repeated_char = first_recurring_character('first recurring character')
print(first_repeated_char)
