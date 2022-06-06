from Imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, img, name, tag, x, y, font, movementspeed):

        super().__init__()
        self.image = img
        self.name = name
        self.tag = tag
        self.x = x
        self.y = y
        self.rect = img.get_rect()
        self.font = font
        self.health = 100
        self.height = img.get_height()
        self.width = img.get_width()
        self.movementspeed = movementspeed

    def update(self, screen):

        self.handlekeys()
        screen.blit(self.image, [self.x, self.y])

        text = self.font.render(str(self.health), True, (0, 128, 0))
        screen.blit(text, [self.x, self.y - self.height/1.7])

    def handlekeys(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.y -= self.movementspeed
        if key[pygame.K_DOWN]:
            self.y += self.movementspeed
        if key[pygame.K_LEFT]:
            self.x -= self.movementspeed
        if key[pygame.K_RIGHT]:
            self.x += self.movementspeed


