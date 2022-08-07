#Challenge 2: Queue with Stack problem solution

'''
The problem is that we want to implement the queue abstract data type and its enqueue() and dequeue() operations with stacks
> Only 2 stacks can be used (one for each functionality)
'''

class Queue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):

        if(len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0):
            raise Exception("Stacks are empty...")

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
