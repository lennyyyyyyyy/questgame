import time
import random
from characters import Character, Sorcerer, Warrior, Boss
def sorcererBattle(player,level):
    enemy = Boss(level)
    print(f"You are up against a level {level} boss. Good luck!\n")
    print(f"You currently have {player.mana} energy.\n")
    counter = 0
    while player.health > 0:
        attack = input("Would you like to blast (10 energy), use fireball (30 energy), rest (gives 50 energy), or use invisibility (60 energy)? ")
        if attack == 'blast':
            player.blast()
            print(f"That did {player.damage} damage!\n")
            print(f"You now have {player.energy} energy left.\n")
            enemy.health -= player.damage
            print(f"The boss has {enemy.health} HP left.\n")
            player.damage = 0
        elif attack == 'fireball':
            player.fireball()
            print(f"That did {player.damage} damage!\n")
            print(f"You now have {player.energy} energy left.\n")
            enemy.health -= player.damage
            print(f"The boss has {enemy.health} HP left.\n")
            player.damage = 0
        elif attack == 'rest':
            player.rest()
            print("Ah! You're awake!")
            print(f"\nYou now have {player.energy} energy left.\n")
        elif attack == 'invisibility':
            player.invisibility()
            print("You are now invisible for 2 turns.\n")
            print(f"You have {player.energy} energy left.\n")
            player.agility = 1
        if player.invisible:
            counter+= 1
        if counter == 2:
            print("You are no longer invisible.\n")
            player.invisible = False
            player.agility = player.speed
            counter = 0
        time.sleep(1)
        boss_attack = random.randint(0, 1)
        if enemy.health < 0:
            print(f"\nCongratulations {player.name}! You defeated the boss!\n")
            player.coins += enemy.coins
            print(f"You earned {enemy.coins} coins!\n")
            break
        while True:
            if boss_attack:
                enemy.smash()
                if enemy.enough_energy:
                    if random.random() < player.agility:
                        time.sleep(1)
                        print("But he misses!\n")
                    else:
                        time.sleep(1)
                        print(f"That did {enemy.damage} damage!\n")
                        player.health -= enemy.damage
                        time.sleep(1)
                        print(f"You have {player.health} HP left.\n")
                    enemy.damage = 0
                    enemy.enough_energy = None
                    break
                elif not enemy.enough_energy:
                    enemy.enough_energy = None
                    boss_attack = 0
            if not boss_attack:
                enemy.stomp()
                if enemy.other_energy:
                    if random.random() < player.agility:
                        time.sleep(1)
                        print("But he misses!\n")
                    else:
                        time.sleep(1)
                        print(f"That did {enemy.damage} damage!\n")
                        player.health -= enemy.damage
                        time.sleep(1)
                        print(f"You have {player.health} HP left.\n")
                    enemy.damage = 0
                    enemy.other_energy = None
                    break
                elif not enemy.other_energy:
                    enemy.other_energy = None
                    boss_attack = 1
            if enemy.energy < 15:
                enemy.rest()
                print("The boss takes a rest.\n")
                break
    if player.health<= 0:
        print("You have died. Game over.\n")
        win = 0
def warriorBattle(player,level):
    enemy = Boss(level)
    print(f"You are up against a level {level} boss. Good luck!\n")
    print(f"You currently have {player.mana} energy.\n")
    counter = 0
    while player.health > 0:
        attack = input("Would you like to jab (10 energy), use strike (25 energy), rest (gives 50 energy), or use invincibility (50 energy)? ")
        if attack == 'jab':
            player.jab()
            print(f"That did {player.damage} damage!\n")
            print(f"You now have {player.energy} energy left.\n")
            enemy.health -= player.damage
            print(f"The boss has {enemy.health} HP left.\n")
            player.damage = 0
        elif attack == 'strike':
            player.strike()
            print(f"That did {player.damage} damage!\n")
            print(f"You now have {player.energy} energy left.\n")
            enemy.health -= player.damage
            print(f"The boss has {enemy.health} HP left.\n")
            player.damage = 0
        elif attack == 'rest':
            player.rest()
            print("Ah! You're awake!\n")
            print(f"You now have {player.energy} energy left.\n")
        elif attack == 'invincibility':
            player.invincibility()
            print("You now have a 75% damage reduction for 2 turns.\n")
            print(f"You have {player.energy} energy left\n")
        if player.invincible:
            counter+= 1
        if counter == 2:
            player.invincible = False
            counter = 0
        time.sleep(1)
        boss_attack = random.randint(0, 1)
        if enemy.health < 0:
            print(f"\nCongratulations {player.name}! You defeated the boss!\n")
            player.coins += enemy.coins
            print(f"You earned {enemy.coins} coins!\n")
            break
        while True:
            if boss_attack:
                enemy.smash()
                if enemy.enough_energy:
                    if random.random() < player.agility:
                        time.sleep(1)
                        print("But he misses!\n")
                    else:
                        time.sleep(1)
                        if player.invincible:
                            print(f"That only did {enemy.damage * 0.25} damage!\n")
                            player.health -= (enemy.damage * 0.25)
                            time.sleep(1)
                            print(f"You have {player.health} HP left.\n")
                        else:
                            print(f"That did {enemy.damage} damage!\n")
                            player.health -= enemy.damage
                            time.sleep(1)
                            print(f"You have {player.health} HP left.\n")
                    enemy.damage = 0
                    enemy.enough_energy = None
                    break
                elif not enemy.enough_energy:
                    enemy.enough_energy = None
                    boss_attack = 0
            if not boss_attack:
                enemy.stomp()
                if enemy.other_energy:
                    if random.random() < player.agility:
                        time.sleep(1)
                        print("But he misses!\n")
                    else:
                        time.sleep(1)
                        if player.invincible:
                            print(f"That only did {enemy.damage * 0.25} damage!\n")
                            player.health -= (enemy.damage * 0.25)
                            time.sleep(1)
                            print(f"You have {player.health} HP left.\n")
                        else:
                            print(f"That did {enemy.damage} damage!\n")
                            player.health -= enemy.damage
                            time.sleep(1)
                            print(f"You have {player.health} HP left.\n")
                    enemy.damage = 0
                    enemy.other_energy = None
                    break
                elif not enemy.other_energy:
                    enemy.other_energy = None
                    boss_attack = 1
            if enemy.energy < 15:
                enemy.rest()
                print("The boss takes a rest.\n")
                break
    if player.health <= 0:
        print("You have died. Game over.\n")
        win = 0
