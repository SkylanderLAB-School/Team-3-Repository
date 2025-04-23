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

import time
import random

#Character Class
class Character:
    def __init__(self, name,hpMax,hp,strength,magic,ac):
        self.name = name
        self.hpMax = hpMax
        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.ac = ac
    def dealDamage(self, amount):
        self.hp -= amount

#Enemy Class
class Enemy:
    def __init__(self, name,hpMax,hp,strength,magic,ac,magicRoll,strengthRoll,strengthStatus,magicStatus):
        self.name = name
        self.hpMax = hpMax
        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.ac = ac
        self.magicRoll = magicRoll
        self.strengthRoll = strengthRoll
        self.strengthStatus = strengthStatus
        self.magicStatus = magicStatus
    def dealDamage(self,amount):
        self.hp -= amount

#Weapon Class
class Weapon:
    def __init__(self, attackName,damageRoll,status):
        self.attackName = attackName
        self.damageRoll = damageRoll
        self.status = status

#Skill Class
class Skill:
    def __init__(self, attackName,damageRoll,status):
        self.attackName = attackName
        self.damageRoll = damageRoll
        self.status = status

#Variables
currentEnemy = None
currentCharacter = None
heldWeapon = None
skill = None
inCombat = False

#Characters
construct = Character("Construct",70,70,3,5,12)

#Enemies
owlBear = Enemy("Owl Bear",120,120,6,2,10,10,25,None,None)
enemyList = [owlBear]

#Weapons
sword = Weapon("Slash",15,None)

#Skills
burn = Skill("Burn",10,"burn")

#Combat
def chooseCharacter():
    global currentCharacter
    global skill
    global heldWeapon
    heldWeapon = sword
    characterChoice = int(input("Choose a character (1) Construct: "))
    if characterChoice == 1:
        currentCharacter = construct
        skill = burn
    else:
        chooseCharacter()

def showFightStats():
    global currentCharacter
    global currentEnemy
    print("Your hp: ",currentCharacter.hp,"/",currentCharacter.hpMax)
    print(currentEnemy.name, "hp: ", currentEnemy.hp, "/", currentEnemy.hpMax)

def checkDeath():
    global currentCharacter
    global currentCharacter
    if currentEnemy.hp < 1:
        inCombat = False
        print("You killed ",currentEnemy.name)
    if currentCharacter.hp < 1:
        print("You have died")
        exit(0)

#player actions
def playerAction():
    global currentCharacter
    global heldWeapon
    global skill
    print("(1) ",heldWeapon.attackName)
    print("(2) ",skill.attackName)
    action = input("Choose an action: ")
    if action == "1":
        playerWeaponAttack()
    elif action == "2":
        playerMagicAttack()
    else:
        playerAction()

def playerWeaponAttack():
    global currentCharacter
    global heldWeapon
    global currentEnemy
    dodgeRoll = random.randint(1,20)
    if dodgeRoll > currentEnemy.ac:
        damage = random.randint(1,heldWeapon.damageRoll) + currentCharacter.strength
        currentEnemy.dealDamage(damage)
        print("You deal ", damage, "damage")
    else:
        print("You miss")
    time.sleep(1)

def playerMagicAttack():
    global currentCharacter
    global skill
    global currentEnemy
    dodgeRoll = random.randint(1,20) + currentCharacter.magic
    if dodgeRoll > currentEnemy.ac:
        damage = random.randint(1,skill.damageRoll)
        currentEnemy.dealDamage(damage)
        print("You deal ", damage, "damage")
    else:
        print("You miss")
    time.sleep(1)

#enemy actions
def enemyActions():
    global currentEnemy
    global currentCharacter
    sOrM = random.randint(1,2)
    if sOrM == 1:
        enemyWeaponAttack()
    if sOrM == 2:
        enemyMagicAttack()

def enemyWeaponAttack():
    global currentCharacter
    global currentEnemy
    dodgeRoll = random.randint(1,20)
    if dodgeRoll > currentCharacter.ac:
        damage = random.randint(1,currentEnemy.strengthRoll) + currentEnemy.strength
        currentCharacter.dealDamage(damage)
        print(currentEnemy.name, " dealt ", damage, "damage")
    else:
        print(currentEnemy.name," missed")
    time.sleep(1)

def enemyMagicAttack():
    global currentCharacter
    global currentEnemy
    dodgeRoll = random.randint(1,20) + currentEnemy.magic
    if dodgeRoll > currentCharacter.ac:
        damage = random.randint(1,currentEnemy.magicRoll)
        currentCharacter.dealDamage(damage)
        print(currentEnemy.name," dealt ", damage, "damage")
    else:
        print(currentEnemy.name," missed")
    time.sleep(1)

#combat loop
def startCombat(enemyChoice):
    global currentCharacter
    global currentEnemy
    inCombat = True
    currentEnemy = enemyChoice
    print("You have encountered a ",currentEnemy.name)
    time.sleep(1)
    while inCombat == True:
        showFightStats()
        time.sleep(1)
        playerAction()
        enemyActions()
        checkDeath()
    currentEnemy = 0

chooseCharacter()
startCombat(owlBear)