#Class for players
class Character:
    def __init__(self, name, hp, maxhp, ac, strength, magic, type, origin):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.ac = ac
        self.strength = strength
        self.magic = magic
        self.type = type
        self.origin = origin

#class for enemy
class Enemy:
    def __init__(self, name, hp, maxhp, ac, strength, magic, type, origin):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.ac = ac
        self.strength = strength
        self.magic = magic
        self.type = type
        self.origin = origin

#Characters - L, E, J
pyro = Character("Pyro", 19, 19, 9, 2, 10, "Pyromaniac Mercenary", "Team Fortress 2")
gob = Character("Goblin", 17, 22, 6, 1, 3, "Collector", "None")
const = Character("Construct", 20, 20, 12, 4, 8, "Mage Robot", "Slay the Spire")

#Enemys - L, E, J
asj = Enemy("Arkeyan Shield Juggernaught", 25, 25, 15, 2, 12, "Ancient Defense Robot", "Skylanders")
b33 = Enemy("Heavy Drone B-33", 55, 55, 1, 6, 4, "MECHA BEE DESTROYER BLASTLORD", "Bug Fables")
wizrd = Enemy("Wizzard", 30, 32, 30, 12, 18, "Warrior", "N/a")
drgon = Enemy("Agheel", 200, 250, 60, 90, 33, "Dragon", "Elden Ring")
Golm = Enemy("Golem", 100, 100, 13, 6, 2, "Tank", "Somewhere")
krkn = Enemy("Kraken", 200, 200, 12, 4, 5, "Big Squid boi", "The Ocean")
#[] = Enemy()
#[] = Enemy()wow
#[] = Enemy()
