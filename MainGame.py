import pickle
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
        if player_answer == "start game":
            start_game()
            game = False
        elif player_answer == "load game":
            try:
                load_game()
                game = False
            except Exception:
                print("There is no save file. Please start a new game.")
        elif player_answer == "exit game":
            exit()
        else:
            print("Please select from the options given.")
            
def start_game():
    Player.character_creation()

def player_menu():  #  Might want to redo this code
    if Player.player_character.floor == 3 and Player.player_character.position == 2:
        print(Player.player_character.position)
        print(f"You have entered the boss room...You have been attacked by {Enemy.balrog.name}!")
        Battle.battle(Enemy.balrog)
    else: 
        examined = False
        while True:
            if Player.player_character.floor == 3 and Player.player_character.position == 2:
                print(f"You have entered the boss room...You have been attacked by {Enemy.balrog.name}!")
                Battle.battle(Enemy.balrog)
            player_answer = int(input("What do you want to do?\n1: Move\n2: Examine\n3: Equip item\n4: Unequip item\n5: Inventory\n6: Save\n7: Load\n>: "))
            if player_answer == 1:
                Player.player_character.move()
                print("You have moved to the next room.")
                enemy_num_encountered = random.randint(0, 2)
                encounter = Battle.encounter_check()
                if (encounter == True and
                        enemy_num_encountered == 0):
                    print(f"You have been attacked by {Enemy.slime.name}!")
                    Enemy.slime.hp = 20  #  Battle auto completes because the "new hp value" gets saved within the loop. Look at this code later again.
                    Battle.battle(Enemy.slime)
                elif (encounter == True and 
                        enemy_num_encountered == 1):
                    print(f"You have been attacked by {Enemy.skeleton.name}!")
                    Enemy.skeleton.hp = 30
                    Battle.battle(Enemy.skeleton)
                elif (encounter == True and
                        enemy_num_encountered == 2):
                    print(f"You have been attacked by {Enemy.zombie.name}!")
                    Enemy.zombie.hp = 25
                    Battle.battle(Enemy.zombie)
                else: pass
            elif player_answer == 2:
                if not examined:
                    print(RoomDescription.random_room_description())
                    examined = True
                else:
                    print("You have already examined this room!")
            elif player_answer == 3:
                Player.equip_item()
            elif player_answer == 4:
                Player.unequip_item()
            elif player_answer == 5:
                if not Player.player_character.inventory:
                    print("You have nothing in your inventory!")
                else:
                    print(Player.player_character.check_inventory())
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
    game_menu()
    player_menu()

if __name__ == "__main__":
    main()