import Colors
from GeneralFunctions import *
from Imports import *


class SimpleFollowEnemy(pygame.sprite.Sprite):
    def __init__(self, name, tag, xycoord, font, movementspeed):

        super().__init__()
        # the sprite to be rendered
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
        self.health = 10
        # width and height variables for scaling the image
        self.height = 80
        self.width = 80
        # movementspeed regulators
        self.movementspeed = movementspeed
        # collisionbox
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def update(self, screen, playerlist):

        # update statements
        self.checkhealth()
        self.updaterect()
        self.followplayer(playerlist)
        pygame.draw.rect(screen, Colors.red, self.rect)

        # health indicator rendering
        text = self.font.render(str(self.health), True, Colors.white)
        screen.blit(text, [self.x, self.y - (self.height/2.5)])

    def followplayer(self, playerlist):

        # simple check to see if there are players left
        playercount = 0
        for i in playerlist:
            if i.tag == "Player":
                playercount += 1

        if playercount != 0:
            # determining offset
            for i in playerlist:
                if i.tag == "Player":
                    xoffset = self.x - i.x
                    yoffset = self.y - i.y
                    break
            # moving accordingly
            if returnpositive(xoffset) > returnpositive(yoffset):
                if xoffset < 0:
                    self.x += self.movementspeed
                if xoffset > 0:
                    self.x -= self.movementspeed
            else:
                if yoffset < 0:
                    self.y += self.movementspeed
                if yoffset > 0:
                    self.y -= self.movementspeed



    def updaterect(self):
        self.rect = pygame.Rect([self.x, self.y], [self.width, self.height])

    def checkhealth(self):
        if self.health == 0 or self.health < 0:
            self.kill()

    @staticmethod
    def attack(towhat):
        towhat.health -= 10