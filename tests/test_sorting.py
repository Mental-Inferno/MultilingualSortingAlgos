from SortingAlgorithmPython import SortingPython

SortingPython = SortingPython.SortingPython()

arr = [12,11,13,5,6,7]
print("Given array is", end="\n")
print(arr)
arr = SortingPython.merge(arr)
print("Sorted array is: ", end="\n")
print(arr)