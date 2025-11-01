# 22ug3-0257 

import time

def quick_sort(arr):
    data = arr.copy()
    steps = [0]
    start_time = time.time()

    def quick_sort_rec(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            steps[0] += 1
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    quick_sort_rec(0, len(data) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    return data, execution_time, steps[0]