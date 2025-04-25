import time
import random

#Character Class
class Character:
    def __init__(self, name,hpMax,hp,strength,magic,ac,currentStatus,statusLevel):
        self.name = name
        self.hpMax = hpMax
        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.ac = ac
        self.currentStatus = currentStatus
        self.statusLevel = statusLevel
    def dealDamage(self, amount):
        self.hp -= amount
    def maxHeal(self):
        self.hp = self.hpMax
    def burn(self):
        self.hp -= self.statusLevel
        print("You were burned for ", self.statusLevel, "damage")
        self.statusLevel -= self.strength
        if self.statusLevel < 1:
            print("You no longer burned")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)
    def poison(self):
        self.hp -= self.statusLevel
        print("You were poisoned for ", self.statusLevel, "damage")
        self.statusLevel -= self.magic
        if self.statusLevel < 1:
            print("You no longer poisoned")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)
    def bleed(self):
        self.hp -= self.statusLevel
        print("You bleed ", self.statusLevel, "damage")
        self.statusLevel -= 1
        if self.statusLevel < 1:
            print("You no longer bleeding")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)


#Enemy Class
class Enemy:
    def __init__(self, name,hpMax,hp,strength,magic,ac,magicRoll,strengthRoll,strengthStatus,magicStatus,currentStatus,statusLevel):
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
        self.currentStatus = currentStatus
        self.statusLevel = statusLevel
    def dealDamage(self,amount):
        self.hp -= amount
    def burn(self):
        self.hp -= self.statusLevel
        print(self.name, "was burned for ", self.statusLevel, "damage")
        self.statusLevel -= self.strength
        if self.statusLevel < 1:
            print(self.name,"is no longer burned")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)
    def poison(self):
        self.hp -= self.statusLevel
        print(self.name, "was poisoned for ", self.statusLevel, "damage")
        self.statusLevel -= self.magic
        if self.statusLevel < 1:
            print(self.name,"is no longer poisoned")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)
    def bleed(self):
        self.hp -= self.statusLevel
        print(self.name, " bleed for ", self.statusLevel, " damage")
        self.statusLevel -= 1
        if self.statusLevel < 1:
            print(self.name,"is no longer bleeding")
            self.statusLevel = 0
            self.currentStatus = None
        time.sleep(1)

#Weapon Class
class Weapon:
    def __init__(self, attackName,damageRoll,status,name):
        self.attackName = attackName
        self.damageRoll = damageRoll
        self.status = status
        self.name = name

#Skill Class
class Skill:
    def __init__(self, attackName,damageRoll,status,name):
        self.attackName = attackName
        self.damageRoll = damageRoll
        self.status = status
        self.name = name

#Variables
currentEnemy = None
currentCharacter = None
heldWeapon = None
skill = None
inCombat = False

#Characters
construct = Character("Construct",75,75,3,5,12,None,None)
pyro = Character("Pyro",70,70,5,3,11,None,None)
goblin = Character("Goblin",65,65,4,4,9,None,None)

#Enemies
wizard = Enemy("Wizard",50,50,2,6,9,10,6,None,"burn",None,None)
golem = Enemy("Golem",100,100,6,1,13,5,20,None,None,None,None)
asj = Enemy("Arkeyan Shield Juggernaught",90,90,6,2,14,10,15,None,None,None,None)
dragon = Enemy("AGHEEL THE GREAT FLYING DRAGON!!!",200,200,5,5,13,15,20,None,"burn",None,None)
enemyList = [wizard,golem,asj,dragon]

#Weapons
sword = Weapon("Sword Slash",15,None,"Sword")
fireAxe = Weapon("Axe Swing",20,None,"Fire Axe")
dagger = Weapon("Dagger Stab",8,None,"Dagger")

#Skills
electrify = Skill("Electric Shock",20,"shock","Electrify")
fireBlast = Skill("Fire Blast",5,"burn","Fire Blast")
poisonPotion = Skill("Poison Potion",5,"poison","Poison Potion")

