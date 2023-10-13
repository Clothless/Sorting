import numpy
import time
import sys
sys.setrecursionlimit(200000)
def partition(arr, start, end):
    pivot = arr[end]
    partIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[partIndex] = arr[partIndex], arr[i]
            partIndex += 1
    arr[partIndex], arr[end] = arr[end], arr[partIndex]
    return partIndex


def quickSort(arr, start, end):
    if start < end:
        partIndex = partition(arr, start, end)
        quickSort(arr, start, partIndex-1)
        quickSort(arr, partIndex+1, end)
    return arr


best = numpy.load('100thousand.npy')
worst = numpy.load('100thousandReverse.npy')
avg = numpy.load('100ThousandRand.npy')

startBest = time.time()
quickSort(best, 0, 99999)
endBest = time.time()
startWorst = time.time()
quickSort(worst, 0, 99999)
endWorst = time.time()
startAvg = time.time()
quickSort(avg, 0, 99999)
endAvg = time.time()

print(f'worst case: {endWorst-startWorst}s')
print(f'avg case: {endAvg - startAvg}s')
print(f'best case: {endBest - startBest}s')