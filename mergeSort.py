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


def mergeSort(arr):
    if len(arr) < 2:
        return
    else:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, arr)
    return arr
