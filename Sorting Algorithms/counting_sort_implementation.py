#Counting Sort Implementation

class CountingSort:

    def __init__(self, data):
        self.data = data
        # k = max - min + 1
        self.count_array = [0 for _ in range(max(data) - min(data)+1)]

    def sort(self):

        # Considering all items in data in O(N) running time
        for i in range(len(self.data)):
            self.count_array[self.data[i] - min(self.data)] += 1

        z = 0

        # Considering the counting array in O(k)
        for i in range(min(self.data), max(self.data)+1):

            while self.count_array[i - min(self.data)] > 0:
                self.data[z] = i
                z += 1
                self.count_array[i - min(self.data)] -= 1
            

# Testing
if __name__ == '__main__':

    x = [4,6,-3,0,10,14,22,5]
    counting_sort = CountingSort(x)
    counting_sort.sort()
    print("Sorted Array:",counting_sort.data)
