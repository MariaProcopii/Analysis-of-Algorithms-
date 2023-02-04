import math

def fibonacci(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    negative_golden_ratio = (1 - math.sqrt(5)) / 2
    return int((golden_ratio**n - negative_golden_ratio**n) / math.sqrt(5))
