class SortPython():

    def mergeSort(self, arr):
        # variables to divide the array elements
        L, R = 0, 0

        # base case
        if len(arr) <= 1:
            return arr

        # divide the array in half
        half = len(arr)//2

        # divide the array elements and mergesort recursively
        L = self.mergeSort(arr[:half])
        R = self.mergeSort(arr[half:])

        return self.merge(L, R)

    def merge(self, L, R):

        left_index, right_index = 0, 0

        # initialize sorted array
        sorted_arr = []

        # copy data to temporary arrays L[] and R[]
        while left_index < len(L) and right_index < len(R):
            if L[left_index] < R[right_index]:
                sorted_arr.append(L[left_index])
                left_index += 1
            else:
                sorted_arr.append(R[right_index])
                right_index += 1

        # append any element remaining
        while left_index < len(L):
            sorted_arr.append(L[left_index])
            left_index += 1
            right_index += 1
        while right_index < len(R):
            sorted_arr.append(R[right_index])
            left_index += 1
            right_index += 1

        return sorted_arr

    def quickSort(self, arr):

        # initialize sorted array
        sorted_arr = []

        # call recursive function
        sorted_arr = self.quick(arr, 0, len(arr)-1)

        return sorted_arr

    def quick(self, arr, low_index, high_index):

        # if more than one item to be sorted
        if low_index < high_index:

            # call partition function to get partitioning index
            p = self.partition(arr, low_index, high_index)

            # recursively call quick for the left and right of the list
            self.quick(arr, low_index, p-1)
            self.quick(arr, p+1, high_index)

        return arr

    def partition(self, arr, low_index, high_index):

        # gets the mid index
        mid_index = (high_index + low_index) // 2

        # comparisons to choose the median between the low, mid, and high index
        pivot_index = high_index
        if arr[low_index] < arr[mid_index]:
            if arr[mid_index] < arr[high_index]:
                pivot_index = mid_index
        elif arr[low_index] < arr[high_index]:
            pivot_index = low_index

        # gets the pivot value from pivot index
        pivot_value = arr[pivot_index]

        # swap the pivot value into the leftmost position of the list
        arr[pivot_index], arr[low_index] = arr[low_index], arr[pivot_index]

        # set a border equal to the low index
        border = low_index

        # iterate through the list from low to high
        for i in range(low_index, high_index+1):
            # if item is lower than pivot value, swap to left side of the list
            if arr[i] < pivot_value:
                border+=1
                arr[i], arr[border] = arr[border], arr[i]
        arr[low_index], arr[border] = arr[border], arr[low_index]

        return (border)

