# Import statements
from Imports import *
from Level import Level
from Colors import *
from Player import Player
from GeneralFunctions import generaterandomarray


def gameloop(windowsizex, windowsizey, refreshrate):
    pygame.init()

    # Pygame window setup
    windowsize = windowsizex, windowsizey
    pygame.display.set_caption("Floors and doors")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    font = pygame.font.SysFont("Vera", 40)

    # variables
    framecounter = 0
    currentlevelx = 0
    currentlevely = 0
    levelnumber = 1
    levelwidth, levelheight = 10, 10
    levellist = [[0 for _ in range(levelwidth)] for _ in range(levelheight)]
    xrow = 0
    yrow = 0
    distancewhenswitchinglevels = 0
    posarray = generaterandomarray()
    # player generation
    randompos = random.randint(0, len(posarray)-1)
    player = Player("Player0", "Player", posarray[randompos], font)
    posarray.pop(randompos)
    print("Player has been generated")

    for i in range(levelheight):
        for j in range(levelwidth):
            level = Level(random.randint(0, 1), random.randint(0, 5), levelnumber, font, player, posarray)
            # noinspection PyTypeChecker
            levellist[xrow][yrow] = level
            xrow += 1
            levelnumber += 1
        yrow += 1
        xrow = 0

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
        # simply clearing the screen
        screen.fill(black)
        # global level update statement
        levellist[currentlevelx][currentlevely].update(screen, framecounter)

        text = font.render("level: " + str(currentlevelx) + ", " + str(currentlevely), True, white)
        screen.blit(text, (0, 0))

        # map movement logic
        # player going right
        if player.x > screen.get_width():
            if currentlevelx < levelwidth:
                currentlevelx += 1
                player.x = 0 + distancewhenswitchinglevels
            else:
                player.x = screen.get_width()
        # player going left
        elif player.x < 0:
            if currentlevelx > 0:
                currentlevelx -= 1
                player.x = screen.get_width() - distancewhenswitchinglevels
            else:
                player.x = 0
        # player going down
        elif player.y > screen.get_height():
            if currentlevely < levelheight:
                currentlevely += 1
                player.y = 0 + distancewhenswitchinglevels
            else:
                player.y = screen.get_height()
        # player going up
        elif player.y < 0:
            if currentlevely > 0:
                currentlevely -= 1
                player.y = screen.get_height() - distancewhenswitchinglevels
            else:
                player.y = 0 + distancewhenswitchinglevels

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
        framecounter += 1
