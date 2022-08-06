#Linked Lists - Challenge #2: Reversing a linked list

class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # Inserting a node at the beginning of the linked list 
    def insert_start(self,data):
        self.num_of_nodes+=1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            
        else:
            new_node.next_node = self.head
            self.head = new_node

    # Inserting a node at the end of the linked list 
    def insert_end(self,data):
        self.num_of_nodes+=1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            
        else:
            actual_node = self.head

            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    # Returns the number of nodes in the linked list
    def size_of_list(self):
        return self.num_of_nodes

    # Traversing through the linked list 
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # Removing a node on the basis of given data
    def remove(self,data):
        
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data!=data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
            
        else:
            previous_node.next_node = actual_node.next_node

# Reversing a Singly Linked List (O(N) linear running time complexity)

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


# Testing
if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start(20)
    linked_list.insert_start(30)
    linked_list.insert_start(40)
    linked_list.insert_start(50)
    print("---------------------------------------------")
    print("Traversing through Linked List:")
    linked_list.traverse()
    print("---------------------------------------------")
    linked_list.reverse()
    print("Traversing through Linked List post reversal:")
    linked_list.traverse()
    print("---------------------------------------------")
