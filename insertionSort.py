import numpy as np
import time as t
import math

best = np.load('100thousand.npy')
worst = np.load('100thousandReverse.npy')
avg = np.load('100ThousandRand.npy')

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        empty = i
        while (empty > 0 and arr[empty -1] > temp):
            arr[empty] = arr[empty - 1]
            empty -= 1
        arr[empty] = temp
    return arr

startBest = t.time()
print(insertionSort(best))
endBest = t.time()
startAvg = t.time()
print(insertionSort(avg))
endAvg = t.time()
startWorst = t.time()
print(insertionSort(worst))
endWorst = t.time()

print(f'worst case: {round(endWorst-startWorst, 3)}s')
print(f'avg case: {round(endAvg - startAvg, 3)}s')
print(f'best case: {round(endBest - startBest, 3)}s')
