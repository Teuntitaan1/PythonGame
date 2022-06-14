# Import statements
from Imports import *
from Level import Level
from Colors import *
from Player import Player



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
    currentlevel = 0
    levellist = []

    # player generation
    player = Player("Player0", "Player", random.randint(40, 760), random.randint(40, 760), font)
    print("Player has been generated")


    for i in range(60):
        level = Level(random.randint(0, 7), random.randint(0, 7), i, font, player)
        levellist.append(level)

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



        screen.fill(black)
        levellist[currentlevel].update(screen, framecounter)

        if len(levellist[currentlevel].enemylist) == 0:
            currentlevel += 1

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
        framecounter += 1
