#Radix Sort Implementation

import random

# Setting a constant number of items
ITEMS_IN_BUCKET = 10

class RadixSort:

    def __init__(self, data):
        self.data = data

    # Returns number of digits from the largest item
    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):

        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):

        count_array = [[] for _ in range(ITEMS_IN_BUCKET)]

        # Storing the count of each element in count_array
        for num in self.data:
            # Calculating the index of the given bucket
            index = (num // (10 ** d)) % 10
            count_array[index].append(num)

        # Considering all items in the count_array
        z = 0
        for i in range(len(count_array)):

            while len(count_array[i]) > 0:
                # O(N) linear running time complexity
                self.data[z] = count_array[i].pop(0)
                z += 1


# Testing
if __name__ == '__main__':

    n = [5,3,10,12,9,8,20,100,325,1023]
    random.shuffle(n)
    print("Shuffled Array:",n)
    radix_sort = RadixSort(n)
    radix_sort.sort()
    print("Sorted Array:",radix_sort.data)
