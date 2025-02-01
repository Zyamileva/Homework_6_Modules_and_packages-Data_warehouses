def factor_custom(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("n must be positive")

    result = 1
    for i in range(1, n + 1, 1):
        result *= i
    return result


def greatest_common_divisor(x, y):
    """Euclidean algorithm.
    Calculate the greatest common divisor of two numbers."""
    if x < 0 or y < 0:
        raise ValueError("Both numbers must be positive")
    while y:
        x, y = y, x % y
    return x
