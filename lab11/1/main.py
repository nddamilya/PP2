import pygame, sys
from pygame.locals import *
import random, time

# Инициализация pygame
pygame.init()
pygame.mixer.init()

# Настройки FPS
FPS = 60
clock = pygame.time.Clock()

# Цвета
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Игровые переменные
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Шрифты
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)
game_over = font_big.render("Game Over", True, BLACK)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Загрузка фона
background = pygame.image.load("images/street.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# КЛАСС ВРАГА
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        # Появление врага в случайной позиции
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)

    def move(self):
        global SCORE
        global SPEED

        # Движение врага вниз
        self.rect.move_ip(0, SPEED)

        # Если враг вышел за экран — появляется заново
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.respawn()


# КЛАСС ИГРОКА
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        # Движение машины влево
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # Движение машины вправо
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)


# КЛАСС МОНЕТЫ
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Загружаем изображение монеты
        self.image = pygame.image.load("images/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()

        # Случайный вес монеты (1, 2 или 3)
        self.weight = random.choice([1, 2, 3])

        self.respawn()

    def respawn(self):
        # Случайная позиция монеты на дороге
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-300, -50)
        )

    def move(self):
        self.rect.move_ip(0, 2)

        # Удаляем монету, если она вышла за экран
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# Создание объектов
player = Player()
enemy = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

# Таймер появления монет каждые 2 секунды
COIN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_EVENT, 2000)


# Игровой цикл
while True:

    # Обработка событий
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Создание новой монеты
        if event.type == COIN_EVENT:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Отрисовка фона
    screen.blit(background, (0, 0))

    # Отображение счета
    screen.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Coins: {COIN_SCORE}", True, BLACK), (260, 10))

    # Движение и отрисовка объектов
    for obj in all_sprites:
        screen.blit(obj.image, obj.rect)
        obj.move()

    # Столкновение с врагом — конец игры
    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Столкновение с монетами
    hits = pygame.sprite.spritecollide(player, coins, True)

    for coin in hits:
        # Добавляем вес монеты к общему счету
        COIN_SCORE += coin.weight

        # Увеличиваем скорость врага каждые 5 монет
        if COIN_SCORE % 5 == 0:
            SPEED += 1

    pygame.display.update()
    clock.tick(FPS)