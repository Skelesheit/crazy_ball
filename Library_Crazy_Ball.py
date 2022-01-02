import pygame


class NotSpriteError(TypeError):
    """Ошибка, в которой говорится о том, что
    спрайт отсутствует"""


def checking_sprite(sprite):
    if sprite:
        return sprite
    else:
        raise NotSpriteError


def __doc__():
    """Игровая мини-библиотека или мини-фреймворк,
    созданная из pygame.
    название её: Crazy_ball"""


class Ground:
    def __init__(self):
        self.sprite = "aaa"
        pos = tuple()

    def __str__(self):
        return "G"


class Player(pygame.sprite):

    def __init__(self, sprite: pygame.sprite, size=(30, 30), speed=10):
        super().__init__()
        self.sprite = checking_sprite(sprite)
        self.rect = self.image.get_rect()
        self.size = size
        self.speed = speed
        self.coins = 0
        self.direction_x = -1
        self.direction_y = -1

    def update(self):
        """движение игрока"""

    def draw(self):
        """Рисование игрока"""

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
                 ground: Ground):
        self.blocks = list()
        self.enemies = list()
        self.coins = list()
        self.map = [(length + 1) * [ground] for _ in range(weight + 1)]
        self.borders = (length + 1, weight + 1)

    def set_block(self, block: Block, pos: tuple):
        block.pos = pos
        self.blocks.append(block)
        if self.borders:
            x, y = pos
            self.map[x][y] = block
        else:
            raise IndexError

    def set_enemy(self, enemy: Enemy, pos: tuple):
        enemy.pos = pos
        self.enemies.append(enemy)
        if self.borders:
            x, y = pos
            self.map[x][y] = enemy
        else:
            raise IndexError

    def set_player(self, player: Player, pos: tuple):
        player.pos = pos
        if self.borders:
            x, y = pos
            self.map[x][y] = player
        else:
            raise IndexError

    def set_coin(self, coin: Coin, pos: tuple):
        coin.set_pos(pos)
        self.coins.append(coin)

    def draw(self):
        """рисование карты и краёв"""


class Enemy(pygame.sprite):
    """Враги народа"""

    def __init__(self, sprite: pygame.sprite,
                 size=(20, 20), speed=10, ):
        self.sprite = sprite
        self.pos = (0, 0)
        self.speed = speed
        self.size = size
        self.direction_x = -1
        self.direction_y = -1

    def collision(self):
        """Столкновение врага со стеной"""

    def draw(self):
        """Рисует врага"""

    def update(self):
        """Движение врага"""

    def __str__(self):
        return "E"


class Block(pygame.sprite):
    def __init__(self, sprite:pygame.sprite):
        self.sprite = pygame.sprite
        pos = (0, 0)

    def __str__(self):
        return "B"

    def draw(self):
        """рисует стену"""


class Coin(pygame.sprite):
    """Монеты"""

    def __init__(self, sprite:pygame.sprite):
        self.sprite = pygame.sprite
        self.pos = tuple()

    def set_coin(self, pos):
        self.pos = pos

    def __str__(self):
        return "C"


class Game:
    """Правила игры и сама игра"""

    def __init__(self):
        self.running = "playing"

    def kill_player(self):
        """Смерть игрока"""

    def win_player(self):
        """Победа игрока"""

    def check_coins(self):
        """
        Проверка количества монет.
        Если все собраны, то игрок выиграл
        """

    def play(self, Map: Map, Player: Player):
        """
            Здесь сама игра,
            которая заключена в цикле
        """
        pygame.init()

        height, width = 700, 550
        screen = pygame.display.set_mode((height, width))

        while self.running == "playing":
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = "stop_play"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        print("w")
                    if event.key == pygame.K_a:
                        print("a")
                    if event.key == pygame.K_d:
                        print("d")
                    if event.key == pygame.K_s:
                        print("s")

        self.check_coins()

        Map.draw()

        if Map.enemies:
            for enemy in Map.enemies:
                enemy.collision()
                enemy.move()

        Player.collision_player()
        Player.move()
