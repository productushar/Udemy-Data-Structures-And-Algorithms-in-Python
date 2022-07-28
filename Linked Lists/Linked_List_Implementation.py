#Linked List Implementation

class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

    #Returns data stored in node
    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        #First node of linkedlist
        #Exclusive access available
        self.head = None
        self.num_of_nodes = 0
        
    #O(1) Running time complexity; Insert new node at head
    def insert_start(self,data):
        self.num_of_nodes+=1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            
        else:
            new_node.next_node = self.head
            self.head = new_node

    #O(N) Running time complexity; Insert new node at the end
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

    #O(1) Running time complexity; Returns number of nodes
    def size_of_list(self):
        return self.num_of_nodes

    #O(N) Running time complexity; Traversing through the entire list
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    #O(N) Running time complexity; Removing a node based on given data
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


#Testing
if __name__=='__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Adam')
    linked_list.insert_end(7.5)
    linked_list.traverse()
    print("---------")
    linked_list.remove("Adam")
    linked_list.traverse()


