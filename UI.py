import Colors

from Imports import *


class UI(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        # positioning
        self.tickerx = 600
        self.tickery = 5
        # width and height variables for scaling the image, movement speed directed by the direction
        self.tickerheight = 20

        # collisionbox
        # self.ticker = pygame.Rect([self.tickerx, self.tickery], [self.tickerwidth, self.tickerheight])


    # noinspection PyTypeChecker
    def update(self, screen, framecounter, lasttick):
        self.updateticker(screen, framecounter, lasttick)



    def updateticker(self, screen, framecounter, lasttick):
        self.ticker = pygame.Rect([self.tickerx, self.tickery], [framecounter - lasttick, self.tickerheight])
        pygame.draw.rect(screen, Colors.green, self.ticker)

