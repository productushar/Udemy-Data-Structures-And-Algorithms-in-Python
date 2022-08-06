#Travelling-Salesman Problem Implementation

'''
Given a list of cities and the distances between each pair of cities.
What is the shortest possible route that visits each city exactly once and returns to the origin city?
'''

class TravellingSalesmanProblem:

    def __init__(self, graph):
        self.graph = graph
        # Number of vertices in graph
        self.n = len(graph)
        # Status of visiting nodes
        self.visited = [False for _ in range(self.n)]
        self.visited[0] = True
        # Collection of all hamiltonian cycles to get the MIN cycle
        self.hamiltonian_cycles = []
        self.path = [0 for _ in range(self.n)]

    # Whether including the given node is valid 
    def is_valid(self, vertex, actual_position):

        # Checking whether the given vertex has already been visited
        if self.visited[vertex]:
            return False

        # Checking if there is a connection between the vertices
        if self.graph[actual_position][vertex] == 0:
            return False

        return True

    def tsp(self, actual_position, counter, cost):

        if counter == self.n and self.graph[actual_position][0]:
            self.path.append(0)
            print(self.path)
            self.hamiltonian_cycles.append(cost + self.graph[actual_position][0])
            self.path.pop()
            return

        # Considering all nodes in the graph
        for i in range(self.n):
            
            if self.is_valid(i, actual_position):
                self.path[counter] = i
                self.visited[i] = True
                self.tsp(i, counter + 1, cost + self.graph[actual_position][i])

                self.visited[i] = False


# Testing
if __name__ == "__main__":

    g = [[0,1,0,2,0],
         [1,0,1,0,2],
         [0,1,0,3,1],
         [2,0,3,0,1],
         [0,2,1,1,0]]

    tsp = TravellingSalesmanProblem(g)
    tsp.tsp(0, 1, 0)
    print(tsp.hamiltonian_cycles)
