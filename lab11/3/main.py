import pygame

# Инициализация pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint SIMPLE")

# Таймер для FPS
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Холст для рисования
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BLACK)

# Палитра цветов
palette = [
    (240,144,245),     # pink
    (245,240,144),     # yellow
    (118,188,254),     # blue
    (167,247,153),   # green
    (180,139,224),   # purple
    (255, 255, 255)  # белый
]

# Цвет по умолчанию
color = (240,144,245)

# Инструмент по умолчанию
tool = 'brush'

# Размер кисти
radius = 10

# Флаг рисования
drawing = False

# Начальная позиция фигуры
start_pos = (0, 0)

# Шрифт для текста
font = pygame.font.SysFont(None, 24)


# Основной игровой цикл
while True:

    # Обработка событий
    for event in pygame.event.get():

        # Закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Выбор инструмента с клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = 'brush'      # кисть
            elif event.key == pygame.K_2:
                tool = 'rect'       # прямоугольник
            elif event.key == pygame.K_3:
                tool = 'circle'     # круг
            elif event.key == pygame.K_4:
                tool = 'eraser'     # ластик
            elif event.key == pygame.K_5:
                tool = 'square'     # ластик
            elif event.key == pygame.K_6:
                tool = 'right triangle'     # ласти
            elif event.key == pygame.K_7:
                tool = 'equilateral triangle'     # ластик
            elif event.key == pygame.K_8:
                tool = 'rhombus'     # ластик
            

        # Нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Выбор цвета из палитры
            for i, c in enumerate(palette):
                if 10 + i * 50 <= x <= 50 + i * 50 and 10 <= y <= 50:
                    color = c

            # Левая кнопка мыши
            if event.button == 1:
                drawing = True
                start_pos = event.pos

            # Правая кнопка уменьшает размер кисти
            elif event.button == 3:
                radius = max(1, radius - 2)

        # Отпускание кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # Рисование прямоугольника
                if tool == 'rect':
                    pygame.draw.rect(
                        canvas,
                        color,
                        (
                            min(start_pos[0], end_pos[0]),
                            min(start_pos[1], end_pos[1]),
                            abs(start_pos[0] - end_pos[0]),
                            abs(start_pos[1] - end_pos[1])
                        ),
                        2
                    )

                # Рисование круга
                elif tool == 'circle':
                    r = int(
                        (
                            (start_pos[0] - end_pos[0]) ** 2 +
                            (start_pos[1] - end_pos[1]) ** 2
                        ) ** 0.5
                    )
                    pygame.draw.circle(canvas, color, start_pos, r, 2)

                # Рисование квадрата
                elif tool == "square":
                    pygame.draw.rect(canvas, color, (x, y, 100, 100), 2)

                # Рисование прямоугольный треугольника
                elif tool == "equilateral triangle":
                    points = [
                        (start_pos[0], start_pos[1]),
                        (end_pos[0], end_pos[1]),
                        (start_pos[0], end_pos[1])
                    ]

                    pygame.draw.polygon(canvas, color, points, 2)

                # Рисование Равносторонний треугольника
                elif tool == "right triangle":
                    side = abs(end_pos[0] - start_pos[0])

                    points = [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] - side//2, start_pos[1] + side),
                        (start_pos[0] + side//2, start_pos[1] + side)
                    ]

                    pygame.draw.polygon(canvas, color, points, 2)
                
                # Рисование ромба
                elif tool == "rhombus":

                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2

                    points = [
                        (center_x, start_pos[1]),
                        (end_pos[0], center_y),
                        (center_x, end_pos[1]),
                        (start_pos[0], center_y)
                    ]

                    pygame.draw.polygon(canvas, color, points, 2)

        # Движение мыши
        if event.type == pygame.MOUSEMOTION:
            if drawing:

                # Рисование кистью
                if tool == 'brush':
                    pygame.draw.circle(canvas, color, event.pos, radius)

                # Работа ластика
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, BLACK, event.pos, radius)

    # Очистка экрана
    screen.fill(BLACK)

    # Отображение холста
    screen.blit(canvas, (0, 0))

    # Отрисовка палитры цветов
    for i, c in enumerate(palette):
        pygame.draw.rect(screen, c, (10 + i * 50, 10, 40, 40))

    # Отображение текущего инструмента
    text = font.render(f"Tool: {tool}", True, WHITE)
    screen.blit(text, (10, 60))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)