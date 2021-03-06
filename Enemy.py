import random
import Items

class Enemy:
    def __init__(self, name, hp, attack, defense, initiative, loot, gold, description, is_defeated):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.initiative = initiative
        self.loot = loot
        self.gold = gold
        self.description = description
        self.is_defeated = is_defeated

def enemy_gold():
    randomized_gold = random.randint(0, 30)
    return randomized_gold

def boss_gold():
    randomized_boss_gold = random.randint(50, 300)
    return randomized_boss_gold

def randomized_loot():
    dice_roll = random.randint(0, 20)
    if dice_roll > 10:
        randomized_loot_index = random.randint(0, (len(Items.item_loot_table) - 1))
        return Items.item_loot_table[randomized_loot_index]


#enemy list. HP, ATK, DEF, INI
skeleton = Enemy("Skeleton", 30, 12, 2, 2, randomized_loot(), enemy_gold(), "Spooky scary skeletons sends shivers down my spine.", False)
zombie = Enemy("Zombie", 25, 13, 3, 2, randomized_loot(), enemy_gold(), "A walking corpse.", False)
slime = Enemy("Slime", 20, 10, 1, 3, randomized_loot(), enemy_gold(), "A glob of monster liquid.", False)

def revive_monster():  #  to stop battle from autobattling
    if skeleton.is_defeated == True:
        skeleton.hp = 30
        skeleton.is_defeated = False
    elif zombie.is_defeated == True:
        zombie.hp = 25
        zombie.is_defeated = False
    elif slime.is_defeated == True:
        slime.hp = 20
        slime.is_defeated = False

#Boss list. TO DO: BOSS LOOT TABLE
balrog = Enemy("Balrog", 300, 50, 30, 3, randomized_loot(), boss_gold(), "A giant monster with two wings. I would run if I were you.", False)