'''
Challenge: Using Breadth First Search to find way out of a maze

> Problem is to construct an algorithm that can find its way out of an NxN maze
> There may be several obstacles so we can use backtracking or construct the search tree and use depth-first search
'''

from collections import deque

class MazeSolver:

    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1,0,0,-1]
        self.move_y = [0,-1,1,0]
        self.visited = [[False for i in range(len(matrix))] for j in range(len(matrix))]
        self.min_distance = float('inf')

    # Function to test validity of the given maze
    def is_valid(self, row, col):

        if row < 0 or row >= len(self.matrix):
            return False

        if col < 0 or col >= len(self.matrix):
            return False

        if self.matrix[row][col] == 0:
            return False

        if self.visited[row][col]:
            return False

        return True

    # BFS implementation for the maze
    def search(self, i, j, destination_x, destination_y):

        self.visited[i][j] = True
        queue = deque()
        queue.append((i, j, 0))

        while queue:

            (i, j, dist) = queue.popleft()

            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    # This function prints out the shortest path if valid
    def show_result(self):
        
        if self.min_distance != float('inf'):
            print("The shortest path from source to destination:",self.min_distance)

        else:
            print("No feasible solution - The destination cannot be reached!")


# Testing
if __name__ == '__main__':

    # 1 represents the availability of that block to be used as a part of the path while 0 represents otherwise
    m = [
        [1,1,1,1,1],
        [0,1,1,1,1],
        [0,0,0,1,1],
        [1,0,1,1,0],
        [0,0,0,1,1]
        ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0,0,4,4)
    maze_solver.show_result()
