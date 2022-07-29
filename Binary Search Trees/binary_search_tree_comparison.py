#Comparing Binary Search Trees

'''

Challenge:

Write an efficient algorithm thats able to compare two binary search trees.
The method returns true if the trees are identical (same topology with same values in the nodes) otherwise it returns false.

'''

class TreeComparator:
    
    def compare(self,node1,node2):
        
        # Returns a comparison if either node is None
        if not node1 or not node2:
            return node1 == node2

        # Returns False if nodes have different data
        if node1.data is not node2.data:
            return False
          
        # Recursive Implementation
        return self.compare(node1.left_node,node2.left_node) and self.compare(node1.right_node,node2.right_node)
