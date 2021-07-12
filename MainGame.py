import pickle
import Player
import DungeonMap
import Battle
import Enemy
import Items
import RoomDescription
import random


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

def player_menu():
    while True:
        player_answer = int(input("What do you want to do?\n1: Move\n2: Examine\n3: Equip item\n4: Unequip item\n5: Inventory\n6: Save\n7: Load\n>: "))
        if player_answer == 1:
            Player.player_character.move()
            if Player.player_character.position == 12:
                Battle.battle(Enemy.balrog)
            Battle.encounter_check()
            enemy_num_encountered = random.randint(0, 3)
            if Battle.encounter_check() and enemy_num_encountered <= 1:
                Battle.battle(Enemy.slime)
            elif Battle.encounter_check() and enemy_num_encountered == 2:
                Battle.battle(Enemy.skeleton)
            elif Battle.encounter_check() and enemy_num_encountered == 3:
                Battle.battle(Enemy.zombie)
        elif player_answer == 2:
            RoomDescription.random_room_description()
            examined = True
            if examined:
                return "You have already examined this room."
        elif player_answer == 3:
            Player.equip_item()
        elif player_answer == 4:
            Player.unequip_item()
        elif player_answer == 5:
            if not Player.player_character.inventory():
                return "You have nothing in your inventory!"
            else:
                Player.player_character.check_inventory()
        elif player_answer == 6:
            save_game()
            print("You have successfully saved your game.")
        elif player_answer == 7:
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

def main():
    player_menu()


if __name__ == "__main__":
    main()