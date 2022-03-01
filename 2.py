def f(n):
    if n <= 15:
        return n * n + 11
    elif n % 2 == 0:
        return f(n // 2) + n * n * n - 5 * n
    else:
        return f(n - 1) + 2 * n + 3
print(f(40))