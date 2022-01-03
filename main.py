from Library_Crazy_Ball import *

pygame.init()

size = a, b = 1200, 1000
screen = pygame.display.set_mode(size)

Ground = Ground("ground.jpg")
Map = Map(20, 20, Ground)
Player = Player("ball_owl.png", speed=4)
Map.set_player(Player, (15, 15))
Map.set_block("block.png", (2, 2))
Map.set_block("block.png", (3, 3))
Map.set_block("block.png", (5, 5))
Map.set_block("block.png", (6, 5))
Map.set_coin("ball_panda.png", (4, 4))
Map.set_coin("ball_panda.png", (5, 7))
Map.set_enemy("ball.png", (7, 8), speed=10)
Map.set_enemy("ball.png", (3, 2), speed=10)
Game1 = Game()

mod = Game1.play(Map, Player, screen)
if mod == "win game":
    print("you win")
elif mod == "game over":
    print(mod)
