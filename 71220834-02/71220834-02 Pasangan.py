import timeit
import random

def generate_list(i):
    batas_atas = i * 100
    randomlist = random.sample(range(0, batas_atas), i)
    randomlist.sort()
    return randomlist

def cari_pasangan(data, target):
    for i in range(0, len(data)-1):
        for j in range(i, len(data)):
            if data[i] + data[j] == target:
                print(data[i], '+', data[j], '=', target)
            return True
        return False

start = timeit.default_timer()
nilai = 0
x = []
y = []
for i in range(1,101):
  nilai = nilai + i * 2
  end = timeit.default_timer()
  x.append(i)
  y.append(end - start)
  print(f'waktu yang dibutuhkan mencari pasangan', end - start)

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.xlabel('Jumlah')
plt.ylabel('Waktu')
plt.show()