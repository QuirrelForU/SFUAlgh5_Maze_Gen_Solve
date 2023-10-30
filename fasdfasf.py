import random

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
                a[i][j + 2] = a[i][j]

    for j1 in range(1, cols_fixed, 2):
        if i != rows_fixed - 2:
            a[i + 2][j1] = a[i][j1]
            if random.choice([True, False]):

                # place wall under the cell if exist an exit with the same index

                first_place = j1
                last_place = len(a[i]) - a[i][::-1].index(a[i][j1]) - 1
                obrubok = a[i + 1][first_place:last_place + 1]
                if obrubok.count(0) > 1:
                    a[i + 1][j1] = 1
                    a[i + 2][j1] = index
                    index += 1
for i in range(1, cols_fixed - 2, 2):
    if a[rows_fixed - 2][i] != a[rows_fixed - 2][i + 2]:
        a[rows_fixed - 2][i + 1] = 0
        a[rows_fixed - 2][i + 2] == a[rows_fixed - 2][i]

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


print('generated_maze')
maze_print(a, cols_fixed, rows_fixed)
# solve maze

created_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print('maze in array')
for row in created_maze:
    print(row)

print('\nstable_maze ')
maze_print(created_maze, cols_fixed, rows_fixed)

# start and end in fixed format
start = (1, 1)
end = (13, 13)



while True:

    pass
