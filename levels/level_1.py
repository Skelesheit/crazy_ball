def load_level():
    from Library_Crazy_Ball import Player, Ground, Map, Game
    import pygame
    pygame.init()
    size = 1800, 1000
    screen = pygame.display.set_mode(size)
    Ground = Ground("ground.jpg")
    Map = Map(10, 10, Ground)
    Player = Player("ball_owl.png", 5)
    Map.set_player(Player, (5, 5))
    for i in range(5):
        Map.set_block("block.png", (i, 2))
    Map.set_coin("coin.png", (4, 4))
    Map.set_coin("coin.png", (0, 0))
    Map.set_coin("coin.png", (5, 5))
    Map.set_coin("coin.png", (10, 10))
    Map.set_coin("coin.png", (0, 10))
    Map.set_coin("coin.png", (10, 0))
    Map.set_block("block.png", (6, 5))
    Map.set_block("block.png", (6, 4))
    Map.set_block("block.png", (6, 3))
    Map.set_block("block.png", (7, 6))
    Map.set_block("block.png", (8, 6))
    Map.set_block("block.png", (9, 6))
    Map.set_block("block.png", (10, 6))
    Map.set_coin("coin.png", (10, 5))
    Game1 = Game()
    win = Game1.play(Map, Player, screen)
    return win


