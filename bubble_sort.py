# 22ug3-0474 

import time

def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    steps = 0
    start_time = time.time()

    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    end_time = time.time()
    execution_time = end_time - start_time
    return data, execution_time, steps