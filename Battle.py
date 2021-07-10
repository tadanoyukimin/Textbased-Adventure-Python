import random
import Player
import Items

def attack():
    player_damage = Player.player_character.attack
    return player_damage

def defend():
    player_defense = Player.player_character.defense
    return player_defense

def damage_enemy(encountered_enemy, player_damage):
    adjusted_damage = player_damage - encountered_enemy.defense
    encountered_enemy.hp -= adjusted_damage
    print(f"You hit {encountered_enemy} for {adjusted_damage}!")

def guard(encountered_enemy, player_defense):
    adjusted_enemy_damage = encountered_enemy.attack - player_defense
    Player.player_character.hp -= adjusted_enemy_damage
    print(f"You got hit for {adjusted_enemy_damage} while guarding. You have {Player.player_character.hp} HP.")

def enemy_attack(enemy):
    enemy_damage = enemy.attack
    adjusted_enemy_damage = enemy_damage - Player.player_character.defense
    Player.player_character.hp -= adjusted_enemy_damage
    print(f"You got hit for {adjusted_enemy_damage}! You have {Player.player_character.hp} HP.")

def encounter_check():
    no_encounter = Player.player_character.initiative
    yes_encounter = random.randint(0, 10)
    if yes_encounter > no_encounter:
        print("You hear slight rumbling in the distance...")
        print("You have been attacked!")
        return yes_encounter

def battle(enemy):
    in_combat = True
    while in_combat:
        while enemy.hp > 0:
            if Player.player_character.hp <=0:
                print(Player.player_character.hp)
                print("You died. GAME OVER.")
                exit()
            else:
                player_action = input("What do you want to do?\n1. Attack\n2. Guard\n3. Flee\n>")
                if player_action == 1:
                    player_attack = attack()
                    damage_enemy(enemy, player_attack)
                    enemy_attack(enemy)
                elif player_action == 2:
                    player_defense = defend()
                    guard(enemy, player_defense)
                    enemy_attack(enemy)
                elif player_action == 3:
                    print("You flee successfully!")
                    in_combat = False
                else:
                    print("Please select the correct option.")

        print("You have defeated the enemy.")
        Player.player_character.gold += enemy.gold
        Player.player_character.inventory.append(enemy.loot)
        in_combat = False 