from Imports import *
from Enemies import SimpleFollowEnemy
from Boosts import HealthBoost
from GeneralFunctions import getgridposition
# todo fix the bulletshit
# todo fix the levelgrid
# todo add a level editor(should not be that hard just add it as a statein maingameloop
# todo add a save and load system, saving should be in a .json file and loading should be easy
class Level:
    def __init__(self, amountofenemies, numberofpowerups, levelnumber, font, player, posarray):

        # every entity should be on the grid
        levelgridwidth, levelgridheight = 10, 10
        self.levelgrid = [[0 for _ in range(levelgridwidth)] for _ in range(levelgridheight)]
        self.levelgrid[int(player.x/800-1)][int(player.y/800-1)] = player
        # entity spawning
        self.playerlist = pygame.sprite.GroupSingle()
        self.enemylist = pygame.sprite.Group()
        self.boostlist = pygame.sprite.Group()
        self.bulletlist = pygame.sprite.Group()
        # makes a seperate copy of the array so that it does not interfere with the global array
        self.posarray = posarray.copy()
        # variables
        self.name = "Level" + str(levelnumber)
        self.lasttick = 0
        self.tickspeed = 50

        for i in range(amountofenemies):
            # generates a random position on the array
            randomnum = random.randint(0, len(self.posarray)-1)
            enemy = SimpleFollowEnemy("SimpleFollowEnemy" + str(i), "Enemy", self.posarray[randomnum], font)
            # removes the position from the available points in the array so that nothing spawns on eachother
            gridposition = getgridposition(self.posarray[randomnum])
            # noinspection PyTypeChecker
            self.levelgrid[gridposition["x"]][gridposition["y"]] = enemy
            self.posarray.pop(randomnum)

            print("Generated enemy" + str(i))
            self.enemylist.add(enemy)

        self.playerlist.add(player)

        for i in range(numberofpowerups):
            # generates a random position on the array
            randomnum = random.randint(0, len(self.posarray)-1)
            which = random.randint(1, 100)

            boost = HealthBoost("HealthBoost" + str(i), "Boost", self.posarray[randomnum])
            print("Generated Healthboost" + str(i))
            self.boostlist.add(boost)
            gridposition = getgridposition(self.posarray[randomnum])
            # noinspection PyTypeChecker
            self.levelgrid[gridposition["x"]][gridposition["y"]] = boost
            # removes the position from the available points in the array so that nothing spawns on eachother
            self.posarray.pop(randomnum)

        print("Level number " + str(levelnumber) + " has been generated.")

    def update(self, screen, framecounter):
        # update system
        x = 0
        y = 0
        for i in range(10):
            for j in range(10):
                if self.levelgrid[j][i] != 0:
                    if self.levelgrid[j][i].tag == "Enemy":
                        self.levelgrid[j][i].update(screen, self.playerlist)
                    if self.levelgrid[j][i].tag == "Player":
                        self.levelgrid[j][i].update(screen, framecounter, self.bulletlist)
                    if self.levelgrid[j][i].tag == "Boost":
                        self.levelgrid[j][i].update(screen)
                x += 1
            x = 0
            y += 1
        # ticker system
        if framecounter - self.lasttick > self.tickspeed:
            x = 0
            y = 0
            for i in range(10):
                for j in range(10):
                    if self.levelgrid[j][i] != 0:
                        if self.levelgrid[j][i].tag == "Enemy":
                            self.levelgrid[j][i].tick()
                        if self.levelgrid[j][i].tag == "Player":
                            self.levelgrid[j][i].tick()
                    x += 1
                x = 0
                y += 1
            self.lasttick = framecounter
        """
        # player collision handler
        for i in self.playerlist:

            collidingenemysprite = pygame.sprite.spritecollideany(i, self.enemylist)

            # enemy collision handling
            if collidingenemysprite is not None:
                collidingenemysprite.attack(i)
                collidingenemysprite.kill()

            # boost handling collision
            collidingboostsprite = pygame.sprite.spritecollideany(i, self.boostlist)

            if collidingboostsprite is not None:
                collidingboostsprite.boost(i)
                collidingboostsprite.kill()
        """



