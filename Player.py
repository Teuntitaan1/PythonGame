import Colors
from Imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, img, name, tag, x, y, font, movementspeed, maxmovementspeed):

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
        # health indicator font
        self.font = font
        # health, needs to be present on every entity
        self.health = 150
        self.healthbegin = self.health
        # width and height variables for scaling the image
        self.height = img.get_height()
        self.width = img.get_width()
        # movementspeed regulators
        self.movementspeed = movementspeed
        self.maxmovementspeed = maxmovementspeed
        self.currentmovementspeed = movementspeed

        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen):

        # update statements
        self.updaterect()
        self.handlekeys()
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

    def handlekeys(self):

        key = pygame.key.get_pressed()

        # sprinting mechanic, changes the current movementspeed, can also be boosted by powerups
        if key[pygame.K_LSHIFT]:
            self.currentmovementspeed = self.maxmovementspeed
        else:
            self.currentmovementspeed = self.movementspeed

        if key[pygame.K_UP]:
            self.y -= self.currentmovementspeed
        if key[pygame.K_DOWN]:
            self.y += self.currentmovementspeed
        if key[pygame.K_LEFT]:
            self.x -= self.currentmovementspeed
        if key[pygame.K_RIGHT]:
            self.x += self.currentmovementspeed

        # debugging health indicator
        if key[pygame.K_w]:
            self.health -= 1
        if key[pygame.K_s]:
            self.health += 1

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
