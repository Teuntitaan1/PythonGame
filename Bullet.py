import Colors

from Imports import *


class SmallBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):

        super().__init__()
        self.x = x
        self.y = y
        # width and height variables for scaling the image, movement speed directed by the direction
        if direction == "left" or direction == "right":
            print("left or right")
            self.height = 20
            self.width = 40
        elif direction == "up" or direction == "down":
            print("up or down")
            self.height = 40
            self.width = 20
        self.movementspeed = 80

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

        self.direction = direction

    # noinspection PyTypeChecker
    def update(self, screen, enemylist):

        if self.x > (screen.get_width()+200) or self.x < -200:
            self.kill()

        if self.y > (screen.get_height()+200) or self.y < -200:
            self.kill()

        self.updaterect()
        pygame.draw.rect(screen, Colors.grey, self.rect)

        collidingenemysprite = pygame.sprite.spritecollideany(self, enemylist)

        # enemy collision handling
        if collidingenemysprite is not None:
            self.attack(collidingenemysprite)
            self.kill()


    def tick(self, tickspeed):
        # looks where to go
        movementbyincrements = tickspeed/self.movementspeed

        if self.direction == "up":
            for i in range(tickspeed):
                self.y -= movementbyincrements
        elif self.direction == "down":
            for i in range(tickspeed):
                self.y += movementbyincrements
        elif self.direction == "left":
            for i in range(tickspeed):
                self.x -= movementbyincrements
        elif self.direction == "right":
            for i in range(tickspeed):
                 self.x += movementbyincrements

    def updaterect(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    @staticmethod
    def attack(towhat):
        towhat.health -= 10

