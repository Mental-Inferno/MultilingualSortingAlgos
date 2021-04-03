from SortingAlgorithmPython import SortingPython
import numpy as np

sortingObj = SortingPython.SortPython()

# Merge sort test
arr = np.random.randint(1,50,10)
print("Given array is", end="\n")
print(arr)
sorted_arr = sortingObj.mergeSort(arr)
print("Sorted array with merge sort is: ", end="\n")
print(sorted_arr)

# Quick sort test
arr = np.random.randint(1,50,10)
print("Given array is", end="\n")
print(arr)
sorted_arr = sortingObj.quickSort(arr)
print("Sorted array with merge sort is: ", end="\n")
print(sorted_arr)