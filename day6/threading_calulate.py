import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext
import math


def calculate_e(k_start, k_end, que=None):
    getcontext().prec = 100
    time.perf_counter()

    partial_sum = 0
    for i in range(k_start, k_end):
        partial_sum += (Decimal(1) / Decimal(math.factorial(i)))

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum


qres = Queue()

N = 100
threads_count = 4

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")

start_time = time.time()

thread_list = []
for i in range(threads_count):
    t = threading.Thread(target=calculate_e, args=(N * i + 1, N * (i + 1), qres))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

e_approx = 0
while not qres.empty():
    e_approx += qres.get()

e_approx += Decimal(1)

print(f"e approximation: {e_approx}")