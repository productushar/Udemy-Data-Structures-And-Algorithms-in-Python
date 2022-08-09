# Quick Sort - Implementation with Iteration 

from collections import deque

class QuickSort:

    def __init__(self, data):
        self.data = data

    # Lomuto's Approach
    def partition(self, low, high):
        pivot_index = (low + high)//2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high):
            
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low = low + 1

        self.data[low], self.data[high] = self.data[high], self.data[low]
        return low

    def sort(self):

        stack = deque()
        stack.append((0, len(self.data)-1))

        while stack:

            start, end = stack.pop()
            pivot = self.partition(start, end)

            if pivot - 1 > start:
                stack.append((start, pivot - 1))

            if pivot + 1 < end:
                stack.append((pivot + 1, end))
                

# Testing
if __name__ == '__main__':

    x = [1,-4,0,10,5,4,3,100]
    algorithm = QuickSort(x)
    algorithm.sort()
    print("Sorted Array:",x)
