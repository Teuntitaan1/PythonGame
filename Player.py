from Imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, img, name, tag, x, y):

        super().__init__()
        self.image = img
        self.name = name
        self.tag = tag
        self.x = x
        self.y = y
        self.rect = img.get_rect()

    def update(self, screen):

        screen.blit(self.image, [self.x, self.y])