#Combat
def chooseCharacter():
    global currentCharacter
    global skill
    global heldWeapon
    characterChoice = int(input("Choose a character (1)Construct (2)Pyro (3)Goblin : "))
    if characterChoice == 1:
        currentCharacter = construct
        skill = electrify
        heldWeapon = sword
    elif characterChoice == 2:
        currentCharacter = pyro
        skill = fireBlast
        heldWeapon = fireAxe
    elif characterChoice == 3:
        currentCharacter = goblin
        skill = daggerThrow
        heldWeapon = dagger
    else:
        chooseCharacter()

def showFightStats():
    global currentCharacter
    global currentEnemy
    print("Your hp: ",currentCharacter.hp,"/",currentCharacter.hpMax)
    print(currentEnemy.name, "hp: ", currentEnemy.hp, "/", currentEnemy.hpMax)

def checkDeath():
    global currentCharacter
    global currentEnemy
    global inCombat
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
        if currentCharacter.currentStatus == "shock":
            damage = round(damage * 0.5)
            print("You are shocked")
            currentCharacter.statusLevel -= 1
            if currentCharacter.statusLevel < 1:
                print("You no longer shocked")
                currentCharacter.statusLevel = 0
                currentCharacter.currentStatus = None
            time.sleep(1)
        currentEnemy.dealDamage(damage)
        print("You deal ", damage, "damage")
        if heldWeapon.status == "burn":
            currentEnemy.currentStatus = "burn"
            currentEnemy.statusLevel = 10
            print("You inflict Burn")
            time.sleep(1)
        if heldWeapon.status == "poison":
            currentEnemy.currentStatus = "poison"
            currentEnemy.statusLevel = 10
            print("You inflict Poison")
            time.sleep(1)
        if heldWeapon.status == "bleed":
            currentEnemy.currentStatus = "bleed"
            currentEnemy.statusLevel = 5
            print("You inflict Bleed")
            time.sleep(1)
        if heldWeapon.status == "shock":
            currentEnemy.currentStatus = "shock"
            currentEnemy.statusLevel = 3
            print("You inflict Shock")
            time.sleep(1)
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
        if currentCharacter.currentStatus == "shock":
            damage = round(damage * 0.5)
            print("You are shocked")
            currentCharacter.statusLevel -= 1
            if currentCharacter.statusLevel < 1:
                print("You no longer shocked")
                currentCharacter.statusLevel = 0
                currentCharacter.currentStatus = None
            time.sleep(1)
        currentEnemy.dealDamage(damage)
        print("You deal ", damage, "damage")
        if skill.status == "burn":
            currentEnemy.currentStatus = "burn"
            currentEnemy.statusLevel = 10
            print("You inflict Burn")
            time.sleep(1)
        if skill.status == "poison":
            currentEnemy.currentStatus = "poison"
            currentEnemy.statusLevel = 10
            print("You inflict Poison")
            time.sleep(1)
        if skill.status == "bleed":
            currentEnemy.currentStatus = "bleed"
            currentEnemy.statusLevel = 5
            print("You inflict Bleed")
            time.sleep(1)
        if skill.status == "shock":
            currentEnemy.currentStatus = "shock"
            currentEnemy.statusLevel = 3
            print("You inflict Shock")
            time.sleep(1)
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
        if currentEnemy.currentStatus == "shock":
            damage = round(damage * 0.5)
            print(currentEnemy.name," is shocked")
            currentEnemy.statusLevel -= 1
            if currentEnemy.statusLevel < 1:
                print(currentEnemy.name," is no longer shocked")
                currentEnemy.statusLevel = 0
                currentEnemy.currentStatus = None
            time.sleep(1)
        currentCharacter.dealDamage(damage)
        print(currentEnemy.name, " dealt ", damage, " melee damage")
        if currentEnemy.strengthStatus == "burn":
            currentCharacter.currentStatus = "burn"
            currentCharacter.statusLevel = 10
            print(currentEnemy.name," inflicts Burn")
            time.sleep(1)
        if currentEnemy.strengthStatus == "poison":
            currentCharacter.currentStatus = "poison"
            currentCharacter.statusLevel = 10
            print(currentEnemy.name," inflicts Poison")
            time.sleep(1)
        if currentEnemy.strengthStatus == "bleed":
            currentCharacter.currentStatus = "bleed"
            currentCharacter.statusLevel = 5
            print(currentEnemy.name," inflicts Bleed")
            time.sleep(1)
        if currentEnemy.strengthStatus == "shock":
            currentCharacter.currentStatus = "shock"
            currentCharacter.statusLevel = 3
            print(currentEnemy.name," inflicts Shock")
            time.sleep(1)
    else:
        print(currentEnemy.name," missed")
    time.sleep(1)

