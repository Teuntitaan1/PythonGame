
import Colors
from Imports import *


class HealthBoost(pygame.sprite.Sprite):
    def __init__(self, name, tag, x, y):

        super().__init__()
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = x
        self.y = y
        # width and height variables for scaling the image
        self.height = 60
        self.width = 60

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen):

        # update statements and render statements
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        pygame.draw.rect(screen, Colors.green, self.rect)

    @staticmethod
    def boost(towhat):
        towhat.health += 10


class SpeedBoost(pygame.sprite.Sprite):
    def __init__(self, name, tag, x, y):

        super().__init__()
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = x
        self.y = y
        # width and height variables for scaling the image
        self.height = 60
        self.width = 60

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen):

        # update statements
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        pygame.draw.rect(screen, Colors.blue, self.rect)

    @staticmethod
    def boost(towhat):
        towhat.movementspeed += 1
