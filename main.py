import pygame
import Library_Crazy_Ball
from Library_Crazy_Ball import *
from copy import copy
pygame.init()

size = a, b = 1200, 800
screen = pygame.display.set_mode(size)

Ground = Ground("ground.jpg")
Map = Map(15, 20, Ground)
Player = Player("ball_owl.png", speed=4)
Map.set_player(Player, (5, 5))
Map.set_block("block.png", (2, 2))
Map.set_block("block.png", (3, 3))
Map.set_block("block.png", (5, 5))
Map.set_block("block.png", (6, 5))
Map.set_coin("ball_panda.png", (4, 4))
Map.set_coin("ball_panda.png", (5, 7))




Game1 = Library_Crazy_Ball.Game()

Game1.play(Map, Player, screen)
