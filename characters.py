import time
import random
class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)


class Sorcerer(Character):
    magical = True
    strength = 10
    HP = 100
    health = HP
    mana = 75
    energy = mana
    damage = 0
    invisible = False
    speed = 0.25
    agility = speed
    coins = 0
    
    def __init__(self, name, magical = True, **kwargs):
        super().__init__(name, **kwargs)
        self.magical = magical
    def blast(self):
        if self.energy >= 10:
            print("Blasted!")
            self.damage = self.strength + random.randint(-5, 5)
            self.energy -= 10
        else:
            print("Not enough energy. The enemy lunges.")
    def fireball(self):
        if self.magical:
            if bool(random.randint(0, 1)) and self.energy >= 25:
                print("Your fireball succeeded!")
                self.damage = 4.5*self.strength + random.randint(-5, 5)
                self.energy -= 25
            else:
                print("Your fireball failed. You fall back.")
        else:
            print("You cannot make a fireball because you are not magical.")
    def invisibility(self):
        if self.energy >= 60 and self.magical:
            print("Activated invisibility")
            self.energy -= 60
            self.invisible = True
        else:
            print("You couldn't cast the invisibility spell.")
    def rest(self):
        time.sleep(5)
        self.energy+= 50
class Boss:
    damage = 0
    enough_energy = None
    other_energy = None
    def __init__(self, level,**kwargs):
        self.level = level
        self.attack = (level*2)+10
        self.health = (level*5)+50
        self.energy = 48 + 4*level
        self.coins = 125+(25*level)
        for key, value in kwargs.items():
            setattr(self, key, value)
    def smash(self):
        if self.energy >= 15:
            print("The boss smashes!")
            self.damage = self.attack + random.randint(-(self.level), self.level)
            self.energy -= 15
            self.enough_energy = True
        else:
            self.enough_energy = False
    def stomp(self):
        if self.energy >= 30:
            print("The boss mightily stomps!")
            self.damage = 2*(self.attack + random.randint(-(self.level), self.level))
            self.energy -= 30
            self.other_energy = True
        else:
            self.other_energy = False
    def rest(self):
        time.sleep(5)
        self.energy += 48 + 4*self.level      
            
    
class Warrior(Character):
    strong = True
    strength = 15
    HP = 120
    health = HP
    mana = 75
    energy = mana
    damage = 0
    invincible = False
    speed = 0.1
    agility = speed
    coins = 0
    def __init__(self, name,strong = True, **kwargs):
        super().__init__(name, **kwargs)
        self.strong = strong
    def jab(self):
        if self.energy >= 10:
            print("Sliced!")
            self.damage = self.strength + random.randint(-5, 5)
            self.energy -= 10
        else:
            print("You don't have enough energy. You wasted time.")
    def strike(self):
        if self.energy >= 25:
            print("The enemy was struck down!")
            self.damage = 2*self.strength + random.randint(-5, 5)
            self.energy -= 25
        else:
            print("You don't have enough energy. The enemy will counterattack.")
    def invincibility(self):
        if self.energy >= 50:
            print("Activated invisibility")
            self.energy -= 50
            self.invincibility = True
        else:
            print("You don't have enough energy. The enemy leaps forward.")
    def rest(self):
        time.sleep(5)
        self.energy+= 50
        
            