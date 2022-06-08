import Colors
from Photos import Photos
from Imports import *
from Bullet import SmallBullet


class Player(pygame.sprite.Sprite):
    def __init__(self, name, tag, x, y, font, movementspeed):

        super().__init__()
        # the sprite to be rendered
        self.image = Photos["PlayerSpriteRight.png"].convert()
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = x
        self.y = y
        # health indicator font
        self.font = font
        # health, needs to be present on every entity
        self.health = 150
        self.healthbegin = self.health
        # width and height variables for scaling the image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        # movementspeed regulators
        self.movementspeed = movementspeed
        self.bulletmovementspeedupgrade = 0
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

        # direction
        self.direction = "right"

    def update(self, screen, bulletlist):

        # update statements
        self.checkhealth()
        self.updaterect()
        self.handlekeys(bulletlist)
        screen.blit(self.image, [self.x, self.y])

        # health indicator rendering
        if self.calculateextrahealth() > 0:
            # if health is above the beginhealth(150 in this case)
            healthindicatortext = self.font.render(str(150), True, self.handletextcolor())
            screen.blit(healthindicatortext, [self.x, self.y - (self.height / 2.5)])
            # like the yellow hearts in minecraft
            extrahealthindicatortext = self.font.render(str(self.calculateextrahealth()), True, Colors.orange)
            screen.blit(extrahealthindicatortext, [self.x, self.y - ((self.height / 2.5)*2)])
        else:
            # if health is below or equal to the beginhealth(150 in this case)
            healthindicatortext = self.font.render(str(self.health), True, self.handletextcolor())
            screen.blit(healthindicatortext, [self.x, self.y - (self.height / 2.5)])

    def handlekeys(self, bulletlist):

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.y -= self.movementspeed
            self.direction = "up"
        elif key[pygame.K_DOWN]:
            self.y += self.movementspeed
            self.direction = "down"

        if key[pygame.K_LEFT]:
            self.image = Photos["PlayerSpriteLeft.png"].convert()
            self.x -= self.movementspeed
            self.direction = "left"
        elif key[pygame.K_RIGHT]:
            self.image = Photos["PlayerSpriteRight.png"].convert()
            self.x += self.movementspeed
            self.direction = "right"

        if key[pygame.K_SPACE]:
            self.shootsmallbullet(bulletlist)

        # debugging health indicator
        if key[pygame.K_w]:
            self.health += 1
        if key[pygame.K_s]:
            self.health -= 1

    # simple gradiant producer from green to red to indicate how close the player is to dying
    def handletextcolor(self):
        if self.calculateextrahealth() > 0:
            return 0, 150, 0
        else:
            return self.healthbegin - self.health, 0 + self.health, 0

    def updaterect(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def calculateextrahealth(self):
        if self.health - self.healthbegin > 0:
            return self.health - self.healthbegin
        else:
            return 0

    def checkhealth(self):
        if self.health == 0:
            self.kill()

    def shootsmallbullet(self, bulletlist):
        bulletname = "Bullet" + str(len(bulletlist)+1)

        bulletlist.add(SmallBullet(bulletname, "bullet", self.x, self.y, 7 + self.bulletmovementspeedupgrade, self.direction))
