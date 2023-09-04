def faktorial_iteratif(i):
  hasil = 1
  for i in range(i, 0, -1):
    hasil = hasil * i
    return hasil

import timeit

start = timeit.default_timer()
nilai = 0

for i in range(1,101):
  nilai = nilai + i * 2
  end = timeit.default_timer()
  print(f'waktu yang dibutuhkan untuk faktorial iteratif', end - start)

print('')

def faktorial_rekursif(i):
  if i == 1:
    return 1
  else:
    return i * faktorial_rekursif(i-1)

import timeit

start = timeit.default_timer()
nilai = 0

for i in range(1,101):
  nilai = nilai + i * 2
  end = timeit.default_timer()
  print(f'waktu yang dibutuhkan untuk faktorial rekrusif', end - start)