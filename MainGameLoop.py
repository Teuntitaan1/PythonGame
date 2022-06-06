# Import statements
import pygame.sprite

import Colors
from Imports import *
from Player import Player
from Photos import Photos
from Enemies import SimpleFollowEnemy


def gameloop(windowsizex, windowsizey, refreshrate):
    pygame.init()

    # Pygame window setup
    windowsize = windowsizex, windowsizey
    pygame.display.set_caption("TriangleGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    font = pygame.font.SysFont("Vera", 40)

    # entity spawning
    entitylist = pygame.sprite.Group()

    for i in range(1):
        player = Player(pygame.transform.scale(Photos["BluePlayer.png"], [60, 60]), "Player"+str(i), "Player", random.randint(40, 800), random.randint(40, 800), font, 3, 6)
        print("Generated player" + str(i))
        entitylist.add(player)

    for i in range(1):
        enemy = SimpleFollowEnemy(pygame.transform.scale(Photos["RedPlayer.png"], [60, 60]), "Enemy"+str(i), "Enemy", random.randint(40, 800), random.randint(40, 800), font, random.randint(1,3))
        print("Generated enemy" + str(i))
        entitylist.add(enemy)


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
        # entity updating
        for i in entitylist:
            i.update(screen, entitylist)
            if i.health == 0:
                i.kill()

            print(pygame.sprite.spritecollide(i, entitylist, False))



        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
