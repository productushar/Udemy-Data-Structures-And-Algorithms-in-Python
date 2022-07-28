#Doubly Linked List Implementation

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    #Inserting an item at the end of the linked list
    #Requires manipulation of tail node in O(1) running time
    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #Traversing the list from the head node and onwards
    def traverse_forward(self):
        actual_node = self.head
        
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    #Traversing the list from the tail node and backwards
    def traverse_backward(self):
        actual_node = self.tail
        
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous


#Testing
if __name__ == '__main__':
    linkedList = DoublyLinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.traverse_forward()
    print("-------")
    linkedList.traverse_backward()
