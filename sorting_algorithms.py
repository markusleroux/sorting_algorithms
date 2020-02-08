from collections import OrderedDict

def quickSort(arr):
    if len(arr) == 0:
        return []

    less, more = [], []

    for v in arr[1:]:
        if v <= arr[0]:
            less.append(v)
        else:
            more.append(v)

    
    return quickSort(less) + [arr[0]] + quickSort(more)


def countingSort(arr):
    count = {}

    for v in arr:
        try:
            count[v] += 1
        except KeyError:
            count[v] = 1

    result = []

    for key, value in {k: count[k] for k in sorted(count)}.items():
        result += value*[key]
    
    return result

def mergeSort(arr):
    if len(arr) > 1:
        left = mergeSort(arr[:len(arr)//2])
        right = mergeSort(arr[len(arr)//2:])

        i = j = k = 0
        m, n = len(left), len(right)

        while (i < m or j < n):
            if i == m:
                arr[k] = right[j]
                j += 1
            elif j == n:
                arr[k] = left[i]
                i += 1
            elif left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1

    return arr

def heapSort(arr):
    pass