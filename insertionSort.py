#!/usr/bin/python

## INSERTION SORT

# Input : Array of Integers - arr
# Output : Returns sorted array

def insertionSort(arr, low, high):
    for i in range(1, high + 1):
        store = arr[i]
        j = i - 1
        while j >= 0 and store <= arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = store
    # print(arr)
    return arr
