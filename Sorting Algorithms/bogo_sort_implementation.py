# Bogo Sort Implementation

import random

class BogoSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        while not self.is_sorted():
            print('Shuffle again...')
            self.shuffle()

    # Fisher-Yates Approach
    def shuffle(self):
        for i in range(len(self.nums) - 2, -1, -1):
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        print(self.nums)
        
    def is_sorted(self):
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i+1]:
                return False

        return True


# Testing
if __name__ == '__main__':

    algorithm = BogoSort([1,-4,0,10,2])
    algorithm.sort()
    print("Sorted Array:",algorithm.nums)
