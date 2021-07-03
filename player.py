import items

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
    
    def loot_item(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        print("This is your inventory.")
        print("------------------------")
        print(f"{self.inventory}")

    def check_equipment(self):
        print("This is your equipment.")
        print("------------------------")
        print(f"{self.equipment}")

def equip_item():
    player_answer = input("What item do you want to equip?> ").title()
        # for equipment in player_character.inventory:
        #     try:
        #         if equipment == player_answer.title():
        #             equipment_category = equipment.category
        #             print(equipment_category)
        #             if not player_character.equipment[equipment_category]:
        #                 player_character.inventory.append(player_character.equipment[equipment_category])
        #                 player_character.equipment[equipment_category] = equipment
        #             elif player_character.equipment[equipment_category]:
        #                 player_character.inventory.append(player_character.inventory[equipment_category])
        #                 player_character.equipment[equipment_category] = equipment
        #             player_character.attack

    for equipment in player_character.inventory:
        print(equipment)
        print(equipment in items.dict_item_stats)
        # try:
        #     if player_answer is equipment.name.title():  
        #         if isinstance(player_answer, items.Weapon) is True:
        #             if player_character.equipment["Weapon"] is None:
        #                 player_character.equipment["Weapon"] = equipment
        #                 player_character.attack += equipment.attack
        #                 return f"You have equipped {equipment}."
        #             elif player_character.equipment["Weapon"]:
        #                 player_character.inventory.append(player_character.equipment["Weapon"])
        #                 player_character.equipment["Weapon"] = equipment
        #                 player_character.attack += equipment.attack
        #                 return f"You have equipped {equipment}."
        #             else:
        #                 return "There is nothing to equip"
        #         if isinstance(player_answer, items.Armor) is True:
        #             if player_character.equipment["Shield"] is None:
        #                 player_character.inventory.append(player_character.equipment["Shield"])
        #                 player_character.equipment["Shield"] = equipment
        #             elif player_character.equipment["Shield"]:
        #                 player_character.inventory.append(player_character.equipment["Shield"])
        #                 player_character.equipment["Shield"] = equipment
        #             player_character.defense += equipment.defense
        #         if isinstance(player_answer, items.Armor) is True:
        #             if player_character.equipment["Shield"] is None:
        #                 player_character.inventory.append(player_character.equipment["Armor"])
        #                 player_character.inventory["Armor"] = equipment
        #             elif player_character.equipment["Armor"]:
        #                 player_character.inventory.append(player_character.equipment["Armor"])
        #                 player_character.inventory["Armor"] = equipment
        #             player_character.defense += equipment.defense   
        # except AttributeError:
        #     return "Did not equip"
                    
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
player_character.loot_item("Bronze Sword")
player_character.check_inventory()
equip_item()ffff

