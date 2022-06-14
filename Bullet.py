import Colors

from Imports import *


class SmallBullet(pygame.sprite.Sprite):
    def __init__(self, name, tag, x, y, movementspeed, direction):

        super().__init__()
        # the sprite to be rendered
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = x
        self.y = y
        # width and height variables for scaling the image
        self.height = 20
        self.width = 40
        # movementspeed regulators
        self.movementspeed = movementspeed
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

        self.direction = direction

    # noinspection PyTypeChecker
    def update(self, screen, enemylist):

        if self.x > (screen.get_width()+200) or self.x < -200:
            self.kill()

        if self.y > (screen.get_height()+200) or self.y < -200:
            self.kill()

        # looks where to go
        if self.direction == "up":
            self.y -= self.movementspeed
        elif self.direction == "down":
            self.y += self.movementspeed
        elif self.direction == "left":
            self.x -= self.movementspeed
        elif self.direction == "right":
            self.x += self.movementspeed
        self.updaterect()

        pygame.draw.rect(screen, Colors.grey, self.rect)

        collidingenemysprite = pygame.sprite.spritecollideany(self, enemylist)

        # enemy collision handling
        if collidingenemysprite is not None:
            self.attack(collidingenemysprite)
            self.kill()

    def updaterect(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    @staticmethod
    def attack(towhat):
        towhat.health -= 10

