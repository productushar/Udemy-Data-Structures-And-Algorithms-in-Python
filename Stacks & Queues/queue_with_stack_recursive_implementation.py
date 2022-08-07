#Challenge 3: Queue with Stack problem solution with recursion

'''
The problem is that we want to implement the queue abstract data type and its enqueue() and dequeue() operations with stacks using recursion
> Only 2 stacks can be used (one for each functionality)
'''

class Queue:

    def __init__(self):
        self.stack = []

    def enqueue(self,data):
        self.stack.append(data)

    def dequeue(self):

        if(len(self.stack)==1):
            return self.stack.pop()

        item = self.stack.pop()
        dequeued_item = self.dequeue()
        self.stack.append(item)

        return dequeued_item
        
        if(len(self.dequeue_stack)==0):

            while(len(self.enqueue_stack)!=0):
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()


# Testing
if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    print(queue.dequeue())
    print(queue.dequeue())    
    print(queue.dequeue())
