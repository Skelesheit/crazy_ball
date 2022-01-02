import pygame


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
        pos = tuple()

    def __str__(self):
        return "G"


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite: str, size=(30, 30), speed=10):
        super().__init__()
        self.image = load_image(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
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
                print(self.rect, block.rect)
                if self.rect.y + 5 > block.rect.y and self.direction_y == 1:
                    self.direction_y = 0
                    print(self.rect, block.rect)

        if self.rect.y < (len(Map.map[0]) - 2) * 50 - 50 and self.direction_y == 1:
            self.rect.y += self.direction_y * self.speed
        if self.rect.y >= 50 and self.direction_y == -1:
            self.rect.y += self.direction_y * self.speed

        if self.rect.x < (len(Map.map) - 3) * 50 - 50 and self.direction_x == 1:
            self.rect.x += self.direction_x * self.speed
        if self.rect.x >= 50 and self.direction_x == -1:
            self.rect.x += self.direction_x * self.speed

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


class Enemy(pygame.sprite.Sprite):
    """Враги народа"""

    def __init__(self, sprite: str,
                 size=(20, 20), speed=1):
        super().__init__()
        self.sprite = sprite
        self.pos = (0, 0)
        self.speed = speed
        self.size = size
        self.direction_x = 0
        self.direction_y = 0

    def collision(self):
        """Столкновение врага со стеной"""

    def draw(self):
        """Рисует врага"""

    def update(self):
        """"""

    def __str__(self):
        return "E"


class Block(pygame.sprite.Sprite):
    def __init__(self, sprite: str, pos: tuple):
        super(Block, self).__init__()
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(pos[0] * 50 + 50, pos[-1] * 50 + 50))
        self.pos = pos

    def __str__(self):
        return "B"

    def draw(self):
        """рисует стену"""


class Coin(pygame.sprite.Sprite):
    """Монеты"""

    def __init__(self, sprite: str):
        super(Coin, self).__init__()
        self.sprite = sprite
        self.pos = tuple()

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

    def set_block(self, block: Block, pos=None):
        if pos:
            x, y = pos

        else:
            x, y = block.pos
        self.blocks.append(block)
        self.map[x][y] = block

    def set_enemy(self, enemy: Enemy, pos: tuple):
        enemy.pos = pos
        self.enemies.append(enemy)

    def set_player(self, player: Player, pos: tuple):
        player.pos = pos

    def set_coin(self, coin: Coin, pos: tuple):
        x, y = pos
        coin.pos = pos
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

    def play(self, Map: Map, Player: Player, screen: pygame.Surface):
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
                    screen.blit(Map.map[line][el].image, (50 + line * 50, 50 + el * 50))

            Player.update(Map)
            screen.blit(Player.image, Player.rect)

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

            if Map.enemies:
                for enemy in Map.enemies:
                    enemy.collision()
                    enemy.move()

            Player.collision_player()
            clock.tick(FPS)
