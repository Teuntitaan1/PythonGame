from Imports import *
from Player import Player
from Enemies import SimpleFollowEnemy
from Boosts import HealthBoost, SpeedBoost


class Level:
    def __init__(self, amountofenemies, numberofpowerups, levelnumber, font):

        # entity spawning
        self.playerlist = pygame.sprite.GroupSingle()
        self.enemylist = pygame.sprite.Group()
        self.boostlist = pygame.sprite.Group()
        self.bulletlist = pygame.sprite.Group()

        for i in range(amountofenemies):
            enemy = SimpleFollowEnemy("SimpleFollowEnemy" + str(i), "Enemy", random.randint(40, 800),
                                      random.randint(40, 800), font, random.randint(1, 3))
            print("Generated enemy" + str(i))
            self.enemylist.add(enemy)

        player = Player("Player0", "Player", random.randint(40, 800), random.randint(40, 800), font, 3)
        print("Player has been generated")
        self.playerlist.add(player)

        for i in range(numberofpowerups):
            which = random.randint(1, 100)
            if which <= 25:
                boost = HealthBoost("HealthBoost" + str(i), "Boost", random.randint(40, 800), random.randint(40, 800))
                print("Generated Healthboost" + str(i))
                self.boostlist.add(boost)
            else:
                boost = SpeedBoost("SpeedBoost" + str(i), "Boost", random.randint(40, 800), random.randint(40, 800))
                print("Generated Speedboost" + str(i))
                self.boostlist.add(boost)

        print("Level number " + levelnumber + " has been generated.")

    def update(self, screen, framecounter):

        # entity's in playerlist updater
        self.playerlist.update(self.bulletlist, framecounter)
        # entity's in enemylist updater
        self.enemylist.update(screen, self.playerlist)
        # entity's in boostlist updater
        self.boostlist.update(screen)
        # entity's in bulletlist updater
        self.bulletlist.update(screen)
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

        # bullet collision handler
        for i in self.bulletlist:

            collidingenemysprite = pygame.sprite.spritecollideany(i, self.enemylist)

            # enemy collision handling
            if collidingenemysprite is not None:
                i.attack(collidingenemysprite)
                i.kill()