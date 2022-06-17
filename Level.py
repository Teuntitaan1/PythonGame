from Imports import *
from Enemies import SimpleFollowEnemy
from Boosts import HealthBoost

# todo fix the bulletshit

class Level:
    def __init__(self, amountofenemies, numberofpowerups, levelnumber, font, player, posarray):

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

            # removes the position from the available points in the array so that nothing spawns on eachother
            self.posarray.pop(randomnum)

        print("Level number " + str(levelnumber) + " has been generated.")

    def update(self, screen, framecounter):

        # entity's in playerlist updater
        self.playerlist.update(framecounter, self.bulletlist)
        # entity's in enemylist updater
        self.enemylist.update(screen, self.playerlist)
        # entity's in boostlist updater
        self.boostlist.update(screen)
        # entity's in bulletlist updater
        self.bulletlist.update(screen, self.enemylist)
        # to render the player above the bullet(looks better)
        for i in self.playerlist:
            i.draw(screen)
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


        # ticking system
        if framecounter - self.lasttick > self.tickspeed:

            for i in self.playerlist:
                i.tick()
            for i in self.enemylist:
                i.tick()
            for i in self.bulletlist:
                i.tick(self.tickspeed)

            self.lasttick = framecounter



