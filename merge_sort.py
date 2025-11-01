# 22ug3-0604

import time

def merge_sort(arr):
    data = arr.copy()
    steps = [0]  # Using list to allow modification inside nested functions
    start_time = time.time()

    def merge(left, right):
        result = []
        while left and right:
            steps[0] += 1
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    def merge_sort_rec(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = merge_sort_rec(data[:mid])
        right = merge_sort_rec(data[mid:])
        return merge(left, right)

    sorted_data = merge_sort_rec(data)
    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_data, execution_time, steps[0]