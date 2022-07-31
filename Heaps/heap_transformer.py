# Challenge: Converting a maximum heap to a minimum heap

class HeapTransformer:

    def __init__(self, heap):
        self.heap = heap

    def transform(self):

        for i in range((len(self.heap)-2)//2,-1,-1):
            self.fix_down(i)

    def fix_down(self, index):
        
        left_index = 2*index + 1
        right_index = 2*index + 2

        largest_index = index

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[index]:
            largest_index = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[largest_index]:
            largest_index = right_index

        if index!=largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)
