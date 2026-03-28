# 1) Simple function (no cache)
def add_to_80(n):
    return n + 80


print(add_to_80(5))  # 85

# 2) Memoized with a global cache
cache = {}


def memoize_add_to_80(n):
    if n in cache:
        return cache[n]
    else:
        print("long time")
        answer = n + 80
        cache[n] = answer
        return answer


print(1, memoize_add_to_80(6))  # triggers "long time"
print(2, memoize_add_to_80(6))  # returns cached result

# 3) Memoized with a closure (no global scope)
# This mimics the JavaScript closure behavior:


def memoize_add_to_80():
    cache = {}

    def inner(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            answer = n + 80
            cache[n] = answer
            return answer
    return inner


memoized = memoize_add_to_80()
print(1, memoized(6))  # triggers "long time"
print(2, memoized(6))  # cached, no "long time"
