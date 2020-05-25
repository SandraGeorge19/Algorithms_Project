#!/usr/bin/python

## QUICK SORT

# Input : Array of Integers - arr
# Output : Returns sorted array


def selectionSort(arr,low,high) :
	for i in range(len(arr)):
		mini = i
		for j in range(i + 1, len(arr)):
			if arr[mini] > arr[j]:
				mini = j
		arr[i], arr[mini] = arr[mini], arr[i]
	return arr