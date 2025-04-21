import random
import time


#character class
class Character:
    def __init__(self,maxhp,hp,physDamage,specDamage,defense):
        self.maxhp = maxhp
        self.hp = hp
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.defense = defense
player = Character(20,20,6,6,10)
#enemy class
class Enemy:
    def __init__(self,name,maxhp,hp,physDamage,specDamage,defense):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.defense = defense

currentEnemy = 0
#list of enemies
slime = Enemy("Slime",15,15,4,6,10)
enemies = [slime]

#combat
#choose enemy
def chooseEnemy():
    global enemies
    global currentEnemy
    enemyRandom = random.choice(enemies)
    currentEnemy = enemyRandom

def showStats():
    global currentEnemy
    print("Player HP:",player.hp,"/",player.maxhp)
    print(currentEnemy.name,"HP:",currentEnemy.hp,"/",currentEnemy.maxhp)

def playerPhys():
    global currentEnemy
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,player.physDamage)
    if defRoll > currentEnemy.defense:
        currentEnemy.hp -= damageRoll
        print("You dealt ",damageRoll,"damage")
    else:
        print("You didn't hit")

def playerSpec():
    global currentEnemy
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,player.specDamage)
    if defRoll > currentEnemy.defense:
        currentEnemy.hp -= damageRoll
        print("You dealt ",damageRoll,"damage")
    else:
        print("You didn't hit")

def playerAction():
    try:
        action = int(input("(1) Strike (2) Spell:"))
    except:
        print("Not Valid Option")
        playerAction()
    if action == 1:
        playerPhys()
    if action == 2:
        playerSpec()

chooseEnemy()
showStats()
playerAction()
showStats()