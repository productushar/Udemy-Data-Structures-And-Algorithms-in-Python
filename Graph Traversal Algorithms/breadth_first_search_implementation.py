#Breadth First Search Implementation

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):

    queue = [start_node]
    start_node.visited = True
    
    while queue:

        actual_node = queue.pop(0)
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


# Testing
if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node1.adjacency_list.append(node3)
    node1.adjacency_list.append(node4)
    node3.adjacency_list.append(node2)
    breadth_first_search(node1)
