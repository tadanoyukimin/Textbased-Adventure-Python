import random
import Player

def attack():
    player_damage = Player.player_character.attack
    return player_damage

def defend():
    player_defense = Player.player_character.defense
    return player_defense

def damage_enemy(encountered_enemy, player_damage):
    adjusted_damage = player_damage - encountered_enemy.defense
    encountered_enemy.hp -= adjusted_damage
    print(f"You hit the {encountered_enemy.name} for {adjusted_damage} damage!")

def guard(encountered_enemy, player_defense):
    adjusted_enemy_damage = encountered_enemy.attack - player_defense
    Player.player_character.hp -= adjusted_enemy_damage
    if adjusted_enemy_damage <= 0:
        adjusted_enemy_damage = 0
    print(f"You got hit for {adjusted_enemy_damage} while guarding. You have {Player.player_character.hp} HP left.")

def enemy_attack(enemy):
    enemy_damage = enemy.attack
    adjusted_enemy_damage = enemy_damage - Player.player_character.defense
    Player.player_character.hp -= adjusted_enemy_damage
    print(f"You got hit for {adjusted_enemy_damage}! You have {Player.player_character.hp} HP left.")

def encounter_check():
    no_encounter = Player.player_character.initiative
    yes_encounter = random.randint(0, 10)
    if yes_encounter > no_encounter:
        return yes_encounter > no_encounter
    else: return False

def battle(enemy):
    in_combat = True
    while in_combat:
        while enemy.hp > 0:
            if Player.player_character.hp <=0:
                print("You died. GAME OVER.")
                exit()
            else:
                player_action = input("What do you want to do?\n    ATTACK || DEFEND || HEAL\n>: ").lower()
                if player_action == "attack":
                    player_attack = attack()
                    damage_enemy(enemy, player_attack)
                    enemy_attack(enemy)
                elif player_action == "defend":
                    player_defense = defend()
                    guard(enemy, player_defense)
                else:
                    print("Please select the correct option.")

        print("You have defeated the enemy.")
        print(f"You have gained {enemy.gold} gold pieces from the {enemy.name}.")
        if enemy.loot is None:
            print(f"You obtained nothing from the {enemy.name}")
        else:
            print(f"You have obtained {enemy.loot} from the {enemy.name}.")
        Player.player_character.gold += enemy.gold
        Player.player_character.loot_item(enemy.loot)
        enemy.is_defeated = True
        in_combat = False 