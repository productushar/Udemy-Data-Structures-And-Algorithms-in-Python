#Selection Sort w/ Recursion - Implementation

class SelectionSort:

    def __init__(self, nums):
        self.nums = nums

    def find_min(self, a, i, j):

        if i == j:
            return i

        z = self.find_min(a, i + 1, j)
        return i if a[i] < a[z] else z

    def sort(self):
        self.selection_sort(self.nums)

    def selection_sort(self, nums, actual_index = 0):

        if actual_index == len(nums):
            return

        min_index = self.find_min(nums, actual_index, len(nums) - 1)

        if min_index != actual_index:
            nums[min_index], nums[actual_index] = nums[actual_index], nums[min_index]

        self.selection_sort(nums, actual_index + 1)
        

# Testing  
if __name__ == '__main__':
    n = [1,-5,0,2,-1,10,9,100,56,-34]
    sort = SelectionSort(n)
    sort.sort()
    print(sort.nums)
