# Fibonacci O(2^n)

def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_master():
    cache = {}
    calculations = 0

    def fib(n):
        nonlocal calculations
        calculations += 1
        if n in cache:
            return cache[n]
        if n < 2:
            return n
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]
    return fib, lambda: calculations


def fibonacci_master2(n):
    if n < 2:
        return n
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[-1]


faster_fib, get_calculations = fibonacci_master()

print("Slow:", fibonacci(35))          # very slow for large n
print("DP (memoized):", faster_fib(100))
print("DP2 (iterative):", fibonacci_master2(100))
print("We did", get_calculations(), "calculations")
