def fibo_rekrusif(i):
    if i <= 0:
        return []
    elif i == 1:
        return [0]
    elif i == 2:
        return [0, 1]
    else:
        sequence = fibo_rekrusif(i - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence   

import timeit

start = timeit.default_timer()
nilai = 0

for i in range(1,101):
  nilai = nilai + i * 2
  end = timeit.default_timer()
  print(f'waktu yang dibutuhkan untuk', end - start)

import timeit

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    fib_n = 0

    for i in range(2, n + 1):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n

    return fib_n

for n in range(1, 36):
    start = timeit.default_timer()
    result = fibonacci_iterative(n)
    end = timeit.default_timer()
    print(f"Suku ke-{n} dari deret Fibonacci: {result}Kecepatan : {end-start}")