print("Welcome to the game of the quest of awesomeness!")
time.sleep(1)
print("You can be a sorcerer or a warrior.")
time.sleep(1)                
print("""
Beginning Sorcerer Stats:                            Beginning Warrior Stats:
100 health                                           120 health
75 starting energy                                   75 starting energy
25% dodge rate                                       10% dodge rate
Moves:                                               Moves:
Blast -10 energy, 5-15dmg                            Jab -10 energy, 10-20dmg
Fireball -30 energy, 50-60dmg, 50% chance of success Strike -25energy, 25-35dmg
Invisibility -60 energy, invisible for 2 turns       Invincibility -50 energy, 75% damage reduction for 2 turns
Rest -uses a turn but gives 50 energy                Rest -uses a turn but gives 50 energy""")
time.sleep(5)               
choice = input("\nWhat is your name? ")
char = input(f"\nWhat would you like to be {choice}? sorcerer or warrior? ")
if char == 'sorcerer':                
    character = Sorcerer(choice)
else:
    character = Warrior(choice)
print("\nEvery level, you will have to defeat a boss.")
time.sleep(1)                
print("You will get coins for defeating bosses, and a shop will appear when you have enough money for an upgrade.")
time.sleep(1)
print("You're health and energy will also reset after every level. The bosses also get harder after each level.")
healthCost = 1000
energyCost = 1000
damageCost = 1000
level = 1
win = 1
while win:
    if char == 'sorcerer':
        sorcererBattle(character, level)
    else:
        warriorBattle(character, level)
    if character.health <= 0:
        break
    level +=1
    character.health = character.HP
    character.energy = character.mana
    enterCharge = min(healthCost, energyCost, damageCost)
    if character.coins >= enterCharge:
        print("Welcome to the shop!\n")
        while True:
            print(f"""     You have: {character.coins} coins
 -Upgrade Health - {healthCost} coins
 increases health by 15 HP
 -Upgrade Energy - {energyCost} coins
 increases energy by 15 mana
 -Upgrade Damage - {damageCost} coins
 increases damage by 10 dmg""")
            upgrade = input("Would you like to upgrade health, energy, damage, or just pass? ")
            if upgrade == 'pass':
                print("Ok then, have a good day!")
                break
            else:
                if upgrade == 'health':
                    if character.coins >= healthCost:
                        print("Cha-Ching!")
                        character.HP += 15
                        character.coins -= healthCost
                        healthCost += 250
                    else:
                        print("You don't have enough coins. Try again.")
                        continue
                elif upgrade == 'damage':
                    if character.coins >= damageCost:
                        print("Cha-Ching!")
                        character.strength += 10
                        character.coins -= damageCost
                        damageCost += 250
                    else:
                        print("You don't have enough coins. Try again.")
                        continue
                elif upgrade == 'energy':
                    if character.coins >= energyCost:
                        print("Cha-Ching!")
                        character.mana += 15
                        character.coins -= energyCost
                        energyCost += 250
                    else:
                        print("You don't have enough coins. Try again.")
                        continue
                time.sleep(1)
                print("Here are your stats now:")
                time.sleep(1.5)
                if char == 'sorcerer':
                    print(f"""
                    Your Stats: 
                    {character.HP} health   
                    {character.mana} starting energy                                  
                    25% dodge rate                                     
                    Moves:                                             
                    Blast -10 energy, {character.strength-5}-{character.strength + 5}dmg                         
                    Fireball -25 energy, {4.5*character.strength - 5}-{4.5*character.strength + 5}dmg, 50% chance of success 
                    Invisibility -60 energy, invisible for 2 turns     
                    Rest -uses a turn but gives 50 energy""")
                elif char == 'warrior':
                    print(f"""
                    Your Stats:
                    {character.HP} health
                    {character.mana} starting energy
                    10% dodge rate
                    Moves:
                    Jab -10 energy, {character.strength-5}-{character.strength + 5}dmg
                    Strike -25energy, {2*character.strength-5}-{2*character.strength + 5}dmg
                    Invincibility -50 energy, 75% damage reduction for 2 turns
                    Rest -uses a turn but gives 50 energy""")
                if character.coins > enterCharge:
                    print("You have enough gold to upgrade again.")
                    continue
                else:
                    print("See you again soon!")
                    break
    
    
        
            
