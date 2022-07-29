#Binary Search Trees - Implementation

class Node:
    
    def __init__(self,data,parent = None):
        
        self.data = data
        self.left_node = None
        self.right_node = None
        
        # Important when implementing the remove function
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Removing a node based on given data
    def remove(self,data):
        
        if self.root:
            self.remove_node(data,self.root)
            
        else:
            self.insert_node(data,self.root)

    # Sub implementary function for remove
    def remove_node(self,data,node):
        
        if node is None:
            return

        if data < node.data:
            self.remove_node(data,node.left_node)

        elif data > node.data:
            self.remove_node(data,node.right_node)

        else:
            
            if node.left_node is None and node.right_node is None:
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None

                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

            elif node.left_node is None and node.right_node is not None:
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node

                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = None

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                parent = node.parent

                if parent is not None:
                    
                    if parent.left_node == node:
                        parent.left_node = node.left_node

                    if parent.right_node == node:
                        parent.right_node = node.left_node

                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data,predecessor)

    def get_predecessor(self,node):
        
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    # Insertion operation                    
    def insert(self,data):
        
        #First node in the BST
        if self.root is None:
            self.root = Node(data)
            
        else:
            self.insert_node(data,self.root)

    # Sub implementary function for insert
    def insert_node(self,data,node):
        
        # Comparison for placement
        if(data < node.data):
            
            if node.left_node:
                # When left node exists
                self.insert_node(data,node.left_node)
                
            else:
                # When there is no left child
                node.left_node = Node(data,node)
                
        else:
            
            if node.right_node:
                self.insert_node(data,node.right_node)
                
            else:
                node.right_node = Node(data,node)

    # Returns minimum value from the BST
    def get_min(self):
        
        if self.root:
            return self.get_min_value(self.root)

    # Sub implementary function for get_min
    def get_min_value(self,node):
        
        if node.left_node:
            return self.get_min_value(node.left_node)

        return node.data

    # Returns maximum value from the BST
    def get_max(self):
        
        if self.root:
            return self.get_max_value(self.root)

    # Sub implementary function for get_max
    def get_max_value(self,node):
        
        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data

    # Function to traverse through all nodes present in the BST
    def traverse(self):
        
        if self.root:
            self.traverse_in_order(self.root)

    # Sub implementary function for traverse
    def traverse_in_order(self,node):
        
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)


# Testing
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(11)
    bst.insert(19)
    bst.insert(23)
    bst.insert(2)
    bst.remove(10)
    bst.remove(8)
    bst.remove(5)
    print("-------------")
    print("Traversal:")
    bst.traverse()
    print("-------------")
    print("Max:",bst.get_max())
    print("-------------")
    print("Min:",bst.get_min())
    print("-------------")
