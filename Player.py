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
        # movementspeed regulators
        self.movementspeed = self.width
        self.bulletmovementspeed = 0
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])
        # shooting shit
        self.framelastshot = 0
        self.shootdelay = 100
        # ticking system fucking shit shit
        self.lasttick = 0
        self.tickspeed = 50

        # direction
        self.direction = "right"
        self.currentaction = None

    def update(self, bulletlist, framecounter):

        # update statements
        self.checkhealth()
        self.updaterect()
        self.handlekeys()
        if framecounter - self.lasttick > self.tickspeed:
            self.lasttick = framecounter
            self.handleactions(bulletlist, framecounter)

    def handlekeys(self):

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
            self.currentaction = "shoot"

    def handleactions(self, bulletlist, framecounter):

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
        elif self.currentaction == "shoot":
            if self.canshoot(framecounter):
                self.shootsmallbullet(bulletlist)
                self.framelastshot = framecounter
        self.currentaction = None

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

        bulletlist.add(SmallBullet(bulletname, "bullet", self.x+self.width/2, self.y+self.height/2, 7 + self.bulletmovementspeed, self.direction))

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