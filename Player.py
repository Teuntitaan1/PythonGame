import Colors
from Photos import Photos
from Imports import *
from Bullet import SmallBullet


class Player(pygame.sprite.Sprite):
    def __init__(self, name, tag, x, y, font):

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
        self.movementspeed = 3
        self.bulletmovementspeedupgrade = 0
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

        # shooting shit
        self.framelastshot = 0
        self.shootdelay = 100

        # direction
        self.direction = "right"

    def update(self, bulletlist, framecounter):

        # update statements
        self.checkhealth()
        self.updaterect()
        self.handlekeys(bulletlist, framecounter)

    def handlekeys(self, bulletlist, framecounter):

        key = pygame.key.get_pressed()

        # movement script
        # what in the holy mother of god have i created TODO fix this fucking shit
        if key[pygame.K_LEFT]:
            if key[pygame.K_UP]:
                self.direction = "leftup"
                self.x -= self.movementspeed
                self.y -= self.movementspeed
            elif key[pygame.K_DOWN]:
                self.direction = "leftdown"
                self.x -= self.movementspeed
                self.y += self.movementspeed
            else:
                self.direction = "left"
                self.x -= self.movementspeed
                self.image = Photos["PlayerSpriteLeft.png"].convert()
        elif key[pygame.K_RIGHT]:
            if key[pygame.K_UP]:
                self.direction = "rightup"
                self.x += self.movementspeed
                self.y -= self.movementspeed
            elif key[pygame.K_DOWN]:
                self.direction = "rightdown"
                self.x += self.movementspeed
                self.y += self.movementspeed
            else:
                self.direction = "right"
                self.x += self.movementspeed
                self.image = Photos["PlayerSpriteRight.png"].convert()
        elif key[pygame.K_UP]:
            if key[pygame.K_LEFT]:
                self.direction = "leftup"
                self.x -= self.movementspeed
                self.y -= self.movementspeed
            elif key[pygame.K_RIGHT]:
                self.direction = "rightup"
                self.x += self.movementspeed
                self.y -= self.movementspeed
            else:
                self.direction = "up"
                self.y -= self.movementspeed
        elif key[pygame.K_DOWN]:
            if key[pygame.K_LEFT]:
                self.direction = "leftdown"
                self.x -= self.movementspeed
                self.y += self.movementspeed
            elif key[pygame.K_RIGHT]:
                self.direction = "rightdown"
                self.x += self.movementspeed
                self.y += self.movementspeed
            else:
                self.direction = "down"
                self.y += self.movementspeed

        if key[pygame.K_SPACE]:
            if self.canshoot(framecounter):
                self.shootsmallbullet(bulletlist)
                self.framelastshot = framecounter

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
        if self.health == 0 or self.health < 0:
            self.kill()

    def shootsmallbullet(self, bulletlist):
        bulletname = "Bullet" + str(len(bulletlist)+1)

        bulletlist.add(SmallBullet(bulletname, "bullet", self.x+self.width/2, self.y+self.height/2, 7 + self.bulletmovementspeedupgrade, self.direction))

    def canshoot(self, framecounter):
        if self.framelastshot + self.shootdelay < framecounter:
            return True
        else:
            return False

    def draw(self, screen):

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