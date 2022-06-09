# Import statements

import Colors
from Imports import *
from Player import Player

from Enemies import SimpleFollowEnemy
from Boosts import HealthBoost, SpeedBoost


def gameloop(windowsizex, windowsizey, refreshrate):
    pygame.init()

    # Pygame window setup
    windowsize = windowsizex, windowsizey
    pygame.display.set_caption("CubeGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    font = pygame.font.SysFont("Vera", 40)

    # variables
    framecounter = 0

    # entity spawning
    playerlist = pygame.sprite.GroupSingle()
    enemylist = pygame.sprite.Group()
    boostlist = pygame.sprite.Group()
    bulletlist = pygame.sprite.Group()

    for i in range(3):
        enemy = SimpleFollowEnemy("SimpleFollowEnemy" + str(i), "Enemy", random.randint(40, 800), random.randint(40, 800), font, random.randint(1, 3))
        print("Generated enemy" + str(i))
        enemylist.add(enemy)

    for i in range(1):
        player = Player("Player" + str(i), "Player", random.randint(40, 800), random.randint(40, 800), font, 3)
        print("Generated player" + str(i))
        playerlist.add(player)

    for i in range(1):
        boost = HealthBoost("HealthBoost" + str(i), "Boost", random.randint(40, 800), random.randint(40, 800))
        print("Generated Healthboost" + str(i))
        boostlist.add(boost)
    for i in range(2):
        boost = SpeedBoost("SpeedBoost" + str(i), "Boost", random.randint(40, 800), random.randint(40, 800))
        print("Generated Speedboost" + str(i))
        boostlist.add(boost)

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

        # entity's in playerlist updater
        playerlist.update(bulletlist, framecounter)
        # entity's in enemylist updater
        enemylist.update(screen, playerlist)
        # entity's in boostlist updater
        boostlist.update(screen)
        # entity's in bulletlist updater
        bulletlist.update(screen)
        # to render the player above the bullet(looks better)
        for i in playerlist:
            i.draw(screen)
        # player collision handler
        for i in playerlist:

            collidingenemysprite = pygame.sprite.spritecollideany(i, enemylist)

            # enemy collision handling
            if collidingenemysprite is not None:
                collidingenemysprite.attack(i)
                collidingenemysprite.kill()

            # boost handling collision
            collidingboostsprite = pygame.sprite.spritecollideany(i, boostlist)

            if collidingboostsprite is not None:
                collidingboostsprite.boost(i)
                collidingboostsprite.kill()

        # bullet collision handler
        for i in bulletlist:

            collidingenemysprite = pygame.sprite.spritecollideany(i, enemylist)

            # enemy collision handling
            if collidingenemysprite is not None:
                i.attack(collidingenemysprite)
                i.kill()

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
        framecounter += 1
