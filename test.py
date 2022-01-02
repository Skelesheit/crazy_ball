import pygame, random

pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)


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


image = load_image("Player.png")

image = pygame.transform.scale(image, (100, 100))

pos = 300, 300
pygame.mouse.set_visible(False)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

    if pygame.mouse.get_focused():
        screen.fill((0, 0, 0))
        pos = pygame.mouse.get_pos()
        pos = pos[0] - 4, pos[-1]

    screen.blit(image, pos)
