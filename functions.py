"""
Contains all functions for game
"""

import os
import sys
import random
import math
import time
from pprint import pprint
import colorama
from colorama import Fore, Style
import ascii_art
from classes.enemy import Enemy, Boss
colorama.init(autoreset=True)

# Utility Functions
##################################################


def typing_print(text):
    """"
    Adds typewriter effect for print function
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


def clear_display():
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Game Functions
##################################################


def gen_char():
    """"
    Function generates Guardian
    """
    clear_display()
    print(Fore.GREEN + ascii_art.WELCOME)
    name = input("What is your name Guardian: ").capitalize()
    while len(name.strip(" ")) == 0:
        print("I appreciate that you may want to keep your identity a "
              "secret but we require a name to join our ranks....")
        name = input("What is your name Guardian: ")
    print(
        f'\nWell {name} what kind of Guardian are you?\n'
        f'\nWould you consider yourself a {Fore.GREEN}'
        f'(W)arrior{Style.RESET_ALL}, an '
        f'{Fore.GREEN}(A)ssassin{Style.RESET_ALL} or a '
        f'{Fore.GREEN}(M)age?\n')
    user_choice = input(
        f"{Fore.GREEN}Enter 'W', 'A' or 'M': ").lower().strip(" ")
    while user_choice != "w" and user_choice != "a" and user_choice != "m":
        print(
            'Invalid input - Enter "W" for "Warrior", "A" for "Assassin"'
            ', "M" for "Mage"\n')
        user_choice = input(
            f"{Fore.GREEN}Enter 'W', 'A' or 'M': ").lower().strip(" ")

    if user_choice == "w":
        typing_print("\nGenerating Guardian.....")
        attack = 10
        defense = 10
        health = 100
        luck = random.randint(0, 10)
        ranged = 5
        magic = 5

    elif user_choice == "a":
        typing_print("\nGenerating Guardian.....")
        attack = 5
        defense = 8
        health = 100
        ranged = 12
        magic = 5
        luck = random.randint(0, 10)

    else:
        typing_print("\nGenerating Guardian.....\n")
        attack = 4
        defense = 6
        health = 100
        ranged = 8
        magic = 12
        luck = random.randint(0, 10)

    clear_display()
    return (attack, defense, health, luck, magic, ranged, name)


def gen_enemy():
    """
    Spawn a random enemy and assigns stats
    """
    file = open('docs.enemy.txt', 'r', encoding="utf8")
    lines = file.readlines()
    enemy = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()

    health = random.randint(50, 100)
    attack = random.randint(10, 20)
    chance = random.randint(1, 10)

    return Enemy(health, attack, chance, enemy)


def gen_boss():
    """
    Spawn a random enemy and assigns stats
    """
    file = open('docs.boss.txt', 'r', encoding="utf8")
    lines = file.readlines()
    boss = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()
    health = random.randint(200, 250)
    attack = random.randint(30, 50)
    chance = random.randint(1, 8)
    super_move = random.randint(100, 200)

    return Boss(health, attack, chance, boss, super_move)


def strike_chance(luck):
    """
    Sets up Guardian attack and uses random to see if successful
    """
    hit = random.randint(0, 4)
    if luck < hit:
        print("You missed!")
        return False

    else:
        return True


def enemy_attack(strike_chance, attack_value, name, defence):
    """
    Sets up Enemy attack and uses random to see if successful
    """
    print(name, "is about to strike...\n")
    time.sleep(0.9)
    strike = random.randint(0, 10)
    if strike_chance >= strike:
        print(f"{name} has struck you successfully...")
        loss = attack_value - defence
        print(f"You feel the warm heat of {Fore.RED}blood...")
        print("you stagger back losing", loss, "health.")
        return math.ceil(loss)

    else:
        print("The enemy misses!")
        return 0


def is_dead(health):
    """
    Checks if Guardian or Enemy has died
    """
    if health < 1:
        return True
    else:
        return False


def loot(luck, gen_char):
    """
    Calculates chance of loot dropping from enemy
    """
    loot_chance = random.randint(0, 4)
    if luck < loot_chance:
        print("That creature dropped no loot...")

    else:
        loot_list = ["docs.common.txt", "docs.legandary.txt",
                     "docs.exotic.txt"]
        listnum = random.randint(0, 2)
        item_type = loot_list[listnum]
        file = open(item_type, "r", encoding="utf8")
        lines = file.readlines()

        item = random.randint(0, len(lines)-1)

        item_line = lines[item]
        split_item_line = item_line.split(",")

        rarity = split_item_line[0]
        name = split_item_line[1]
        value = int(split_item_line[2])
        assign = split_item_line[3]

        if rarity == "Exotic":
            print("The enemy dropped an....")
            print(f"{Fore.YELLOW}{rarity} item - {name}")

        elif rarity == "Legendary":
            print("The enemy dropped an....")
            print(f"{Fore.MAGENTA}{rarity} item - {name}")

        else:
            print("The enemy dropped a....")
            print(f"{Fore.CYAN}{rarity} item - {name}")

        if assign == "attack":
            gen_char.set_attack(gen_char.get_attack()+value)
            print("Your new Close Attack stat is...")
            print(gen_char.get_attack())

        elif assign == "ranged":
            gen_char.set_ranged(gen_char.get_ranged()+value)
            print("Your new Ranged Attack stat is...")
            print(gen_char.get_ranged())

        elif assign == "defence":
            gen_char.set_defence(gen_char.get_defence()+value)
            print("Your new Defence stat is...")
            print(gen_char.get_defence())

        elif assign == "magic":
            gen_char.set_magic(gen_char.get_magic()+value)
            print("Your new Magic Attack stat is...")
            print(gen_char.get_magic())

        else:
            if assign == "luck":
                gen_char.set_luck(gen_char.get_luck()+value)
                print("Your new Luck stat is...")
                print(gen_char.get_luck())

            elif assign == "health":
                gen_char.set_health(gen_char.get_health()+value)
                print("Your new Health stat is...")
                print(gen_char.get_health())


def game_over(enemy_dead):
    """
    Checks for Game Over
    """
    if enemy_dead:
        print("Congratulations Guardian you have slain")
    else:
        print("The foul beast has struck you down Guardian....")


def battle(gen_enemy, gen_char):
    """
    Function to handle battle sequence between Guardian and Enemy
    """
    print(f"Its... {Fore.RED}{gen_enemy.getEName()}{Fore.WHITE}"
          f", and they look ready for a fight!\n")
    print(f"Check out {Fore.RED}{gen_enemy.getEName()}'s{Fore.WHITE} stats:\n")
    stats = vars(gen_enemy)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")

    fight = True

    while fight:
        print(
            "\nYou have engaged the creature, which attack would you like to"
            f" use:\n {Fore.GREEN}'C' for 'Close', 'R' for 'Ranged'"
            f", 'M' for 'Magic' attack?\n")
        choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")
        while choice != "c" and choice != "r" and choice != "m":
            print(
                'Invalid input - Enter "C" for "Close", "R" for "Ranged"'
                ', "M" for "Magic"\n')
            choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")

        if choice == "c":
            damage = gen_char.get_attack()

        elif choice == "r":
            damage = gen_char.get_ranged()

        else:
            damage = gen_char.get_magic()
        clear_display()
        typing_print("You wind up for the attack!!...\n")
        time.sleep(0.8)
        strike = strike_chance(gen_char.get_luck())

        if strike:
            gen_enemy.set_e_health(gen_enemy.get_e_health() - damage)
            print(f"You struck the enemy, {Fore.RED}{gen_enemy.get_e_name()}'s"
                  f" blood gushes....\n")
            print(
                f"{gen_enemy.get_e_name()}'s health is now"
                f"{gen_enemy.get_e_health()}")

        else:
            print("Enemy dodged your attack")

        enemy_dead = is_dead(gen_enemy.get_e_health())

        if not enemy_dead:
            gen_char.set_health(gen_char.get_health() - enemy_attack
                                (gen_enemy.get_e_chance(),
                                gen_enemy.get_e_attack(),
                                gen_enemy.get_e_name(),
                                gen_char.get_defence()))

            guardian_dead = is_dead(gen_char.get_health())

            if guardian_dead:
                fight = False
                return False

            else:
                print("Guardian's remaining health is....",
                      gen_char.get_health())

        else:
            fight = False
            print(gen_enemy.get_e_name(), "has been slain")
            loot(gen_char.get_luck(), gen_char)
            return True
