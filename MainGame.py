import pickle
import Player
import DungeonMap
import Battle
import Enemy
import Items


def start_game():
    player_stat_info, player_name = Player.character_creation()
    Player.player_character.player = player_name
    Player.player_character.hp = player_stat_info[0]
    Player.player_character.hp = player_stat_info[1]
    Player.player_character.mp = player_stat_info[2]
    Player.player_character.attack = player_stat_info[3]
    Player.player_character.defense = player_stat_info[4]
    Player.player_character.initiative = player_stat_info[5]
    dungeon_map = DungeonMap.dungeon_map_second

def player_action():
    while True:
        player_answer = int(input("What do you want to do?\n1: Move\n2: Examine\n3: Equip item\n4: Unequip item\n5: Inventory\n6: Save\n: Load\n>: "))
        if player_answer == 1:
            Player.player_character.move()
        if player_answer == 2:
            pass
        if player_answer == 3:
            Player.equip_item()
        if player_answer == 4:
            Player.unequip_item()
        if player_answer == 5:
            save_game()
        if player_answer == 6:
            load_game()
        else:
            "Please select from options provided."  

def save_game():
    dict_save = {
        "playerinventory": Player.player_character.inventory,
        "playerequipment": Player.player_character.equipment,
        "playerhp": Player.player_character.hp,
        "playermp": Player.player_character.mp,
        "playerattack": Player.player_character.attack,
        "playerdefense": Player.player_character.defense,
        "playerinitiative": Player.player_character.initiative,
        "playergold": Player.player_character.gold,
        "playerposition": Player.player_character.position
    }
    pickle.dump(dict_save, open("save.p", "wb"))

def load_game():
    dict_load = pickle.load(open("save.p", "rb"))
    Player.player_character.inventory = dict_load["playerinventory"]
    Player.player_character.equipment = dict_load["playerequipment"]
    Player.player_character.hp = dict_load["playerhp"]
    Player.player_character.mp = dict_load["playermp"]
    Player.player_character.attack = dict_load["playerattack"]
    Player.player_character.defense = dict_load["playerdefense"]
    Player.player_character.initiative = dict_load["playerinitiative"]
    Player.player_character.gold = dict_load["playergold"]
    Player.player_character.position = dict_load["playerposition"]