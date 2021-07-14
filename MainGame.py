import json
import Player
import DungeonMap
import Battle
import Enemy
import Items
import RoomDescription
import random
import copy

def game_menu():
    print("Welcome to the Textbased Adventure game made in Python.")
    game = True
    while game:
        player_answer = input(
            "What do you want to do?\n1. Start game\n2. Load game\n3. Exit game\n>: ").lower()
        if player_answer == "start game" or "start":
            start_game()
            game = False
        elif player_answer == "load game" or "load":
            try:
                load_game()
                game = False
            except Exception:
                print("There is no save file. Please start a new game.")
        elif player_answer == "exit game" or "exit":
            exit()
        else:
            print("Please select from the options given.")
            
def start_game():
    Player.character_creation()

def help_command():
    print("The following commands are available.")
    print(
        """
        Move: Move your character to the next room, or if possible the next floor.
        Examine: Examine the room you are currently in.
        Inventory: Check your inventory.
        Check Equipment: Check your equipment.
        Equip: Equip an item from your inventory.
        Unequip: Unequip an item from your inventory.
        Save: Saves the game.
        Load: Loads a save file.
        """
    )

def game_commands():
    dict_game_commands = {
        "move": Player.player_character.move,
        "inventory": Player.player_character.check_inventory,
        "equipment": Player.player_character.check_equipment,
        "equip": Player.equip_item,
        "unequip": Player.unequip_item,
        "save": save_game,
        "load": load_game,
        "help": help_command,
        "examine": RoomDescription.random_room_description,
        "map": Player.player_character.check_map
    }
    examined = False
    while True:
        player_input = input("Enter help for a list of commands or if you want to view the list again. What do you want to do?\n:> ").lower()
        if player_input in dict_game_commands:
            try:
                if player_input == "examine" and not examined:
                    RoomDescription.random_room_description()
                    examined = True
                elif player_input == "examine" and examined:
                    print("You have already examined this room!")
                else:
                    dict_game_commands[player_input]()
                    if player_input == "move":
                        examined = False
                        if Player.player_character.floor == 3 and Player.player_character.position == 2:
                            boss_encounter_check()
                        is_encounter = Battle.encounter_check()
                        enemy_num = random.randint(0, 2)
                        if is_encounter==True and enemy_num==0:
                            print(f"You have been attacked by {Enemy.slime.name}!")
                            Battle.battle(Enemy.slime)
                            Enemy.revive_monster()
                        elif is_encounter==True and enemy_num==1:
                            print(f"You have been attacked by {Enemy.skeleton.name}!")
                            Battle.battle(Enemy.skeleton)
                            Enemy.revive_monster()
                        elif is_encounter==True and enemy_num==2:
                            print(f"You have been attacked by {Enemy.zombie.name}!")
                            Battle.battle(Enemy.zombie)
                            Enemy.revive_monster()

            except KeyError:
                print("Unknown command, please check the help documentation.")
        else: print("Unknown command, please check the help documentation.")

def boss_encounter_check():
    if Player.player_character.floor == 3 and Player.player_character.position == 2:
        print(f"You have entered the boss room...You have been attacked by {Enemy.balrog.name}!")
        Battle.battle(Enemy.balrog)
        if Enemy.balrog.is_defeated == True:
            print(f"Congratulations {Player.player_character.player}, you have defeated the boss! Now you can take your spoils and head home...")
            exit()

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
    with open("save.json", "w") as fp:
        json.dump(dict_save, fp)
    print("You have saved the game.")

def load_game():
    with open("save.json", "r") as fp:
        dict_load = json.load(fp)
    Player.player_character.inventory = dict_load["playerinventory"]
    Player.player_character.equipment = dict_load["playerequipment"]
    Player.player_character.hp = dict_load["playerhp"]
    Player.player_character.mp = dict_load["playermp"]
    Player.player_character.attack = dict_load["playerattack"]
    Player.player_character.defense = dict_load["playerdefense"]
    Player.player_character.initiative = dict_load["playerinitiative"]
    Player.player_character.gold = dict_load["playergold"]
    Player.player_character.position = dict_load["playerposition"]
    print("You have loaded a save file.")

def main():
    game_menu()
    help_command()
    game_commands()


if __name__ == "__main__":
    main()