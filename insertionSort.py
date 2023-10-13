def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        empty = i
        while (empty > 0 and arr[empty -1] > temp):
            arr[empty] = arr[empty - 1]
            empty -= 1
        arr[empty] = temp
    return arr

