"""Module for testing the Maze class """
import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    """
    Testing Maze class methods for generating and solving maze
    """
    def test_external_elements_are_walls(self):
        """ Checks if all border elements are equal to 1 (wall number)"""
        maze = Maze(7, 7)
        maze.generate_maze()

        for i in range(maze.rows_fixed):
            for j in range(maze.cols_fixed):
                if i == 0 or i == maze.rows_fixed - 1 or j == 0 or j == maze.cols_fixed - 1:
                    self.assertEqual(maze.maze[i][j], 1)

    def test_generated_maze_size(self):
        """ Checks that the two-dimensional list implementing the maze has the required
        size (each cell has walls around it) """
        rows = 7
        cols = 7
        maze = Maze(rows, cols)
        maze.generate_maze()

        self.assertEqual(len(maze.maze), rows * 2 + 1)
        self.assertEqual(len(maze.maze[0]), cols * 2 + 1)

    def test_solve_maze(self):
        """Tests the solve function for static square maze"""
        maze = Maze(7, 7)
        test_maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        maze.maze = test_maze
        start = (1, 1)
        end = (13, 13)

        maze.solve_maze(start, end)

        expected_solution = [
            [1, 1], [1, 3], [3, 3], [5, 3], [7, 3], [9, 3], [9, 5],
            [11, 5], [13, 5], [13, 7], [13, 9], [13, 11], [13, 13]
        ]

        self.assertEqual(maze.path, expected_solution)

    def test_non_square_external_elements_are_walls(self):
        """ Checks if all border elements are equal to 1 (wall number)"""
        maze = Maze(3, 5)
        maze.generate_maze()

        for i in range(maze.rows_fixed):
            for j in range(maze.cols_fixed):
                if i == 0 or i == maze.rows_fixed - 1 or j == 0 or j == maze.cols_fixed - 1:
                    self.assertEqual(maze.maze[i][j], 1)

    def test_non_square_generated_maze_size(self):
        """ Checks that the two-dimensional list implementing the maze has the required
                size (each cell has walls around it) """
        rows = 5
        cols = 3
        maze = Maze(rows, cols)
        maze.generate_maze()

        self.assertEqual(len(maze.maze), rows * 2 + 1)
        self.assertEqual(len(maze.maze[0]), cols * 2 + 1)

    def test_non_square_solve_maze(self):
        """Tests the solve function for static non-square maze"""
        maze = Maze(7, 4)
        test_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 0, 0, 1],
                     [1, 0, 1, 1, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1]]

        maze.maze = test_maze
        start = (1, 1)
        end = (13, 7)

        maze.solve_maze(start, end)

        expected_solution = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1],
                             [11, 1], [13, 1], [13, 3], [13, 5], [13, 7]]

        self.assertEqual(maze.path, expected_solution)


if __name__ == '__main__':
    unittest.main()
