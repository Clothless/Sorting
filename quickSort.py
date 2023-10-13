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