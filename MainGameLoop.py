from Imports import *
from Player import Player
from Photos import Photos


def gameloop(windowsizex, windowsizey, refreshrate):

    windowsize = windowsizex, windowsizey
    pygame.display.set_caption("TriangleGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshrate = refreshrate
    pygame.init()


    play = Player(Photos["Triangle"], "Player1", "Player", 400, 400)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        play.update(screen)
        clock.tick(refreshrate)
        pygame.display.update()
