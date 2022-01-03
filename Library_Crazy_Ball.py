import pygame
import random


class NotSpriteError(TypeError):
    """Ошибка, в которой говорится о том, что
    спрайт отсутствует"""


def checking_sprite(sprite):
    if sprite:
        return sprite
    else:
        raise NotSpriteError


def load_image(name, colorkey=None):
    image = pygame.image.load(name)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Ground(pygame.sprite.Sprite):

    def __init__(self, sprite: str):
        super().__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.sprite = sprite

    def __str__(self):
        return "G"


class Player(pygame.sprite.Sprite):
    """Игрок, которым можно управлять"""

    def __init__(self, sprite: str, speed=10):
        super().__init__()
        self.image = load_image(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(200, 300))
        self.radius = self.rect.width // 2
        self.pos = 0, 0
        self.speed = speed
        self.coins = 0
        self.direction_x = 0
        self.direction_y = -1

    def update(self, Map):

        for block in Map.blocks:
            if self.rect.colliderect(block.rect):
                if self.direction_y == 0:
                    self.direction_x = -self.direction_x
                else:
                    self.direction_y = -self.direction_y
                break

        for i in range(len(Map.coins)):
            if self.rect.colliderect(Map.coins[i]):
                Map.coins.pop(i)
                break

        if self.rect.y < (len(Map.map[0])) * 50 and self.direction_y == 1:
            self.rect.y += self.direction_y * self.speed
        if self.rect.y >= 50 and self.direction_y == -1:
            self.rect.y += self.direction_y * self.speed

        if self.rect.x < (len(Map.map)) * 50 and self.direction_x == 1:
            self.rect.x += self.direction_x * self.speed
        if self.rect.x >= 50 and self.direction_x == -1:
            self.rect.x += self.direction_x * self.speed

    def set_pos(self, pos: tuple):
        x, y = pos
        self.rect.x = x * 50
        self.rect.y = y * 50

    def __str__(self):
        return "P"


class Enemy(pygame.sprite.Sprite):
    """Враги народа"""

    def __init__(self, sprite: str,
                 speed=5):
        super().__init__()
        self.image = load_image(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(200, 300))
        self.radius = self.rect.width // 2
        self.speed = speed
        self.direction_x = 1
        self.direction_y = 1
        self.speed_x = 0
        self.speed_y = 0
        self.set_speed()

    def update(self, Map):
        for block in Map.blocks:
            if self.rect.colliderect(block.rect):
                self.set_speed()
                self.direction_y = - self.direction_y
                self.direction_x = - self.direction_x
                break


        if self.rect.y >= (len(Map.map[0])) * 50 - 50:
            self.set_speed()
            self.direction_y = -1

        if self.rect.y <= 60:
            self.set_speed()
            self.direction_y = 1

        if self.rect.x >= (len(Map.map)) * 50 - 10:
            self.set_speed()
            self.direction_x = -1
        if self.rect.x <= 60:
            self.set_speed()
            self.direction_x = 1

        self.rect.x += self.direction_x * self.speed_x
        self.rect.y += self.direction_y * self.speed_y

    def set_pos(self, pos: tuple):
        x, y = pos
        self.rect.x = x * 50
        self.rect.y = y * 50

    def set_speed(self):
        """Создаёт рандомное направление для врага"""
        self.speed_x = random.randint(1, self.speed)
        self.speed_y = abs(self.speed - self.speed_x)

    def __str__(self):
        return "E"


class Block(pygame.sprite.Sprite):
    """Стены, через которые игрок не может пройти"""

    def __init__(self, sprite: str, pos: tuple):
        super(Block, self).__init__()
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(pos[-1] * 50 + 50, pos[0] * 50 + 50, 50, 50)
        self.pos = pos

    def __str__(self):
        return "B"


class Coin(pygame.sprite.Sprite):
    """Монеты"""

    def __init__(self, sprite: str, pos: tuple):
        super(Coin, self).__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.Rect(pos[-1] * 50 + 50, pos[0] * 50 + 50, 50, 50)
        self.pos = pos

    def __str__(self):
        return "C"


class Map:
    """Карта, на которой всё размещается"""

    def __init__(self, length: int, weight: int,
                 ground: Ground):
        self.blocks = list()
        self.enemies = list()
        self.coins = list()
        self.map = [(length + 1) * [ground] for _ in range(weight + 1)]
        self.borders = (length + 1, weight + 1)
        self.ground = ground

    def set_block(self, namefile: str, pos: tuple):
        x, y = pos
        block = Block(namefile, (x, y))
        self.blocks.append(block)
        self.map[y][x] = block

    def set_enemy(self, filename: str, pos: tuple, speed=1):
        enemy = Enemy(filename, speed)
        enemy.set_pos(pos)
        self.enemies.append(enemy)

    def set_player(self, player: Player, pos: tuple):
        player.set_pos(pos)

    def set_coin(self, namefile: str, pos: tuple):
        x, y = pos
        coin = Coin(namefile, (x, y))
        self.coins.append(coin)

    def draw(self):
        """рисование карты и краёв"""


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

    def play(self, Map: Map, Player: Player, screen: pygame.Surface) -> str:
        """
            Здесь сама игра,
            которая заключена в цикле
        """

        clock = pygame.time.Clock()
        FPS = 60
        while self.running == "playing":
            pygame.display.flip()
            pygame.display.update()
            for line in range(len(Map.map)):
                for el in range(len(Map.map[line])):
                    if type(Map.map[line][el]) == Block:
                        screen.blit(Map.map[line][el].image, Map.map[line][el].rect)
                    else:
                        screen.blit(Map.map[line][el].image, (50 + line * 50, 50 + el * 50))
            for coin in Map.coins:
                screen.blit(coin.image, coin.rect)

            for enemy in Map.enemies:
                enemy.update(Map)
                screen.blit(enemy.image, enemy.rect)

            Player.update(Map)
            screen.blit(Player.image, Player.rect)

            for enemy in Map.enemies:
                if Player.rect.colliderect(enemy):
                    self.running = "game over"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = "stop_play"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        Player.direction_y = -1
                        Player.direction_x = 0
                    if event.key == pygame.K_a:
                        Player.direction_y = 0
                        Player.direction_x = -1
                    if event.key == pygame.K_d:
                        Player.direction_y = 0
                        Player.direction_x = 1
                    if event.key == pygame.K_s:
                        Player.direction_y = 1
                        Player.direction_x = 0

            self.check_coins()

            if len(Map.coins) == 0:
                self.running = "win game"

            clock.tick(FPS)

        return self.running
