import matplotlib.pyplot as plt
from tabulate import tabulate
import random
import time

x= [500, 1000, 3000, 5000, 10000, 15000, 30000, 50000, 70000, 100000]
y = []

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))


def algorithm1(n):
    c = [True] * (n + 1)  # Initialize all numbers from 2 to n as prime

    c[0] = False  # 0 and 1 are not primes
    c[1] = False

    i = 2
    while (i <= n):
        if c[i] == True:
            j = 2 * i  # Start with 2*i instead of i^2
            while (j <= n):
                c[j] = False
                j += i
        i += 1

    # Create a list of prime numbers
    primes = []
    for i in range(2, n + 1):
        if c[i] == True:
            primes.append(i)

    return primes


def algorithm2(n):
    c = [True] * (n + 1)  # Initialize all numbers from 2 to n as prime

    c[0] = False  # 0 and 1 are not primes
    c[1] = False

    i = 2
    while (i <= n):  # Check up to n
        j = 2 * i
        while (j <= n):
            c[j] = False
            j += i
        i += 1

    # Create a list of prime numbers
    primes = []
    for i in range(2, n + 1):
        if c[i] == True:
            primes.append(i)

    return primes


def algorithm3(n):
    c = [True] * (n + 1)  # Initialize all numbers from 2 to n as prime

    c[0] = False  # 0 and 1 are not primes
    c[1] = False

    i = 2
    while (i <= n):  # Check up to n
        if c[i] == True:
            j = i + 1
            while (j <= n):
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    # Create a list of prime numbers
    primes = []
    for i in range(2, n + 1):
        if c[i] == True:
            primes.append(i)

    return primes


def algorithm4(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False

    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0:
                c[i] = False
                break
            j += 1
        i += 1

    primes = []
    for i in range(n + 1):
        if c[i]:
            primes.append(i)

    return primes

import math

def algorithm5(n):
    # Create a boolean array of length n+1 and set all values to True
    c = [True] * (n+1)

    # Mark 1 as non-prime
    c[1] = False

    # Iterate over all integers up to n and test for primality
    i = 2
    while i <= n:
        # Test for primality by checking all possible factors up to sqrt(i)
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                c[i] = False
                break
            j += 1
        i += 1

    # Extract the list of prime numbers from the boolean array
    primes = [i for i in range(2, n+1) if c[i]]

    return primes


def time_sorting_algorithm(sorting_algorithm, n):
    start_time = time.time()
    sorting_algorithm(n)
    end_time = time.time()
    algorithm_name = sorting_algorithm.__name__
    # print(f"{algorithm_name} took {end_time - start_time:.6f} seconds to return a list of prime numbers up to {n}")
    return end_time - start_time

for i in x:
    y.append(time_sorting_algorithm(algorithm5, i))

results(x, y, algorithm5.__name__)
