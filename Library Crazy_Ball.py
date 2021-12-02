def __doc__():
    """Игровая мини-библиотека или мини-фреймворк,
    созданная из pygame.
    название её: Crazy_ball"""

class Player:
    def __init__(self, sprite=None, size=(30, 30), speed=10):
        if not sprite:
            pass
        self.sprite = sprite
        self.size = size()
        self.speed = speed

    def move(self):
        """движение игрока"""

    def set_coords(self):
        """Метод для смены координат"""

    def collision_player(self):
        """Столкновение игрока"""

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

    def collect_coin(self):
        """Сбор монет"""

class Enemy:
    """Враги народа"""
    def __init__(self):
        pass

