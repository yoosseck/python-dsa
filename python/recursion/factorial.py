# Write two functions that finds the factorial of any number.
# One should use recursive, the other should just use a for loop

def find_factorial_recursive(number):
    if number == 2:
        return 2

    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):

    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


print(find_factorial_recursive(2))
print(find_factorial_recursive(3))
print(find_factorial_recursive(4))
print(find_factorial_recursive(5))
print(find_factorial_recursive(6))
