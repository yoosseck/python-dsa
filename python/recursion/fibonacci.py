# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

#For example: fibonacciRecursive(6) should return 8


def fibonacci_iterative(n):
    arr = [0, 1]

    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])

    return arr[n]


def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(0))
print(fibonacci_recursive(1))
print(fibonacci_recursive(2))
print(fibonacci_recursive(3))
print(fibonacci_recursive(4))
print(fibonacci_recursive(5))
print(fibonacci_recursive(6))
print(fibonacci_recursive(7))
print(fibonacci_recursive(8))
print(fibonacci_recursive(9))
print(fibonacci_recursive(10))
print(fibonacci_recursive(11))
print(fibonacci_recursive(12))
