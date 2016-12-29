import pygame, sys

from game import Game, Player

pygame.init()
size = width, height = 1020, 640
black = 0, 0, 0
myfont = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game = Game(Player("p1", "x"), Player("p2", "o"))

while True:

    events = pygame.event.get()
    game = game.update(events)

    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(10) / 1000.0

    screen.fill(black)
    game.draw(screen)
    pygame.display.flip()