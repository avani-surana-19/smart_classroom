 # Fundamental Algorithms: Summation, Factorial, GCD, and Fibonacci progression

def compute_summation_and_average(marks_list):
    """Computes total summation and average of student marks."""
    total = 0
    count = 0
    for mark in marks_list:
        total += mark
        count += 1
    average = total / count if count > 0 else 0
    return total, average

def compute_fibonacci_progression(n):
    """Generates nth Fibonacci number for tracking student improvement levels."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def compute_gcd(a, b):
    """Euclidean algorithm to find GCD (can be used for mark scaling factors)."""
    while b:
        a, b = b, a % b
    return a