from multiprocessing.sharedctypes import Value
import sys
from scenes import goblin_fight
#from p_project import *
#Terrance Suggestion Code
import random
#End Terrance Suggestion Code

class Enemy():
    def __init__(self):
        self.hp = random.randint(100, 200)
        self.attk = random.randint(10, 50)
        self.gold = random.randint(5, 10)


class GoblinEnemy(Enemy):

    def __init__(self):
        super().__init__()
        self.hp = random.randint(40, 65)
        self.attk = random.randint(12, 15)
        self.gold = random.randint(5, 8)


class OrcEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = random.randint(400, 500)
        self.attk = random.randint(40, 60)
        self.gold = random.randint(50, 55)

class SpiderEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = random.randint(100, 200)
        self.attk = random.randint(15, 20)
        self.gold = random.randint(15, 18)

class SkeletonEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = random.randint(40, 50)
        self.attk = random.randint(15, 18)
        self.gold = random.randint(8, 12)

class ElderDragonEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = random.randint(1000,1200)
        self.attk = random.randint(100, 120)
        self.gold = random.randint(5000, 6000)

goblin = GoblinEnemy()

orc = OrcEnemy()

giant_spider = SpiderEnemy()

skeleton = SkeletonEnemy()

elder_dragon = ElderDragonEnemy()

monstersA = [goblin , skeleton]
monstersB = [orc, giant_spider]
BossesA = [elder_dragon]

#Terrance Suggestion Code
ultimate_list = [monstersA, monstersB, BossesA]
print(ultimate_list[0][0])
#End Terrance Suggestion Code

my_health = 1000
my_attk = 10

alive = True


def status(x):
    if x == False:
        print("The light starts slowly going away as you close your eyes for the final time.....")
        sys.exit()
    else:
        print("something went wrong")

def test(a, b, c, d, e):
    print("Enemy Health: ", c)
    print("Enemy Attack: ", d)

    while True: 
        playerchoice = input("press 1 to continue: ")
        if playerchoice == "1":
            print("""
        ========================================================================
        |                           Battle Menu                                |
        |______________________________________________________________________|""")
            print("Your Health: ", a)
            print("[Option 1] Attack for ", b, "hit points.")
            print("[Option 2] Use Skill")
            playerchoice = input("Choose an Option: ")

            if playerchoice == "1" and c > 0:
                c = c - b
                print("you swing at the monster for ", b, "damage!")
                print("Monsters Health: ", c)

            if playerchoice == "1" and c <= 0:
                print("the Monster is dead")
                #monster dies end game

            if playerchoice == "1" and c > 0:
                a = a - d
                print("The monster Swings back at you for ", d, "health!")
                print("Your health: ", a)
                if a <= 0 and c >= 0:
                    e = False
                    status(e)

            else:
                print("Please choose a valid option")


        else:
            print("please choose a valid option")

#gob_b()
#print statements are here for testing reasons remove before final stages
#for testing reasons my_hp & my_damage are put as temporary my_health & my_atttack as that code has no value unless its in Pproject 


# Take this code for the monster encounters 
'''
    print(Scene())
    print("You have encountered a monster!")
    print("""
    =========================================================================
    |                    You have encountered a Monster!                    |
    |_______________________________________________________________________|""")'''
