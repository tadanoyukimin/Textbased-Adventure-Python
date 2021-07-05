import random
import items

class Enemy:
    def __init__(self, name, hp, attack, defense, loot, gold, description):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.loot = loot
        self.gold = gold
        self.description = description

def enemy_gold():
    randomized_gold = random.randint(0, 30)
    return randomized_gold

def boss_gold():
    randomized_boss_gold = random.randint(50, 300)
    return randomized_boss_gold

def randomized_loot():
    dice_roll = random.randint(0, 20)
    if dice_roll > 10:
        randomized_loot_index = random.randint(0, len(items.item_loot_table))
        return items.item_loot_table[randomized_loot_index]
    else:
        print("The enemy dropped nothing.")


#enemy list
skeleton = Enemy("Skeleton", 30, 5, 2, randomized_loot(), enemy_gold(), "Spooky scary skeletons sends shivers down my spine.")
zombie = Enemy("Zombie", 25, 5, 3, randomized_loot(), enemy_gold(), "A walking corpse.")
slime = Enemy("Slime", 20, 3, 1, randomized_loot(), enemy_gold())


#Boss list. TODO: BOSS LOOT TABLE
balrog = Enemy("Balrog", 300, 50, 30, randomized_loot(), boss_gold(), "A giant monster with two wings. I would run if I were you.")