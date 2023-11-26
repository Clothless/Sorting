import numpy as np
import time as t
import math

best = np.load('100thousand.npy')
worst = np.load('100thousandReverse.npy')
avg = np.load('100ThousandRand.npy')

def merge(arr, temp, fr,mid,to):
    i = fr
    k = fr
    j = mid+1

    while i <= mid and j <= to:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i < len(arr) and i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    for i in range(fr,to+1):
        arr[i] = temp[i]

def iterMergeSort(arr):
    low = 0
    high = len(arr) - 1

    temp = arr.copy()

    size  = 1
    while size <= high - low:

        for i in range(low, high, 2*size):
            fr = i
            mid = i + size - 1
            to = min(i + 2*size - 1, high)
            merge(arr, temp, fr,mid,to)
        size *= 2
    return arr


print(iterMergeSort([5, 7, -9, 3, -4, 2, 8]))