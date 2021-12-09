# import pygame
import pygame


class NotSpriteError(TypeError):
    """Ошибка, в которой говорится о том, что
    спрайт отсутствует"""


def checking_sprite(self, sprite):
    if sprite:
        self.sprite = sprite
    else:
        raise NotSpriteError


def __doc__():
    """Игровая мини-библиотека или мини-фреймворк,
    созданная из pygame.
    название её: Crazy_ball"""


class Ground:
    def __init__(self):
        sprite = "aaa"
        pos = (0, 0)

    def __str__(self):
        return "G"


class Player:
    def __doc__(self):
        """Сам игрок"""

    def __init__(self, sprite=None, size=(30, 30), speed=10):
        checking_sprite(self, sprite)
        self.size = size
        self.speed = speed
        self.coins = 0

    def move(self):
        """движение игрока"""

    def set_coords(self):
        """Метод для смены координат"""

    def collision_player(self):
        """Столкновение игрока"""

    def checking_clolission(self):
        """Проверка со столкновением"""

    def __str__(self):
        return "P"


class Map:
    """Карта, на которой всё размещается"""

    def __init__(self, length: int, weight: int,
                 ground: 'Ground'):
        self.blocks = list()
        self.enemies = list()
        self.map = [(length + 1) * [ground] for _ in range(weight + 1)]
        self.borders = (length + 1, weight + 1)

    def set_block(self, block: 'Block', pos: tuple):
        block.pos = pos
        self.blocks.append(block)
        if self.borders:
            x, y = pos
            self.map[x][y] = block
        else:
            raise IndexError

    def set_enemy(self, enemy: 'Enemy', pos: tuple):
        enemy.pos = pos
        self.enemies.append(enemy)
        if self.borders:
            x, y = pos
            self.map[x][y] = enemy
        else:
            raise IndexError

    def set_player(self, player: 'Player', pos: tuple):
        player.pos = pos
        if self.borders:
            x, y = pos
            self.map[x][y] = player
        else:
            raise IndexError


class Game:
    """Правила игры"""

    def __init__(self, *args):
        running = "pLaying"

    def kill_player(self):
        """Смерть игрока"""

    def win_player(self):
        """Победа игрока"""

    def collision_player_enemy(self):
        """Столкновение врага"""

    def check_coins(self):
        """
        Проверка количества монет.
        Если все собраны, то игрок выиграл
        """

    def play(self):
        """
            Здесь сама игра,
            которая заключена в цикле
        """
        pygame.init()

        height, width = 700, 550
        screen = pygame.display.set_mode((height, width))
        running = "playing"

        while running == "playing":
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = "stop_play"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Мышка нажата")
                if event.type == pygame.KEYDOWN:
                    print("клавиша нажата")
                    if event.key == pygame.K_w:
                        print("w")
                    if event.key == pygame.K_a:
                        print("a")
                    if event.key == pygame.K_d:
                        print("d")
                    if event.key == pygame.K_s:
                        print("s")

        for enemy in Map.enemies:
            pass

        """player"""

        for block in blocks:
            pass


class Enemy:
    """Враги народа"""

    def __init__(self, sprite=None,
                 size=(20, 20), speed=10):
        checking_sprite(self, sprite)
        self.pos = (0, 0)
        self.speed = speed
        self.size = size

    def collision(self):
        """Столкновение врага со стеной"""

    def __str__(self):
        return "E"


class Block:
    def __init__(self, sprite):
        sprite = checking_sprite(self, sprite)
        pos = (0, 0)

    def __str__(self):
        return "B"
