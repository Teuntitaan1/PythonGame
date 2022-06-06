# Import statements
import pygame

import Colors
from Imports import *
from Player import Player
from Photos import Photos


def gameloop(windowsizex, windowsizey, refreshrate):
    pygame.init()

    # Pygame window setup
    windowsize = windowsizex, windowsizey
    pygame.display.set_caption("TriangleGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    font = pygame.font.SysFont("Vera", 72)

    # entity spawning
    entitylist = []

    for i in range(9):
        player = Player(Photos["BluePlayer.png"], "Player"+str(i), "Player", random.randint(40, 800), random.randint(40, 800), font, 3)
        print("Generated player" + str(i))
        entitylist.append(player)

    print("Starting game")

    # main loop
    while 1:

        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Shutting down game")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Shutting down game")
                    sys.exit()

        # screen reset
        screen.fill(Colors.black)
        # player update
        for i in entitylist:
            i.update(screen)

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
