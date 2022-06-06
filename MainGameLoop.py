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
    pygame.display.set_caption("CubeGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    font = pygame.font.SysFont("Vera", 40)

    # entity spawning
    playerlist = pygame.sprite.Group()
    enemylist = pygame.sprite.Group()

    for i in range(15):
        enemy = SimpleFollowEnemy(pygame.transform.scale(Photos["RedPlayer.png"], [60, 60]), "Enemy" + str(i), "Enemy",
                                  random.randint(40, 800), random.randint(40, 800), font, random.randint(1, 3))
        print("Generated enemy" + str(i))
        enemylist.add(enemy)

    for i in range(1):
        player = Player(pygame.transform.scale(Photos["BluePlayer.png"], [60, 60]), "Player" + str(i), "Player",
                        random.randint(40, 800), random.randint(40, 800), font, 3, 6)
        print("Generated player" + str(i))
        playerlist.add(player)




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
        for i in playerlist:
            i.update(screen, )
            if i.health == 0:
                i.kill()
        for i in enemylist:
            i.update(screen, playerlist)
            if i.health == 0:
                i.kill()

        # collision handler
        for i in playerlist:
            collidingenemysprite = pygame.sprite.spritecollideany(i, enemylist)
            if collidingenemysprite is not None:
                i.health -= 10
                collidingenemysprite.kill()







        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
