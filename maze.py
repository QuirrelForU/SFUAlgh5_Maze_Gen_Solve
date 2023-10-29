import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]

    def generate(self):
        for row in range(self.rows):
            sets = [set([col]) for col in range(self.cols)]
            print(sets)
            for col in range(self.cols - 1):
                if random.choice([True, False]):
                    # Add a wall to the right
                    self.grid[row][col] |= 1  # Set the right wall
                else:
                    # Check if the current cell and the cell on the right are in the same set
                    if sets[col] is not sets[col + 1]:
                        # Merge the sets and remove the wall
                        sets[col] |= sets[col + 1]
                        for i in range(self.cols):
                            if sets[i] is sets[col + 1]:
                                sets[i] = sets[col]

            if row < self.rows - 1:
                for col in range(self.cols):
                    if len(sets[col]) > 1:
                        # Add a wall to the bottom if the set contains more than one cell
                        self.grid[row][col] |= 2  # Set the bottom wall
                        # Remove the bottom wall for a random cell in the same set
                        random_cell = random.choice(list(sets[col]))
                        self.grid[row + 1][random_cell] &= ~2  # Clear the bottom wall

    # def display(self):
    #     for row in self.grid:
    #         for cell in row:
    #             if cell & 1:
    #                 print("+---", end="")
    #             else:
    #                 print("+   ", end="")
    #         print("+")
    #         for cell in row:
    #             if cell & 2:
    #                 print("|   ", end="")
    #             else:
    #                 print("    ", end="")
    #         print("|")

# Example usage:
maze = Maze(5, 5)
maze.generate()
#maze.display()

#print(maze.grid)

'''
maze
0 prohod
1 stena
indecies from 2 to +inf

dlya elem v massive est kletka sprava\sleva\snizu\sverhu



'''