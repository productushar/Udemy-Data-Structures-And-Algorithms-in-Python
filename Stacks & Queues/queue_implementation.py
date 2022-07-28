#Queue Implementation
#FIFO: First In First Out

class Queue:

    def __init__(self):
        self.queue = []

    # Checks whether the queue is empty or not
    def is_empty(self):
        return self.queue == []

    # Enqueuing operation
    def enqueue(self,data):
        self.queue.append(data)

    # Dequeuing operation
    def dequeue(self):
      
        if self.size_queue()!=0:
            data = self.queue[0]
            del self.queue[0]
            return data
          
        else:
            return -1

    # Returns the first element in the queue
    def peek(self):
        return self.queue[0]

    # Returns the size of the queue
    def size_queue(self):
        return len(self.queue)

#Testing
if __name__=='__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Size:   ",queue.size_queue())
    print("Peek:   ",queue.peek())
    print("Dequeue:",queue.dequeue())
    print("Size:   ",queue.size_queue())
