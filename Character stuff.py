#Class for players
class Character:
    def __init__(self, name, hp, maxhp, defense, physDamage, specDamage, type, origin):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.defense = defense
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.type = type
        self.origin = origin

#class for enemy
class Enemy:
    def __init__(self, name, hp, maxhp, defense, physDamage, specDamage, type, origin):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.defense = defense
        self.physDamage = physDamage
        self.specDamage = specDamage
        self.type = type
        self.origin = origin


#Characters - L, E, J
pyro = Character("Pyro", 19, 19, 9, 2, 10, "Pyromaniac Mercenary", "Team Fortress 2")
goblin = Character("Goblin", 17, 22, 6, 1, 3, "Collector", "None")
construct = Character("Construct", 20, 20, 12, 4, 8, "Mage Robot", "Slay the Spire")

#Enemys - L, E, J
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
[] = Enemy()
