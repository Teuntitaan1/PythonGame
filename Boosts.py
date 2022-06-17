
import Colors
from Imports import *


class HealthBoost(pygame.sprite.Sprite):
    def __init__(self, name, tag, xycoord):

        super().__init__()
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = xycoord["x"]
        self.y = xycoord["y"]
        # width and height variables for scaling the image
        self.height = 80
        self.width = 80

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen):

        # update statements and render statements
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        pygame.draw.rect(screen, Colors.green, self.rect)

    @staticmethod
    def boost(towhat):
        towhat.health += 10


