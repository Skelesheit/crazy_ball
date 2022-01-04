def generate_random_level():
    from Library_Crazy_Ball import Player, Ground, Map, Game
    import random
    import pygame
    pygame.init()
    size = 1800, 1000
    screen = pygame.display.set_mode(size)
    Ground = Ground("ground.jpg")
    Map = Map(15, 20, Ground)
    Player = Player("ball_owl.png", speed=4)
    Map.set_player(Player, (15, 15))
    for _ in range(15):
        x, y = random.randint(1, 15), random.randint(1, 15)
        Map.set_block("block.png", (x, y))
    for _ in range(6):
        x, y = random.randint(1, 15), random.randint(1, 15)
        Map.set_coin("ball_panda.png", (x, y))
    for _ in range(7):
        x, y = random.randint(1, 15), random.randint(1, 15)
        Map.set_enemy("ball_tiger.png", (x, y), 7)
    Game1 = Game()
    mod = Game1.play(Map, Player, screen)
    return mod

