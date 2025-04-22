import random
import time


#character class
class Character:
    def __init__(self,maxhp,hp,strength,wisdom,defense):
        self.maxhp = maxhp
        self.hp = hp
        self.strength = strength
        self.wisdom = wisdom
        self.defense = defense


#weapon class
weapon = 0
class Weapon:
    def __init__(self,name,Damage,Status):
        self.name = name
        self.Damage = Damage
        self.Status = Status

#skill class
skill = 0
class Skill:
    def __init__(self,name,Damage,Status):
        self.name = name
        self.Damage = Damage
        self.Status = Status

#weapon list
sword = Weapon("Sword Slash",4,0)
magicBolt = Skill("Magic Bolt",6,0)
#enemy class
class Enemy:
    def __init__(self,name,maxhp,hp,strength,wisdom,defense):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.strength = strength
        self.wisdom = wisdom
        self.defense = defense

currentEnemy = 0

#list of enemies
slime = Enemy("Slime",15,15,4,6,10)
enemies = [slime]

#combat
player = Character(20,20,6,6,10)
weapon = sword
inCombat = True

def chooseEnemy():
    global enemies
    global currentEnemy
    enemyRandom = random.choice(enemies)
    currentEnemy = enemyRandom

def showStats():
    global currentEnemy
    print("Player HP:",player.hp,"/",player.maxhp)
    print(currentEnemy.name,"HP:",currentEnemy.hp,"/",currentEnemy.maxhp)

def playerWeapon():
    global currentEnemy
    global weapon
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,weapon.Damage) + player.strength
    if defRoll > currentEnemy.defense:
        currentEnemy.hp -= damageRoll
        print("You dealt ",damageRoll,"damage")
    else:
        print("You didn't hit")
    time.sleep(1)

def playerSkill():
    global currentEnemy
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,weapon.Damage) + player.wisdom
    if defRoll > currentEnemy.defense:
        currentEnemy.hp -= damageRoll
        print("You dealt ",damageRoll,"damage")
    else:
        print("You didn't hit")
    time.sleep(1)

def playerAction():
    global skill
    global weapon
    try:
        action = int(input("(1)",weapon.name,"(2)",skill.name,":"))
    except:
        print("Not Valid Option")
        playerAction()
    if action == 1:
        playerWeapon()
    if action == 2:
        playerSkill()

def enemyPhys():
    global currentEnemy
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,currentEnemy.strength)
    if defRoll > player.defense:
        player.hp -= damageRoll
        print(currentEnemy.name," dealt ",damageRoll,"damage")
    else:
        print(currentEnemy.name," didn't hit")
    time.sleep(1)

def enemySpec():
    global currentEnemy
    defRoll = random.randint(1,20)
    damageRoll = random.randint(1,currentEnemy.wisdom)
    if defRoll > player.defense:
        player.hp -= damageRoll
        print(currentEnemy.name," dealt ",damageRoll,"damage")
    else:
        print(currentEnemy.name," didn't hit")
    time.sleep(1)

def enemyAction():
    global currentEnemy
    pOrS = ["p","s"]
    pSRandom = random.choice(pOrS)
    if pSRandom == "p":
        enemyPhys()
    if pSRandom == "s":
        enemySpec()

def checkDeath():
    global currentEnemy
    global inCombat
    if currentEnemy.hp < 1:
        inCombat = False
        print(currentEnemy.name,"has died")
    if player.hp < 1:
        inCombat = False
        print("You have died")

def goInCombat():
    global inCombat
    inCombat = True
    chooseEnemy()
    while inCombat == True:
        showStats()
        playerAction()
        checkDeath()
        enemyAction()
        checkDeath()
    currentEnemy = 0

goInCombat()
