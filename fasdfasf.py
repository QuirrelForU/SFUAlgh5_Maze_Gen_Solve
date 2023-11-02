import copy
import random

'''
добавить ввод | вывод лабиринта в файл
добавить вывод png лабиринта
добавить ввод лабиринта из jpg | png 
написать тесты к классу maze
генерация гифки для решения и построения лабиринта
добавить CLI интерфейс

'''
rows = 7
cols = 7

rows_fixed = rows * 2 + 1
cols_fixed = cols * 2 + 1

index = 2

# empty maze
a = [[0] * cols_fixed for _ in range(rows_fixed)]
# borders = 1
a = [[1 if i in (0, rows_fixed - 1) or j in (0, cols_fixed - 1) else 0 for j in range(cols_fixed)] for i in
     range(rows_fixed)]

# input indecies for 1 rows
for j in range(1, cols_fixed, 2):
    a[1][j] = index
    index += 1

for i in range(1, rows_fixed, 2):
    # right wall
    for j in range(1, cols_fixed - 2, 2):
        if random.choice([True, False]):
            # add wall to the right
            a[i][j + 1] = 1
        else:
            # test if indecies are equal
            if a[i][j] == a[i][j + 2]:
                # if true place wall between them
                a[i][j + 1] = 1
            else:
                # else give them equal indecies
                temp = copy.copy(a[i][j + 2])

                for k in range(1, cols_fixed, 2):
                    if a[i][k] == temp:
                        a[i][k] = a[i][j]
    # print('after right wall')
    # print_matrix(a)
    # bottom wall
    for j1 in range(1, cols_fixed, 2):
        if i != rows_fixed - 2:
            a[i + 2][j1] = a[i][j1]
            if random.choice([True, False]):
                # place wall under the cell if exist an exit with the same index
                count = 0
                temp = copy.copy(a[i][j1])
                for z in range(1, cols_fixed, 2):
                    if a[i][z] == temp and a[i + 1][z] == 0:
                        count += 1
                if count > 1:
                    a[i + 1][j1] = 1
                    a[i + 2][j1] = index
                    index += 1
    # print('after bottom wall')
    # print_matrix(a)
for i in range(1, cols_fixed - 2, 2):
    if a[rows_fixed - 2][i] != a[rows_fixed - 2][i + 2]:
        a[rows_fixed - 2][i + 1] = 0
        temp = copy.copy(a[rows_fixed - 2][i + 2])
        for z in range(i + 2, cols_fixed - 2, 2):
            if a[rows_fixed - 2][z] == temp:
                a[rows_fixed - 2][z] == a[rows_fixed - 2][i]

# delete all trash-numbers
for i in range(1, rows_fixed, 2):
    for j in range(1, cols_fixed, 2):
        a[i][j] = 0


def maze_print(maze, cols_fixed, rows_fixed):
    for i in range(cols):
        print('___', end='')
    print()
    for i in range(1, rows_fixed, 2):
        print('|', end='')
        for j in range(1, cols_fixed, 2):
            if maze[i][j + 1] == 1 and maze[i + 1][j]:
                print('__|', end='')
            elif maze[i][j + 1] == 1:
                print('  |', end='')
            elif maze[i + 1][j] == 1:
                print('___', end='')
            elif i == rows_fixed - 2 and maze[i][j + 1] == 0:
                print('___', end='')
            else:
                print('   ', end='')
        print()


def maze_print_solved(maze, cols_fixed, rows_fixed, path):
    for i in range(cols):
        print('___', end='')
    print()
    for i in range(1, rows_fixed, 2):
        print('|', end='')
        for j in range(1, cols_fixed, 2):
            if maze[i][j + 1] == 1 and maze[i + 1][j] and [i, j] in path:
                print('_~|', end='')
            elif maze[i][j + 1] == 1 and [i, j] in path:
                print(' ~|', end='')
            elif maze[i + 1][j] == 1 and [i, j] in path:
                print('_~_', end='')
            elif i == rows_fixed - 2 and maze[i][j + 1] == 0 and [i, j] in path:
                print('_~_', end='')
            elif maze[i][j + 1] == 1 and maze[i + 1][j]:
                print('__|', end='')
            elif maze[i][j + 1] == 1:
                print('  |', end='')
            elif maze[i + 1][j] == 1:
                print('___', end='')
            elif i == rows_fixed - 2 and maze[i][j + 1] == 0:
                print('___', end='')
            elif [i, j] in path:
                print(' ~ ', end='')
            else:
                print('   ', end='')
        print()


def shortest_distance(start_pos, end_pos):
    return (abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])) // 2


def find_element_in_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return [i, j]
    return None  # Если элемент не найден, вернуть None


def a_way_out(maze, start_pos, end_pos):
    maze[start_pos[0]][start_pos[1]][1] = 1

    def try_move(direction, distance):
        new_pos_wall = (start_pos[0] + direction[0], start_pos[1] + direction[1])
        new_pos = (start_pos[0] + direction[0] * distance, start_pos[1] + direction[1] * distance)
        if maze[new_pos_wall[0]][new_pos_wall[1]] != 1 and maze[new_pos[0]][new_pos[1]][1] != 1:
            maze[new_pos[0]][new_pos[1]] = [shortest_distance(new_pos, end_pos), 0,
                                            maze[start_pos[0]][start_pos[1]][2] + [[new_pos[0], new_pos[1]]]]
            ways.append(maze[new_pos[0]][new_pos[1]])

    ways = []
    # Перемещение вправо
    try_move((0, 1), 2)
    # Перемещение вверх
    try_move((-1, 0), 2)
    # Перемещение вниз
    try_move((1, 0), 2)
    # Перемещение влево
    try_move((0, -1), 2)
    shortest_ways = list(filter(lambda x: not x[1], ways))
    shortest_ways.sort(key=lambda x: x[0])
    if any(sublist[:2] == [0, 0] for sublist in shortest_ways):
        return
    elif shortest_ways:
        new_start = find_element_in_matrix(maze, shortest_ways[0])
        a_way_out(maze, new_start, end_pos)
    else:
        new_start = [1, 1]
        for i in range(1, rows_fixed, 2):
            for j in range(1, cols_fixed, 2):
                if maze[i][j][0] != 0 and maze[i][j][1] != 1:
                    if maze[i][j][0] < maze[new_start[0]][new_start[1]][0]:
                        new_start = [i, j]

        a_way_out(maze, new_start, end_pos)


created_maze = a
print('\ngenerated_maze ')
maze_print(created_maze, cols_fixed, rows_fixed)
print('\n')

# start and end in fixed format rows, cols
start = (1, 1)
end = (13, 13)
print(created_maze)
for row in created_maze:
    print(row)

solving_maze = copy.copy(created_maze)
for i in range(1, rows_fixed, 2):
    for j in range(1, cols_fixed, 2):
        solving_maze[i][j] = [0, 0, 0]


solving_maze[start[0]][start[1]] = [shortest_distance(start, end), 0, [list(start)]]
a_way_out(solving_maze, start, end)
path = solving_maze[13][13][2]
maze_print_solved(created_maze, cols_fixed, rows_fixed, path)
