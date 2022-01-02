import Library_Crazy_Ball

import pygame

"""sprite = pygame.surface([100, 100])
image = pygame.image.load("Player.jpg")
image.set_colorkey(-1)"""

Player = Library_Crazy_Ball.Player("aaa", (30, 30), 10)
Enemy = Library_Crazy_Ball.Enemy("aaa", (30, 30), 10)
Ground = Library_Crazy_Ball.Ground()
Map = Library_Crazy_Ball.Map(8, 8, "ground")
Map.set_player(Player, (5, 5))
Map.set_enemy(Enemy, (6, 6))

Game1 = Library_Crazy_Ball.Game()

Game1.play(Map, Player)
