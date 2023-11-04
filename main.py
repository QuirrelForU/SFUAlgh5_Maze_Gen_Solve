"""
CLI module for interaction with Maze class.
maze generation, maze solving, maze import from file|image(png), maze export to file|image,
creating gif of maze generation and gif of maze solving
"""
import argparse
from maze import Maze


def main():
    """
    Main function for working with Maze class in CLI.

    Returns:
    """
    parser = argparse.ArgumentParser(description="Maze Generator and Solver CLI")
    parser.add_argument("--size", type=str, help="Maze size in the format 'rows,cols'")
    parser.add_argument("--solve_indecies", type=str,
                        help="Indices for solving in the format 'start_row,start_col,end_row,end_col'")
    parser.add_argument("--import_file", type=str,
                        help="Path to the import file (use .png for images and .txt for text)")
    parser.add_argument("--filename", type=str, help="Name of the output files")
    parser.add_argument("--console_output", action="store_true", help="Output the maze in console")
    parser.add_argument("--text_output", action="store_true", help="Output the maze in textfile")
    parser.add_argument("--image_output", action="store_true", help="Output the maze in image")
    parser.add_argument("--gif_output", action="store_true", help="Output the gif(s) of maze")

    args = parser.parse_args()
    maze = None
    # check size for generation
    if args.size:
        size = args.size.split(",")
        if len(size) != 2:
            print("Error: Provide dimensions in the format 'rows,cols'.")
            return
        rows, cols = map(int, size)
        maze = Maze(rows, cols)
        maze.generate_maze()
    # import maze from file
    if args.import_file:
        maze = Maze()
        if args.import_file.endswith(".png"):
            maze.import_maze_from_image(args.import_file)
        elif args.import_file.endswith(".txt"):
            maze.import_maze_from_file(args.import_file)
        else:
            print("Error: Unsupported import file format. Use .png for images or .txt for text.")
            return
    # if the maze is not created, subsequent functions are useless
    if maze is None:
        print("Error: Provide maze size or import a maze for solving.")
        return

    # check indecies for solving
    solve_indecies = args.solve_indecies.split(",")

    if len(solve_indecies) != 4:
        print("Error: Provide solving coordinates in the format 'start_row,start_col,end_row,end_col'.")
        return
    start, end = list(map(int, solve_indecies[:2])), list(map(int, solve_indecies[2:]))

    maze.solve_maze(start, end)

    if args.console_output:
        maze.print_maze()
        if maze.path:
            maze.print_solved_maze()

    if args.filename:

        if args.text_output:
            maze.export_maze_to_file(args.filename + ".txt")
        if args.image_output:
            maze.create_maze_png(maze.maze).save(args.filename + ".png", "PNG")
        if args.gif_output:
            if maze.generation_states:
                maze.create_gif_maze_gen(args.filename + "_generation.gif")
            if maze.solving_states:
                maze.create_gif_maze_solve(args.filename + "_solving.gif", duration=300)


if __name__ == "__main__":
    main()
