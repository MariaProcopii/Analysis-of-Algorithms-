from tabulate import tabulate
import time
import matplotlib.pyplot as plt
import decimal
import math

def calculate_pi_digit_bbp(n):
    pi = 0.0
    for k in range(n):
        pi += (1/pow(16, k)) * ((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6)))
    return int(pi * 16) % 16


def calculate_pi_digit_chudnovsky(n):
    decimal.getcontext().prec = n + 1
    decimal.getcontext().Emax = 9999999999

    C = 426880 * decimal.Decimal(10005).sqrt()
    pi = 0
    k = 0
    while True:
        numerator = decimal.Decimal((-1)**k) * math.factorial(6*k) * (545140134*k + 13591409)
        denominator = math.factorial(3*k) * math.factorial(k)**3 * (640320**(3*k))
        term = C * numerator / denominator
        pi += term

        if abs(term) < decimal.Decimal(1) / 10**(n+1):
            break

        k += 1

    return int(pi) % 16




def calculate_pi_digit_spigot(n):
    digits_per_iteration = 8

    def extract_digit(x, digit):
        return (x // 10**digit) % 10

    pi = ""
    q, r, t, k, n1, n2 = 1, 0, 1, 1, 3, 3

    for _ in range(n // digits_per_iteration + 1):
        if 4*q+r-t < n1*t:
            pi += str(n2)
            if len(pi) == n + 1:
                return int(pi[n])
            nr = 10*(r-n2*t)
            n = 10*(3*q+r) // t - 10*n2
            n2 = (10*(3*q+r) // t) % 10
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*n1
            nn = (q*(7*k+2)+r*n2) // (t*n2)
            q *= k
            t *= n2
            n1 = nn
            n2 = (q+k) // t
            q *= -10
            r = nr
            k += 1

    return int(pi[n % digits_per_iteration])




x = [100, 300, 500, 700, 1000, 1500, 1700, 2000, 2500, 3000, 5000]
y = []

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('execution time (ms)')
    plt.title(name)
    plt.show()
    print(tabulate([['time (s)']+ y], headers=(['nr'] + x), tablefmt='orgtbl'))



def time_sorting_algorithm(sorting_algorithm, n):
    start_time = time.time()
    sorting_algorithm(n)
    end_time = time.time()
    return end_time - start_time

for i in x:
    y.append(time_sorting_algorithm(calculate_pi_digit_spigot, i))

results(x, y, calculate_pi_digit_spigot.__name__)