def enemyMagicAttack():
    global currentCharacter
    global currentEnemy
    dodgeRoll = random.randint(1,20) + currentEnemy.magic
    if dodgeRoll > currentCharacter.ac:
        damage = random.randint(1,currentEnemy.magicRoll)
        if currentEnemy.currentStatus == "shock":
            damage = round(damage * 0.5)
            print(currentEnemy.name," is shocked")
            currentEnemy.statusLevel -= 1
            if currentEnemy.statusLevel < 1:
                print(currentEnemy.name," is no longer shocked")
                currentEnemy.statusLevel = 0
                currentEnemy.currentStatus = None
            time.sleep(1)
        currentCharacter.dealDamage(damage)
        print(currentEnemy.name," dealt ", damage, " magic damage")
        if currentEnemy.magicStatus == "burn":
            currentCharacter.currentStatus = "burn"
            currentCharacter.statusLevel = 10
            print(currentEnemy.name," inflicts Burn")
            time.sleep(1)
        if currentEnemy.magicStatus == "poison":
            currentCharacter.currentStatus = "poison"
            currentCharacter.statusLevel = 10
            print(currentEnemy.name," inflicts Poison")
            time.sleep(1)
        if currentEnemy.magicStatus == "bleed":
            currentCharacter.currentStatus = "bleed"
            currentCharacter.statusLevel = 5
            print(currentEnemy.name," inflicts Bleed")
            time.sleep(1)
        if currentEnemy.magicStatus == "shock":
            currentCharacter.currentStatus = "shock"
            currentCharacter.statusLevel = 3
            print(currentEnemy.name," inflicts Shock")
            time.sleep(1)
    else:
        print(currentEnemy.name," missed")
    time.sleep(1)

#combat loop
def startCombat(enemyChoice):
    global currentCharacter
    global currentEnemy
    global inCombat
    inCombat = True
    currentEnemy = enemyChoice
    print("You have encountered a ",currentEnemy.name)
    time.sleep(1)
    while inCombat == True:
        showFightStats()
        time.sleep(1)
        playerAction()
        checkStatusPlayer()
        enemyActions()
        checkStatusEnemy()
        checkDeath()
    currentEnemy = 0

#status check
def checkStatusPlayer():
    global currentCharacter
    global currentEnemy
    if currentCharacter.currentStatus != None:
        if currentCharacter.currentStatus == "burn":
            currentCharacter.burn()
        if currentCharacter.currentStatus == "poison":
            currentCharacter.poison()
        if currentCharacter.currentStatus == "bleed":
            currentCharacter.bleed()

def checkStatusEnemy():
    global currentCharacter
    global currentEnemy
    if currentEnemy.currentStatus != None:
        if currentEnemy.currentStatus == "burn":
            currentEnemy.burn()
        if currentEnemy.currentStatus == "poison":
            currentEnemy.poison()
        if currentEnemy.currentStatus == "bleed":
            currentEnemy.bleed()

chooseCharacter()
startCombat(wizard)
currentCharacter.hp = currentCharacter.hpMax
time.sleep(3)
startCombat(golem)
currentCharacter.hp = currentCharacter.hpMax
time.sleep(3)
startCombat(asj)
currentCharacter.hp = currentCharacter.hpMax
time.sleep(3)
startCombat(dragon)
