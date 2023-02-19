import matplotlib.pyplot as plt
from tabulate import tabulate
import random
import time

x= [200, 400, 600, 800, 1000, 1200, 1300, 1500, 2000, 2500]
y = []

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

def time_sorting_algorithm(sorting_algorithm, size, A):
    start_time = time.time()
    sorting_algorithm(A)
    end_time = time.time()
    algorithm_name = sorting_algorithm.__name__
    # print(f"{algorithm_name} took {end_time - start_time:.6f} seconds to sort {size} elements.")
    return end_time - start_time

for i in x:
    A = generate_random_array(i, 1, 1000)
    y.append(time_sorting_algorithm(bubble_sort, i, A))

results(x, y, bubble_sort.__name__)
