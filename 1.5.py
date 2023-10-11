def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_zeros(n):
    if n < 5:
        return 0
    else:
        return n // 5 + factorial_zeros(n // 5)