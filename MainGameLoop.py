# Import statements
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
    player = Player(Photos["BluePlayer.png"], "Player1", "Player", 400, 400, font, 3)

    print("Starting game")

    # main loop
    while 1:

        # event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Shutting down game")
                sys.exit()

        # screen reset
        screen.fill(Colors.black)
        # player update
        player.update(screen)

        # screen update
        clock.tick(refreshrate)
        pygame.display.update()
