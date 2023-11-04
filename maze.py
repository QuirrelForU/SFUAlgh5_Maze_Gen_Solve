"""
Module for Maze class implementation.
"""
import copy
import random
from typing import List, Union, Tuple
from PIL import Image, ImageDraw


class Maze:
    """
       A class for generating, solving, and manipulating mazes.

       Args:
           rows (int): The number of rows in the maze.
           cols (int): The number of columns in the maze.

       Attributes:
           rows_fixed (int): The fixed number of rows in the maze (adjusted for walls).
           cols_fixed (int): The fixed number of columns in the maze (adjusted for walls).
           index (int): Current index used during maze generation.
           maze (List[List[int]]): A 2D list representing the maze layout.
           path (List[List[int]]): The path found during maze solving.
           generation_states (List[List[List[int]]]): States of the maze during generation.
           solving_states (List[List[List[int]]]): States of the maze during solving.
       """

    def __init__(self, rows: int = 1, cols: int = 1) -> None:
        """
        Initialize the Maze object with the specified number of rows and columns.

        Args:
            rows (int): The number of rows in the maze.
            cols (int): The number of columns in the maze.

        Returns:
            None
        """
        self.rows_fixed = rows * 2 + 1
        self.cols_fixed = cols * 2 + 1
        self.index = 2
        self.maze = None
        self.path = None
        self.generation_states = []
        self.solving_states = []

    def generate_maze(self) -> None:
        """
        Generate a maze and save generation states in generation_states variable.

        Returns:
            None
        """
        # empty maze
        self.maze = [[0] * self.cols_fixed for _ in range(self.rows_fixed)]

        self.generation_states.append(copy.deepcopy(self.maze))

        # borders
        self.maze = [
            [1 if i in (0, self.rows_fixed - 1) or j in (0, self.cols_fixed - 1) else 0 for j in range(self.cols_fixed)]
            for i in range(self.rows_fixed)]
        self.generation_states.append(copy.deepcopy(self.maze))
        # make support walls
        for i in range(2, maze.rows_fixed, 2):
            for j in range(0, maze.cols_fixed, 2):
                maze.maze[i][j] = 1
        self.generation_states.append(copy.deepcopy(self.maze))
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
            # update states
            self.generation_states.append(copy.deepcopy(self.maze))
        # last line
        for i in range(1, self.cols_fixed - 2, 2):
            if self.maze[self.rows_fixed - 2][i] != self.maze[self.rows_fixed - 2][i + 2]:
                self.maze[self.rows_fixed - 2][i + 1] = 0
                temp = copy.copy(self.maze[self.rows_fixed - 2][i + 2])
                for z in range(i + 2, self.cols_fixed - 2, 2):
                    if self.maze[self.rows_fixed - 2][z] == temp:
                        self.maze[self.rows_fixed - 2][z] == self.maze[self.rows_fixed - 2][i]
        self.generation_states.append(copy.deepcopy(self.maze))
        # delete trash
        for i in range(1, self.rows_fixed, 2):
            for j in range(1, self.cols_fixed, 2):
                self.maze[i][j] = 0
        self.index = 2

    def print_maze(self) -> None:
        """
        Print the maze in console.

        Returns:
            None
        """
        for i in range(self.cols_fixed // 2):
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

    def print_solved_maze(self) -> None:
        """
        Print the solved maze layout in console.

        Returns:
            None
        """
        for i in range(self.cols_fixed // 2):
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

    def shortest_distance(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> int:
        """
        Calculate the shortest distance between two positions in the maze.

        Args:
            start_pos (Tuple[int, int]): The starting position as a (row, column) tuple.
            end_pos (Tuple[int, int]): The ending position as a (row, column) tuple.

        Returns:
            int: The shortest distance between the positions.
        """
        return (abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])) // 2

    def find_element_in_matrix(self, matrix: List[List[int]], target: int) -> Union[List[int], None]:
        """
        Find the target value in a 2D matrix.

        Args:
            matrix (List[List[int]]): The 2D matrix to search.
            target (int): The target value to find.

        Returns:
            Union[List[int], None]: The position of the target value as a (row, column) tuple or None if not found.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return [i, j]
        return None

    def solve_maze(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Solve the maze from a given start position to an end position.

        Args:
            start (Tuple[int, int]): The starting position as a (row, column) tuple.
            end (Tuple[int, int]): The ending position as a (row, column) tuple.

        Returns:
            None
        """

        def a_way_out(maze: List[List[List[int]]], start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
            """
            Recursive function to find a way out in the maze using backtracking.

            Args:
                maze (List[List[List[int]]): A 3D list representing the maze layout with state information.
                start_pos (Tuple[int, int]): The current position as a (row, column) tuple.
                end_pos (Tuple[int, int]): The destination position as a (row, column) tuple.

            Returns:
                None
            """
            maze[start_pos[0]][start_pos[1]][1] = 1
            self.solving_states.append(maze[start_pos[0]][start_pos[1]][2])
            ways = []

            def try_move(direction: Tuple[int, int], distance: int) -> None:
                """
                Attempt to move in a specific direction from the current position and update the maze state.

                Args:
                    maze (List[List[List[int]]): A 3D list representing the maze layout with state information.
                    direction (Tuple[int, int]): The movement direction as a (row, column) tuple.
                    distance (int): The distance to move in that direction.

                Returns:
                    None
                """
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
        self.solving_states.append(solving_maze[start[0]][start[1]][2])
        a_way_out(solving_maze, start, end)
        self.solving_states.append(solving_maze[end[0]][end[1]][2])
        self.solving_states.append(solving_maze[end[0]][end[1]][2])
        self.solving_states.append(solving_maze[end[0]][end[1]][2])
        self.path = solving_maze[end[0]][end[1]][2]

    def import_maze_from_file(self, filename: str) -> None:
        """
        Import a maze from a text file.

        Args:
            filename (str): The name of the text file containing the maze.

        Returns:
            None
        """
        try:
            with open(filename, 'r') as file:
                maze_data = [list(map(int, line.strip())) for line in file.readlines()]

                if len(maze_data) == self.rows_fixed and all(len(row) == self.cols_fixed for row in maze_data):
                    self.maze = maze_data
                else:
                    print("Invalid maze dimensions in the file.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def import_maze_from_image(self, filename: str) -> None:
        """
        Import a maze from an image file.

        Args:
            filename (str): The name of the image file containing the maze.

        Returns:
            None
        """
        wall_color = (0, 0, 0)
        path_color = (255, 255, 255)
        try:
            image = Image.open(filename)
            width, height = image.size

            maze_data = []
            for y in range(0, height, 21):
                row = []
                for x in range(0, width, 21):
                    pixel = image.getpixel((x, y))
                    if pixel == wall_color:
                        row.append(1)
                    elif pixel == path_color:
                        row.append(0)
                    else:
                        raise ValueError("Unknown pixel color in the image")
                maze_data.append(row)
            self.maze = maze_data
            self.rows_fixed = len(maze_data)
            self.cols_fixed = len(maze_data[0])
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def export_maze_to_file(self, filename: str) -> None:
        """
        Export the maze to a text file.

        Args:
            filename (str): The name of the text file to save the maze.

        Returns:
            None
        """
        with open(filename, 'w') as file:
            for row in self.maze:
                file.write(''.join(map(str, row)) + '\n')

    def create_maze_png(self, maze: List[List[int]], solve_path: List[List[int]] = None) -> Image.Image:
        """
        Create an image representation of the maze with optional solution path.

        Args:
            maze (List[List[int]]): The maze layout.
            solve_path (List[List[int]]): The solution path as a list of (row, column) tuples (default: None).

        Returns:
            Image.Image: A PIL image representing the maze.
        """
        cell_size = 20  # Adjust cell size as needed
        wall_color = (0, 0, 0)  # Color for walls
        path_color = (255, 255, 255)  # Color for paths
        find_color = (255, 0, 0)  # Color for searching algorithm

        width = self.cols_fixed * cell_size
        height = self.rows_fixed * cell_size
        img = Image.new('RGB', (width, height), path_color)
        draw = ImageDraw.Draw(img)

        for i in range(self.rows_fixed):
            for j in range(self.cols_fixed):
                if maze[i][j] == 1:
                    draw.rectangle([(j * cell_size, i * cell_size),
                                    ((j + 1) * cell_size, (i + 1) * cell_size)], fill=wall_color)
        if solve_path:
            for position in solve_path:
                draw.rectangle([(position[1] * cell_size, position[0] * cell_size),
                                ((position[1] + 1) * cell_size, (position[0] + 1) * cell_size)], fill=find_color)

        # img.save(filename, 'PNG')
        return img

    def create_gif_maze_gen(self, filename: str, duration: int = 1000, loop: int = 0) -> None:
        """
        Create a GIF animation of the maze generation process.

        Args:
            filename (str): The name of the GIF file to save.
            duration (int): The duration (in milliseconds) of each frame (default: 1000).
            loop (int): Number of times the GIF should loop (0 for infinite loop, default: 0).

        Returns:
            None
        """
        gif = []
        for maze_state in self.generation_states:
            image = self.create_maze_png(maze_state)
            gif.append(image)
        gif.reverse()
        if len(gif) > 0:
            gif.reverse()
            gif[0].save(
                filename,
                save_all=True,
                append_images=gif[1:],
                duration=duration, loop=loop)
        else:
            print('Cannot create gif')

    def create_gif_maze_solve(self, filename: str, duration: int = 1000, loop: int = 0) -> None:
        """
        Create a GIF animation of the maze solving process.

        Args:
            filename (str): The name of the GIF file to save.
            duration (int): The duration (in milliseconds) of each frame (default: 1000).
            loop (int): Number of times the GIF should loop (0 for infinite loop, default: 0).

        Returns:
            None
        """
        gif = []

        for path in self.solving_states:
            image = self.create_maze_png(self.maze, path)
            gif.append(image)
        gif.reverse()
        if len(gif) > 0:
            gif.reverse()
            gif[0].save(
                filename,
                save_all=True,
                append_images=gif[1:],
                duration=duration, loop=loop)
        else:
            print('Cannot create gif')


# Example usage:
maze = Maze(7, 7)
# maze.import_maze_from_image('maze.png')
maze.generate_maze()
# maze.import_maze_from_file('zalupa.txt')
# print('\nGenerated Maze:')
maze.print_maze()
start = (1, 1)
end = (13, 13)
print('\nSolved Maze:')
maze.solve_maze(start, end)
maze.print_solved_maze()
maze.export_maze_to_file('maze.txt')
maze.create_maze_png(maze.maze).save('maze.png', 'PNG')
maze.create_gif_maze_gen('maze.gif')
maze.create_gif_maze_solve('maze_solve.gif', duration=500)
'''
КОМЕНТЫ
CLI
'''
