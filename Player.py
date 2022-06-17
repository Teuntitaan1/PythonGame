import Colors
from Photos import Photos
from Imports import *
from Bullet import SmallBullet


class Player(pygame.sprite.Sprite):
    def __init__(self, name, tag, xycoord, font):

        super().__init__()
        # the sprite to be rendered
        self.image = Photos["PlayerSpriteRight.png"].convert()
        # kind of useless right now
        self.name = name
        # tag for the collision manager to determine what to do
        self.tag = tag
        # positioning
        self.x = xycoord["x"]
        self.y = xycoord["y"]
        # health indicator font
        self.font = font
        # health, needs to be present on every entity
        self.health = 150
        self.healthbegin = self.health
        # width and height variables for scaling the image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        # movementspeed
        self.movementspeed = self.width
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        # shooting shit
        self.framelastshot = 0
        self.shootdelay = 40
        self.direction = "right"


        # action caching
        self.currentaction = None

    def update(self, framecounter, bulletlist):

        # update statements
        self.checkhealth()
        self.updaterect()
        self.handlekeys(framecounter, bulletlist)

    def tick(self):

        if self.currentaction == "left":
            self.x -= self.movementspeed
        elif self.currentaction == "right":
            self.x += self.movementspeed
        elif self.currentaction == "up":
            self.y -= self.movementspeed
        elif self.currentaction == "down":
            self.y += self.movementspeed
        elif self.currentaction is None:
            pass
        self.currentaction = None

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

    def updaterect(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def handlekeys(self, framecounter, bulletlist):

        key = pygame.key.get_pressed()

        # movement script
        if key[pygame.K_LEFT]:
            self.currentaction = "left"
            self.direction = "left"
            self.image = Photos["PlayerSpriteLeft.png"].convert()

        elif key[pygame.K_RIGHT]:
            self.currentaction = "right"
            self.direction = "right"
            self.image = Photos["PlayerSpriteRight.png"].convert()

        elif key[pygame.K_UP]:
            self.currentaction = "up"
            self.direction = "up"
            self.image = Photos["PlayerSpriteUp.png"].convert()
        elif key[pygame.K_DOWN]:
            self.currentaction = "down"
            self.direction = "down"
            self.image = Photos["PlayerSpriteDown.png"].convert()
        elif key[pygame.K_SPACE]:
            if self.canshoot(framecounter):
                self.shootsmallbullet(bulletlist)
                self.framelastshot = framecounter

    # simple gradiant producer from green to red to indicate how close the player is to dying
    def handletextcolor(self):
        if self.calculateextrahealth() > 0:
            return 0, 150, 0
        else:
            return self.healthbegin - self.health, 0 + self.health, 0

    def checkhealth(self):
        if self.health == 0 or self.health < 0:
            self.kill()

    def calculateextrahealth(self):
        if self.health - self.healthbegin > 0:
            return self.health - self.healthbegin
        else:
            return 0

    def shootsmallbullet(self, bulletlist):


        bulletlist.add(SmallBullet(self.x+self.width/2, self.y+self.height/2, self.direction))

    def canshoot(self, framecounter):
        if self.framelastshot + self.shootdelay < framecounter:
            return True
        else:
            return False
