# Quick Sort Implementation

class QuickSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.quick_sort(0,len(self.data)-1)

    def quick_sort(self, low, high):

        if low >= high:
            return

        pivot_index = self.partition(low, high)
        self.quick_sort(low, pivot_index - 1)
        self.quick_sort(pivot_index + 1, high)

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


# Testing
if __name__ == '__main__':

    x = [1,-4,0,10,5,4,3,100]
    algorithm = QuickSort(x)
    algorithm.sort()
    print("Sorted Array:",x)
