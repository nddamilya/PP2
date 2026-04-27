import pygame
import sys
import random

# Инициализация pygame
pygame.init()

# Цвета
FRAME_COLOR = (0,0,0)
SIZE_BLOCK = 20
DBLUE = (6,10,71)
BLUE = (14,18,92)
PINK = (250,105,250)
SNAKE_COLOR = (255,255,255)

# Количество блоков на поле
COUNT_BLOCK = 20

# Цвет верхней панели
HEADER_COLOR = (10,16,84)

# Отступ верхней панели
HEADER_MARGIN = 70

# Отступ между клетками
MARGIN = 1

# Размер игрового окна
size = [
    SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK,
    SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN
]

print(size)

# Создание окна игры
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Таймер для управления FPS
timer = pygame.time.Clock()

# Шрифт для отображения текста
courier = pygame.font.SysFont('courier', 36)


# Класс блока змейки
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Проверка равенства блоков
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

    # Проверка выхода за границы поля
    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCK and 0 <= self.y < COUNT_BLOCK


# Генерация еды в случайной пустой клетке
def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCK - 1)
    y = random.randint(0, COUNT_BLOCK - 1)
    x = random.choice([1, 2, 3])
    y = random.choice([1, 2, 3])

    empty_block = SnakeBlock(x, y)

    # случайный вес еды
    empty_block.weight = random.choice([1, 2, 3])

    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCK - 1)
        empty_block.y = random.randint(0, COUNT_BLOCK - 1)

    return empty_block

    # Проверяем, чтобы еда не появилась на змейке
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCK - 1)
        empty_block.y = random.randint(0, COUNT_BLOCK - 1)

    return empty_block


# Функция отрисовки одного блока
def draw_block(color, row, column):
    pygame.draw.rect(
        screen,
        color,
        [
            SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
            HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
            SIZE_BLOCK,
            SIZE_BLOCK
        ]
    )


# Начальная змейка
snake_blocks = [
    SnakeBlock(9,8),
    SnakeBlock(9,9),
    SnakeBlock(9,10)
]

# Создание первой еды
food = get_random_empty_block()

# Начальное направление движения
d_row = 0
d_col = 1

# Счёт
total = 0

# Скорость
speed = 1


# Основной игровой цикл
while True:

    # Обработка событий
    for event in pygame.event.get():

        # Выход из игры
        if event.type == pygame.QUIT:
            print('Exit')
            pygame.quit()
            sys.exit()

        # Управление змейкой
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0

            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0

            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1

            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    # Заполнение фона
    screen.fill(FRAME_COLOR)

    # Отрисовка верхней панели
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    # Отображение счёта
    text_total = courier.render(f"Total: {total}", 0, PINK)

    # Отображение скорости
    text_speed = courier.render(f"Speed: {speed}", 0, PINK)

    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

    # Отрисовка игрового поля
    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):

            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = DBLUE

            draw_block(color, row, column)

    # Голова змейки
    head = snake_blocks[-1]

    # Проверка столкновения со стеной
    if not head.is_inside():
        print('Crush')
        pygame.quit()
        sys.exit()

    # Отрисовка еды
    draw_block(PINK, food.x, food.y)

    # Отрисовка змейки
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    # Если змейка съела еду
    if food == head:
        total += food.weight

        # Увеличение скорости каждые 5 очков
        speed = total // 5 + 1

        # Увеличение длины змейки
        snake_blocks.append(food)

        # Генерация новой еды
        food = get_random_empty_block()

    # Создание новой головы
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    # Добавляем новую голову
    snake_blocks.append(new_head)

    # Удаляем хвост
    snake_blocks.pop(0)

    # Обновление экрана
    pygame.display.flip()

    # Контроль скорости игры
    timer.tick(3 + speed)