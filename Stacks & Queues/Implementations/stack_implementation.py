#Stack Implementation
# LIFO: Last In First Out

class Stack:

    def __init__(self):
        self.stack = []

    #Inserts items into stack
    def push(self,data):
        self.stack.append(data)

    #Removes and returns the last item inserted
    def pop(self):

        if self.stack_size() < 1:
            return -1
        
        data = self.stack[-1]
        del self.stack[-1]
        return data

    #Returns the last item inserted
    def peek(self):
        return self.stack[-1]

    #Check whether the stack is empty or not
    def is_empty(self):
        return self.stack == []

    #Returns stack size
    def stack_size(self):
        return len(self.stack)


#Testing
if __name__=='__main__':
    stack = Stack()
    stack.push(10)
    stack.push(5)
    print("Peek:",stack.peek())
    print("Size:",stack.stack_size())
    print("Pop: ",stack.pop())
    print("Peek:",stack.peek())
    print("Size:",stack.stack_size())
