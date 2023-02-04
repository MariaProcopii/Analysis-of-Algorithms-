def fibonacci(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        cache[n] = result
        return result
