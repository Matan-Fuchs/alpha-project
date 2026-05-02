import numpy as np

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
#
# print(quicksort([3,6,8,10,1,2,1]))

n = int(input())
arr = np.zeros(n, dtype=int)
for i in range(n):
    arr[i] = int(input())
arr = arr / 3
for i in range(n):
    if arr[i] - int(arr[i]) == 0:
        arr[i] = int(arr[i])
print(arr)
