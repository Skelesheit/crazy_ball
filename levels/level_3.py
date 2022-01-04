def load_level():
    from Library_Crazy_Ball import Player, Ground, Map, Game
    import pygame
    pygame.init()
    size = 1800, 1000
    screen = pygame.display.set_mode(size)
    Player = Player("ball_owl.png", 5)
    Ground = Ground("ground.jpg")
    Map = Map(12, 20, Ground)
    Map.set_player(Player, (5, 5))
    Map.set_coin("coin.png", (4, 4))
    Map.set_coin("coin.png", (0, 0))
    Map.set_coin("coin.png", (5, 5))
    Map.set_coin("coin.png", (10, 10))
    Map.set_coin("coin.png", (0, 20))
    Map.set_coin("coin.png", (0, 10))
    Map.set_coin("coin.png", (12, 20))
    for i in range(3, 6):
        Map.set_block("block.png", (10, i))
    for i in range(3, 8):
        Map.set_block("block.png", (i, 15))
    for i in range(2, 7):
        Map.set_block("block.png", (i, 2))
    for i in range(7, 11):
        Map.set_block("block.png", (6, i))
    for i in range(2, 7):
        Map.set_enemy("ball_tiger.png", (9, 9), 8)

    Game1 = Game()
    return Game1.play(Map, Player, screen)
