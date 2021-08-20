def foo(n):
    while n > 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        print(n)
    return n

foo(23)
