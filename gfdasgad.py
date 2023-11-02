from PIL import Image, ImageDraw


def maze_to_image(maze, cell_size=10, multiplier=2):
    # Определяем цвета для стен и путей в лабиринте
    wall_color = (0, 0, 0)  # Черный цвет
    path_color = (255, 255, 255)  # Белый цвет

    # Определяем размеры изображения с учетом множителя
    width = len(maze[0]) * cell_size * multiplier
    height = len(maze) * cell_size * multiplier

    # Создаем новое изображение
    image = Image.new("RGB", (width, height), wall_color)

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(image)

    # Заполняем изображение в соответствии с лабиринтом
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 0:
                draw.rectangle(
                    [
                        x * cell_size * multiplier,
                        y * cell_size * multiplier,
                        (x + 1) * cell_size * multiplier,
                        (y + 1) * cell_size * multiplier,
                    ],
                    fill=wall_color,
                )
            else:
                draw.rectangle(
                    [
                        x * cell_size * multiplier,
                        y * cell_size * multiplier,
                        (x + 1) * cell_size * multiplier,
                        (y + 1) * cell_size * multiplier,
                    ],
                    fill=path_color,
                )

    return image


def image_to_maze(image_path, maze_size=(4, 4), wall_color=(0, 0, 0), path_color=(255, 255, 255)):
    image = Image.open(image_path)
    width, height = image.size

    cell_width = width // maze_size[0]
    cell_height = height // maze_size[1]

    maze = []

    for y in range(maze_size[1]):
        row = []
        for x in range(maze_size[0]):
            x_start = x * cell_width
            y_start = y * cell_height
            x_end = (x + 1) * cell_width
            y_end = (y + 1) * cell_height

            cell = image.crop((x_start, y_start, x_end, y_end))

            if cell.getpixel((cell_width // 2, cell_height // 2)) == wall_color:
                row.append(0)  # 0 представляет стену
            else:
                row.append(1)  # 1 представляет путь

        maze.append(row)

    return maze
# Пример лабиринта (0 - стена, 1 - путь)
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

# # Преобразуем лабиринт в изображение с множителем 2
# maze_image = maze_to_image(maze, multiplier=2)
#
# # Сохраняем изображение в файл
# maze_image.save("maze.png")
#
# # Отображаем изображение (для просмотра)
# maze_image.show()
#
# # Пример лабиринта (0 - стена, 1 - путь)
# maze = [
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0],
# ]
#
# # Преобразуем лабиринт в изображение с множителем 2
# maze_image = maze_to_image(maze, multiplier=8)
#
# # Сохраняем изображение в файл
# maze_image.save("maze.png")
#
# # Отображаем изображение (для просмотра)
# maze_image.show()

maze = image_to_maze("maze.png", maze_size=(5, 5))

# Выводим полученный двумерный массив
for row in maze:
    print(row)