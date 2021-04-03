class SortingPython():

    def merge_sort(self, L, R):

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


    def merge(self, arr):
        # variables to divide the array elements
        L, R = 0, 0

        # base case
        if len(arr) <= 1:
            return arr

        # divide the array in half
        half = len(arr)//2

        # divide the array elements
        L = self.merge(arr[:half])
        R = self.merge(arr[half:])

        return self.merge_sort(L, R)