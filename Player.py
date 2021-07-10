import Items
import copy
import DungeonMap
import numpy as np
import random

class Player():
    def __init__(self, name, player, hp, mp, attack, defense, initiative):
        self.name = name
        self.player = player
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.initiative = initiative
        self.inventory = []
        self.equipment = {
            "Weapon": None,
            "Shield": None,
            "Armor": None
        }
        self.gold = 0
        self.floor = 0
        self.position = 0

    def loot_item(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        if len(self.inventory) == 0:
            print("There is nothing in your inventory.")
        else:
            print("This is your inventory.")
            print("------------------------")
            print(f"{self.inventory}")

    def check_equipment(self):
        print("This is your equipment.")
        print("------------------------")
        print(f"{self.equipment}")

#  Player action? 
    def move(self):
        current_position = DungeonMap.dungeon_map_second[self.floor][self.position]
        #  This refers to [[0, 1, 2,]], [[0]]
        #  self.position should refer to the index within the nested list, not the nested list itself.
        if self.position == 2:
            self.floor += 1
            self.position = 0 
        else:
            self.position += 1

    def check_map(self):
        current_position = DungeonMap.dungeon_map_second[self.floor][self.position]
        print(f"Your current position is {current_position}.")
        map_copy = copy.copy(DungeonMap.dungeon_map_second)
        return f"The map is \n{map_copy}."

def equip_item():  # [0] = Name, [1] = Item Category, [2] = Item description, [3] = Attack/Defense, [4] = Value
    player_answer = input("What item do you want to equip?> ").title()
    for equipment in player_character.inventory:
        try:
            if player_answer == equipment:
                if Items.dict_item_stats[equipment][1] == "Weapon":
                    if player_character.equipment["Weapon"] is None:
                        player_character.equipment["Weapon"] = equipment
                        player_character.inventory.pop(0)

                    elif player_character.equipment["Weapon"]:
                        player_character.inventory.append(player_character["Weapon"])
                        player_character.equipment["Weapon"] = equipment
                        player_character.inventory.pop(-1)

                    player_character.attack += Items.dict_item_stats[equipment][3]
                    print(f"You have equipped a {equipment}.")

                if Items.dict_item_stats[equipment][1] == "Shield":
                    if player_character.equipment["Shield"] is None:
                        player_character.equipment["Shield"] = equipment
                        player_character.inventory.pop(0)

                    elif player_character.equipment["Shield"]:
                        player_character.inventory.append(player_character["Shield"])
                        player_character.equipment["Shield"] = equipment
                        player_character.inventory.pop(-1)

                    player_character.defense += Items.dict_item_stats[equipment][3]
                    print(f"You have equipped a {equipment}.")

                if Items.dict_item_stats[equipment][1] == "Armor":

                    if player_character.equipment["Armor"] is None:
                        player_character.equipment["Armor"] = equipment
                        player_character.inventory.pop(0)

                    elif player_character.equipment["Armor"]:
                        player_character.inventory.append(player_character["Armor"])
                        player_character.equipment["Armor"] = equipment
                        player_character.inventory.pop(-1)

                    player_character.defense += Items.dict_item_stats[equipment][3]
                    print(f"You have equipped a {equipment}.")

        except AttributeError:
            return f"You failed to equip {equipment}."   

def unequip_item():
    print("This is your equipment.")
    print(player_character.equipment)
    equipped_item = input("What do you want to unequip? (Please specify item name.)\n> ").title()

    if equipped_item == player_character.equipment["Weapon"]:
        player_character.attack -= Items.dict_item_stats[equipped_item][3]
        player_character.inventory.append(equipped_item)
        player_character.equipment["Weapon"] = None

    elif equipped_item == player_character.equipment["Shield"]:
        player_character.defense -= Items.dict_item_stats[equipped_item][3]
        player_character.inventory.append(equipped_item)
        player_character.equipment["Shield"] = None

    elif equipped_item == player_character.equipment["Armor"]:
        player_character.defense -= Items.dict_item_stats[equipped_item][3]
        player_character.inventory.append(equipped_item)
        player_character.equipment["Armor"] = None

    else: pass

   
#class resources. Always HP, MP, ATK, DEF, INITIATIVE
classlist = ["Knight", "Spellcaster", "Ranger"]
knight_stats = [20, 10, 4, 8, 3]
spellcaster_stats = [15, 30, 8, 4, 3]
ranger_stats = [18, 15, 6, 7, 5]

def character_creation():
    player_stats = [0, 0, 0, 0, 0]  #HP, MP, ATK, DEF, INITIATIVE
    player_name = input("UNKNOWN VOICE: Please enter your name...:\n")

    if player_name.strip() == "":
        player_name = "Anonymous"

    print("UNKNOWN VOICE: Choose a class...\nKnights have high defense but low attack...\nSpellcasters have high attack but low defense...\nRangers have average attack and defense but high initiative...")
    
    valid_choice = False
    while not valid_choice:
        player_class = input(">: ").title()
        valid_class_choices = classlist
        if player_class in valid_class_choices:
            if player_class == "Knight":
                player_stats = knight_stats
            elif player_class == "Spellcaster":
                player_stats = spellcaster_stats
            elif player_class == "Ranger":
                player_stats = ranger_stats
            valid_choice = True
        else:
            print("Invalid class choice. Please try again.")
    print("And so your adventure begins...")

    return player_stats, player_name, player_class

player_character = Player("Player", " ", 0, 1, 0, 0, 0)