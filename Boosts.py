from Imports import *


class HealthBoost(pygame.sprite.Sprite):
    def __init__(self, img, name, tag, x, y):

        super().__init__()
        # the sprite to be rendered
        self.image = img
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = x
        self.y = y
        # width and height variables for scaling the image
        self.height = img.get_height()
        self.width = img.get_width()

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen):

        # update statements
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

        screen.blit(self.image, [self.x, self.y])

    @staticmethod
    def boost(towhat):
        if towhat.health < towhat.healthbegin:
            towhat.health += 10
