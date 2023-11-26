import numpy as np
import time as t
import math

best = np.load('100thousand.npy')
worst = np.load('100thousandReverse.npy')
avg = np.load('100ThousandRand.npy')

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i +=1
        else:
            arr[k] = right[j]
            j += 1
        k +=1
    while (i < len(left)):
        arr[k] = left[i]
        i +=1
        k+=1
    while (j < len(right)):
        arr[k] = right[j]
        j +=1
        k+=1


def recMergeSort(arr):
    if len(arr) < 2:
        return
    else:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        recMergeSort(left)
        recMergeSort(right)
        merge(left, right, arr)
    return arr

startBest = t.time()
print(recMergeSort(best))
endBest = t.time()
startAvg = t.time()
print(recMergeSort(avg))
endAvg = t.time()
startWorst = t.time()
print(recMergeSort(worst))
endWorst = t.time()

print(f'worst case: {round(endWorst-startWorst, 3)}s')
print(f'avg case: {round(endAvg - startAvg, 3)}s')
print(f'best case: {round(endBest - startBest, 3)}s')
