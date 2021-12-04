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


class Map:
    """Карта, на которой всё размещается"""

    def __init__(self):
        pass


class Game:
    """Правила игры"""

    def __init__(self, *args):
        None

    def kill_player(self):
        """Смерть игрока"""

    def win_player(self):
        """Победа игрока"""

    def collision_player(self):
        """Столкновение врага"""

    def check_coins(self):
        """Проверка количества монет.
        Есливсе собраны, то игрок выиграл"""

    def play(self):
        """Здесь сама игра,
        которая заключена в цикле
        """


class Enemy:
    """Враги народа"""

    def __init__(self, sprite=None, pos=(0, 0),
                 size=(20, 20), speed=10):
        checking_sprite(self, sprite)
        self.pos = pos
        self.speed = speed
        self.size = size
