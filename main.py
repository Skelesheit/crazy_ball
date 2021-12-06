import Library_Crazy_Ball

import pygame

Game = Library_Crazy_Ball.Game()
Player = Library_Crazy_Ball.Player("aaa", (30, 30), 10)
Enemy = Library_Crazy_Ball.Enemy("aaa", (30, 30), 10)
Ground = Library_Crazy_Ball.Ground()
Map = Library_Crazy_Ball.Map(7, 7, Ground)
Map.set_player(Player, (5, 5))
Map.set_enemy(Enemy, (6, 6))
for i in range(Map.borders[0]):
    for j in range(Map.borders[-1]):
        print(Map.map[j][i], end=" ")
    print()
