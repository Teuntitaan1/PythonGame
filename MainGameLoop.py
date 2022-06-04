from Imports import *

def GameLoop(WindowSizex, WindowSizey, RefreshRate):

    windowsize = width, height = WindowSizex, WindowSizey
    pygame.display.set_caption("TriangleGame")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowsize)
    refreshRate = RefreshRate
    pygame.init()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(refreshRate)
        pygame.display.update()

