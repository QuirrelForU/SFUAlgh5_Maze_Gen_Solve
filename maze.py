import copy
import random


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.rows_fixed = rows * 2 + 1
        self.cols_fixed = cols * 2 + 1
        self.index = 2
        self.maze = None
        self.path = None

    def generate_maze(self):
        # empty maze
        self.maze = [[0] * self.cols_fixed for _ in range(self.rows_fixed)]

        # borders
        self.maze = [
            [1 if i in (0, self.rows_fixed - 1) or j in (0, self.cols_fixed - 1) else 0 for j in range(self.cols_fixed)]
            for i in range(self.rows_fixed)]
        # first row indecies
        for j in range(1, self.cols_fixed, 2):
            self.maze[1][j] = self.index
            self.index += 1

        for i in range(1, self.rows_fixed, 2):

            # right walls
            for j in range(1, self.cols_fixed - 2, 2):
                if random.choice([True, False]):
                    self.maze[i][j + 1] = 1
                else:
                    if self.maze[i][j] == self.maze[i][j + 2]:
                        self.maze[i][j + 1] = 1
                    else:
                        temp = copy.copy(self.maze[i][j + 2])

                        for k in range(1, self.cols_fixed, 2):
                            if self.maze[i][k] == temp:
                                self.maze[i][k] = self.maze[i][j]
            # bottom walls
            for j1 in range(1, self.cols_fixed, 2):
                if i != self.rows_fixed - 2:
                    self.maze[i + 2][j1] = self.maze[i][j1]
                    if random.choice([True, False]):
                        # place wall under the cell if exist an exit with the same index
                        count = 0
                        temp = copy.copy(self.maze[i][j1])
                        for z in range(1, self.cols_fixed, 2):
                            if self.maze[i][z] == temp and self.maze[i + 1][z] == 0:
                                count += 1
                        if count > 1:
                            self.maze[i + 1][j1] = 1
                            self.maze[i + 2][j1] = self.index
                            self.index += 1
        # last line
        for i in range(1, self.cols_fixed - 2, 2):
            if self.maze[self.rows_fixed - 2][i] != self.maze[self.rows_fixed - 2][i + 2]:
                self.maze[self.rows_fixed - 2][i + 1] = 0
                temp = copy.copy(self.maze[self.rows_fixed - 2][i + 2])
                for z in range(i + 2, self.cols_fixed - 2, 2):
                    if self.maze[self.rows_fixed - 2][z] == temp:
                        self.maze[self.rows_fixed - 2][z] == self.maze[self.rows_fixed - 2][i]
        # delete trash
        for i in range(1, self.rows_fixed, 2):
            for j in range(1, self.cols_fixed, 2):
                self.maze[i][j] = 0

    def print_maze(self):
        for i in range(self.cols):
            print('___', end='')
        print()
        for i in range(1, self.rows_fixed, 2):
            print('|', end='')
            for j in range(1, self.cols_fixed, 2):
                if self.maze[i][j + 1] == 1 and self.maze[i + 1][j]:
                    print('__|', end='')
                elif self.maze[i][j + 1] == 1:
                    print('  |', end='')
                elif self.maze[i + 1][j] == 1:
                    print('___', end='')
                elif i == self.rows_fixed - 2 and self.maze[i][j + 1] == 0:
                    print('___', end='')
                else:
                    print('   ', end='')
            print()

    def print_solved_maze(self):
        for i in range(self.cols):
            print('___', end='')
        print()
        for i in range(1, self.rows_fixed, 2):
            print('|', end='')
            for j in range(1, self.cols_fixed, 2):
                if self.maze[i][j + 1] == 1 and self.maze[i + 1][j] and [i, j] in self.path:
                    print('_~|', end='')
                elif self.maze[i][j + 1] == 1 and [i, j] in self.path:
                    print(' ~|', end='')
                elif self.maze[i + 1][j] == 1 and [i, j] in self.path:
                    print('_~_', end='')
                elif i == self.rows_fixed - 2 and self.maze[i][j + 1] == 0 and [i, j] in self.path:
                    print('_~_', end='')
                elif self.maze[i][j + 1] == 1 and self.maze[i + 1][j]:
                    print('__|', end='')
                elif self.maze[i][j + 1] == 1:
                    print('  |', end='')
                elif self.maze[i + 1][j] == 1:
                    print('___', end='')
                elif i == self.rows_fixed - 2 and self.maze[i][j + 1] == 0:
                    print('___', end='')
                elif [i, j] in self.path:
                    print(' ~ ', end='')
                else:
                    print('   ', end='')
            print()

    def shortest_distance(self, start_pos, end_pos):
        return (abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])) // 2

    def find_element_in_matrix(self, matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return [i, j]
        return None

    def solve_maze(self, start, end):

        def a_way_out(maze, start_pos, end_pos):
            maze[start_pos[0]][start_pos[1]][1] = 1
            ways = []

            def try_move(direction, distance):
                new_pos_wall = (start_pos[0] + direction[0], start_pos[1] + direction[1])
                new_pos = (start_pos[0] + direction[0] * distance, start_pos[1] + direction[1] * distance)
                if maze[new_pos_wall[0]][new_pos_wall[1]] != 1 and maze[new_pos[0]][new_pos[1]][1] != 1:
                    maze[new_pos[0]][new_pos[1]] = [self.shortest_distance(new_pos, end_pos), 0,
                                                    maze[start_pos[0]][start_pos[1]][2] + [
                                                        [new_pos[0], new_pos[1]]]]
                    ways.append(maze[new_pos[0]][new_pos[1]])

            try_move((0, 1), 2)
            try_move((-1, 0), 2)
            try_move((1, 0), 2)
            try_move((0, -1), 2)
            shortest_ways = list(filter(lambda x: not x[1], ways))
            shortest_ways.sort(key=lambda x: x[0])
            if any(sublist[:2] == [0, 0] for sublist in shortest_ways):
                return
            elif shortest_ways:
                new_start = self.find_element_in_matrix(maze, shortest_ways[0])
                a_way_out(maze, new_start, end_pos)
            else:
                new_start = [1, 1]
                for i in range(1, self.rows_fixed, 2):
                    for j in range(1, self.cols_fixed, 2):
                        if maze[i][j][0] != 0 and maze[i][j][1] != 1:
                            if maze[i][j][0] < maze[new_start[0]][new_start[1]][0]:
                                new_start = [i, j]
                a_way_out(maze, new_start, end_pos)

        solving_maze = copy.deepcopy(self.maze)
        for i in range(1, self.rows_fixed, 2):
            for j in range(1, self.cols_fixed, 2):
                solving_maze[i][j] = [0, 0, 0]

        solving_maze[start[0]][start[1]] = [self.shortest_distance(start, end), 0, [list(start)]]
        a_way_out(solving_maze, start, end)
        self.path = solving_maze[end[0]][end[1]][2]


# Example usage:
rows = 7
cols = 7
maze = Maze(rows, cols)
maze.generate_maze()
print('\nGenerated Maze:')
maze.print_maze()
start = (1, 1)
end = (13, 13)
print('\nSolved Maze:')
maze.solve_maze(start, end)
maze.print_solved_maze()
