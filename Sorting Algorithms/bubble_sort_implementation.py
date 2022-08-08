# Bubble Sort Implementation

import random

class BubbleSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):

        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j,j+1)
        
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


# Testing
if __name__ == '__main__':

    algorithm = BubbleSort([1,-5,0,2,-1,10,9,100,56,-34])
    algorithm.sort()
    print("Sorted array:",algorithm.nums)
