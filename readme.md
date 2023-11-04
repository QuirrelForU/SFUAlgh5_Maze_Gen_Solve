# Maze Generator and Solver

A command-line interface (CLI) module for interacting with the Maze class, allowing you to generate mazes, solve them,
import from files/images (png or txt), export to files/images, and create GIFs for maze generation and solving.

## Examples of Usage:

### Example 1:

Generate a random maze with a size of 8x8, find a path from the upper left to the lower right corner, and perform
various outputs.

```
python main.py --size 8,8 --solve_indecies 1,1,15,15 --filename maze_test_1 --console_output --text_output --image_output --gif_output
```

- Generates a random maze.
- Finds a path from the upper left to the lower right corner.
- Prints the maze and solved maze in the console.
- Saves the maze in a text file named `maze_test_1.txt`.
- Saves the maze in an image file named `maze_test_1.png`.
- Creates two GIFs: `maze_test_1_generation.gif` and `maze_test_1_solve.gif`.

### Example 2:

Generate a random maze with a size of 4x4 and attempt to find a path (which is not possible), and perform various
outputs.
```
python main.py --size 4,4 --solve_indecies 1,1,1,1 --filename maze_test_2 --console_output --text_output --image_output --gif_output
```

- Generates a random maze.
- Tries to find a path but fails due to the provided indices.
- Prints only the maze in the console.
- Saves the maze in a text file named `maze_test_2.txt`.
- Saves the maze in an image file named `maze_test_2.png`.
- Creates one GIF: `maze_test_2_generation.gif`.

### Example 3:

Import a maze from an image file (`maze.png`), find a path from the upper left to the lower right corner, and perform
various outputs.
```
python main.py --import_file maze.png --solve_indecies 1,1,13,13 --filename maze_test_3 --console_output --text_output --image_output --gif_output
```
- Requires maze.png data file.
- Imports a maze from the image file.
- Finds a path from the upper left to the lower right corner.
- Prints the maze and solved maze in the console.
- Saves the maze in a text file named `maze_test_3.txt`.
- Saves the maze in an image file named `maze_test_3.png`.
- Creates two GIFs: `maze_test_3_generation.gif` and `maze_test_3_solve.gif`.

### Example 4:

Import a maze from a text file (`maze.txt`), attempt to find a path (which is not possible), and perform various
outputs.
```
python main.py --import_file maze.txt --solve_indecies 41,1,53,13 --filename maze_test_4 --console_output --image_output --gif_output
```
- Requires maze.txt data file.
- Imports a maze from a text file.
- Tries to find a path but fails due to the provided indices.
- Prints only the maze in the console.
- Saves the maze in an image file named `maze_test_4.png`.
- No GIFs are created.

Feel free to use these examples to guide you through the usage of the Maze Generator and Solver CLI module.
