# Heap - Implementation

# Setting a constant capacity for this implementation's heap
CAPACITY = 10

# Maximum Heap Implementation: Heaps where the root node contains the largest value
class Heap:

    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*CAPACITY

    # Inserting an item into the heap
    def insert(self, item):

        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)

    # Comparing values to make swap operations upto the root node
    def fix_up(self, index):

        parent_index = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # Returns largest item from the heap
    def get_max(self):
        return self.heap[0]

    # Removes and returns the maximum item from the heap (then restructures)
    def poll(self):

        max_item = self.get_max()

        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1

        self.fix_down(0)

        return max_item

    # Comparing items to make swap operations down to the last node so as to adhere to the heap's properties
    def fix_down(self, index):
        
        left_index = 2*index + 1
        right_index = 2*index + 2

        largest_index = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        if index!=largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    # Heap sort
    def heap_sort(self):

        for i in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


# Testing
if __name__ == '__main__':

    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)
    print("----------------------------------------")
    print("Heap:",heap.heap)
    print("----------------------------------------")
    print("Heap sort:")
    heap.heap_sort()
    print("----------------------------------------")
