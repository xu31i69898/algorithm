import random
import time

def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

def binary_search(S, x):
    left = 0
    right = len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def fibonacci_search(S, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    while fib_m < len(S):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2
    offset = -1
    while fib_m > 1:
        i = min(offset+fib_m_minus_2, len(S)-1)
        if S[i] < x:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i
        elif S[i] > x:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        else:
            return True
    if fib_m_minus_1 and offset < len(S)-1 and S[offset+1] == x:
        return True
    return False

def generate_list(n):
    return [random.randint(0, 1000000) for i in range(n)]

def time_search_algorithms(S, x):
    linear_start = time.time()
    linear_search(S, x)
    linear_end = time.time()
    linear_time = linear_end - linear_start

    binary_start = time.time()
    binary_search(S, x)
    binary_end = time.time()
    binary_time = binary_end - binary_start

    fibonacci_start = time.time()
    fibonacci_search(S, x)
    fibonacci_end = time.time()
    fibonacci_time = fibonacci_end - fibonacci_start

    return linear_time, binary_time, fibonacci_time

def run_experiment():
    for n in range(10, 1010, 10):
        total_linear_time = 0
        total_binary_time = 0
        total_fibonacci_time = 0
        for i in range(5):
            S = generate_list(n)
            x = random.randint(0, 1000000)
            linear_time, binary_time, fibonacci_time = time_search_algorithms(S, x)
            total_linear_time += linear_time
            total_binary_time += binary_time
            total_fibonacci_time += fibonacci_time
        average_linear_time = total_linear_time / 5
        average_binary_time = total_binary_time / 5
        average_fibonacci_time = total_fibonacci_time / 5
        print(f"n = {n}\tLinear search: {average_linear_time:.6f}\tBinary search: {average_binary_time:.6f}\tFibonacci search: {average_fibonacci_time:.6f}")

run_experiment()
