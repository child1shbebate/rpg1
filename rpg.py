import random

# Player class selection
player = input("Enter your name: ")

intelligence = 0
mana = 0
health = 0
agility = 0
strength = 0

print("Choose your class: mage, warrior, hunter")

while True:
    player_class = input().strip().lower()
    if player_class == "mage":
        intelligence = 10
        mana = 100
        health = 80
        agility = 5
        strength = 3
        ability1 = "fireball"
        ability2 = "blink"
        ability3 = "iceblock"
        break
    elif player_class == "warrior":
        intelligence = 1
        health = 100
        mana = 30
        agility = 4
        strength = 10
        ability1 = "rend"
        ability2 = "charge"
        ability3 = "shield wall"
        break
    elif player_class == "hunter":
        intelligence = 3
        health = 60
        mana = 0
        agility = 10
        strength = 3
        pet = 5
        ability1 = "kill command"
        ability2 = "disengage"
        ability3 = "play dead"
        break
    else:
        print("INVALID INPUT PLEASE CHOOSE BETWEEN 'mage, warrior, hunter'")

print(f"You have chosen {player_class}")
print(f"You have {ability1}, {ability2}, {ability3}")
print(f"Health: {health}")
print(f"Mana: {mana}")
print(f"Intelligence: {intelligence}")
print(f"Agility: {agility}")
print(f"Strength: {strength}")
level = 1
print(f"Level: {level}")
xp = 0

print("------------------------------------------------------")
print("Choose your path: left or right")

path_choice = input().strip().lower()

def combat(player_health, player_mana, enemy_health, enemy_damage_min,
           enemy_damage_max, items, abilities):
    iceblock_turns = 0

    while player_health > 0 and enemy_health > 0:
        print("Choose your action: use 1/2/3 for abilities, or 'use item'")
        print(f"1. {abilities[0]}")
        print(f"2. {abilities[1]}")
        print(f"3. {abilities[2]}")
        user_input = input().strip().lower()

        if user_input in ["1", "2", "3"]:
            ability_input = int(user_input)

            if ability_input == 1 and player_class == "mage":
                if player_mana >= 20:
                    print(f"You used {abilities[0]}!")
                    enemy_health -= 10 + (0.5 * intelligence)
                    player_mana -= 20
                else:
                    print("Not enough mana to use fireball!")
                    continue
            elif ability_input == 2 and player_class == "mage":
                print(f"You used {abilities[1]}! You gain 45 mana.")
                player_mana += 45
            elif ability_input == 3 and player_class == "mage":
                print(f"You used {abilities[2]}! You are immune to damage for 3 turns.")
                iceblock_turns = 3
            elif ability_input == 1 and player_class == "warrior":
                print(f"You used {abilities[0]}!")
                enemy_health -= 15
            elif ability_input == 2 and player_class == "warrior":
                print(f"You used {abilities[1]}!")
                enemy_health -= 25
            elif ability_input == 3 and player_class == "warrior":
                print(f"You used {abilities[2]}! You reduce incoming damage by 50% for 3 turns.")
                iceblock_turns = 3
            elif ability_input == 1 and player_class == "hunter":
                print(f"You used {abilities[0]}!")
                enemy_health -= 12
            elif ability_input == 2 and player_class == "hunter":
                print(f"You used {abilities[1]}! You disengage and avoid damage for 1 turn.")
                blink_turns = 1
            elif ability_input == 3 and player_class == "hunter":
                print(f"You used {abilities[2]}! You play dead and avoid all damage for 3 turns.")
                iceblock_turns = 3
            else:
                print("Invalid ability choice!")
                continue

            # Print the health status
            print(f"Player health: {player_health}")
            print(f"Player mana: {player_mana}")
            print(f"Enemy health: {enemy_health}")
            print(f"------------------")

        elif user_input == "use item":
            while True:
                print("Choose an item to use: 1/2/3")
                try:
                    item_input = int(input())
                    if item_input in [1, 2, 3] and items[item_input - 1] > 0:
                        # Use item (simple logic: heal player or increase attack)
                        if item_input == 1:
                            player_health += 20  # Example: heal item
                            print("You used a healing item. Health increased by 20.")
                        elif item_input == 2:
                            abilities[1] += 10  # DPS pot
                            print("You used DPS POT.Damage increased by 10.")
                        elif item_input == 3:
                            player_mana += 30  # Example: mana potion
                            print("You used a mana potion. Mana increased by 30.")
                        items[item_input - 1] -= 1
                        break
                    else:
                        print("Invalid item choice or no items left!")
                except ValueError:
                    print("Invalid input. Please choose an item number (1/2/3).")
        else:
            print("Invalid action choice!")
            continue

        # Apply enemy attack if not in special ability mode
        if iceblock_turns <= 0 :
            player_health -= random.randint(enemy_damage_min, enemy_damage_max)
        else:
            print("Special ability active! No damage taken.")
        if iceblock_turns > 0:
            iceblock_turns -= 1

        # Print the health status
        print(f"Player health: {player_health}")
        print(f"Player mana: {player_mana}")
        print(f"Enemy health: {enemy_health}")

    # Outcome of the combat
    if player_health <= 0 and enemy_health <= 0:
        print("You die with the enemy")
    elif player_health <= 0:
        print("You have been defeated.")
    elif enemy_health <= 0:
        print("You have defeated the enemy.")

    return player_health, enemy_health

# Define abilities based on class
if player_class == "mage":
    abilities = [ability1, ability2, ability3]
elif player_class == "warrior":
    abilities = [ability1, ability2, ability3]
elif player_class == "hunter":
    abilities = [ability1, ability2, ability3]

# Define initial health and damage values for enemy
enemy_health = 100
enemy_damage_min = 5
enemy_damage_max = 15


items = [1, 1, 1]  # Each item slot has 1 item to start with

# Call the combat function
combat(health, mana, enemy_health, enemy_damage_min, enemy_damage_max, items, abilities)
