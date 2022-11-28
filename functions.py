"""
Contains all functions for game
"""

import os
import sys
import random
import math
import time
from pprint import pprint
from getch import pause
import colorama
from colorama import Fore, Style
import ascii_art
import adventure
from classes.guardian import Guardian
from classes.enemy import Enemy
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
        time.sleep(0.04)


def clear_display():
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def sleep():
    """
    Function for sleep sequence
    """
    for zzz in ascii_art.z_list:
        for asleep in range(2):
            clear_display()
            print(Fore.GREEN + Style.BRIGHT + zzz + zzz + zzz)
            time.sleep(.5)
    return asleep


# Game Functions
##################################################


def gen_char():
    """"
    Function generates Guardian
    """
    clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.WELCOME)
    while True:
        try:
            name = input("What is your name Guardian: \n").strip().capitalize()
            if name.isalnum():
                typing_print(f"\nWelcome to the game {name}\n")
                break
            elif len(name.strip(" ")) == 0:
                print("I appreciate that you may want to keep your identity\n"
                      "a secret but we require a name to join our ranks....\n")
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input - Please enter only letters and numbers\n")
    print(
        f'\nWell {name} what kind of Guardian are you?\n'
        f'\nWould you consider yourself a {Fore.GREEN}{Style.BRIGHT}'
        f'(W)arrior{Style.RESET_ALL}, an '
        f'{Fore.GREEN}{Style.BRIGHT}(A)ssassin{Style.RESET_ALL} or a '
        f'{Fore.GREEN}{Style.BRIGHT}(M)age?\n')
    user_choice = input(
        f"{Fore.GREEN}{Style.BRIGHT}Enter 'W',"
        f"'A' or 'M': ").lower().strip(" ")
    while user_choice != "w" and user_choice != "a" and user_choice != "m":
        print(
            'Invalid input - Enter "W" for "Warrior", "A" for "Assassin"'
            ', "M" for "Mage"\n')
        user_choice = input(
            f"{Fore.GREEN}{Style.BRIGHT}Enter 'W',"
            f"'A' or 'M': ").lower().strip(" ")

    if user_choice == "w":
        typing_print("\nGenerating Guardian.....")
        attack = 10
        defense = 8
        health = 100
        ranged = 6
        magic = 6
        luck = random.randint(4, 6)

    elif user_choice == "a":
        typing_print("\nGenerating Guardian.....")
        attack = 5
        defense = 8
        health = 100
        ranged = 12
        magic = 5
        luck = random.randint(4, 6)

    else:
        typing_print("\nGenerating Guardian.....\n")
        attack = 6
        defense = 6
        health = 100
        ranged = 6
        magic = 12
        luck = random.randint(4, 6)

    return Guardian(attack, defense, health, luck, magic, ranged, name)


def gen_enemy():
    """
    Spawn a random enemy and assigns stats
    """
    file = open('docs/enemy.txt', 'r', encoding="utf8")
    lines = file.readlines()
    enemy = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()

    health = random.randint(80, 100)
    attack = random.randint(14, 20)
    chance = random.randint(1, 10)
    defence = random.randint(1, 5)

    return Enemy(health, attack, defence, chance, enemy)


def gen_boss():
    """
    Spawn a random enemy and assigns stats
    """
    file = open('docs/boss.txt', 'r', encoding="utf8")
    lines = file.readlines()
    boss = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()
    health = random.randint(100, 120)
    attack = random.randint(15, 25)
    defence = random.randint(1, 5)
    chance = random.randint(1, 8)

    return Enemy(health, attack, defence, chance, boss)


def strike_chance(luck):
    """
    Sets up Guardian attack and uses random to see if successful
    """
    hit = random.randint(1, 6)
    if luck < hit:
        print("\nYou missed!")
        return False

    else:
        return True


def enemy_attack(enemy_chance, attack_value, name, defence):
    """
    Sets up Enemy attack and uses random to see if successful
    """
    print(f"{Fore.RED}{Style.BRIGHT}{name} {Style.RESET_ALL}"
          f"is about to strike...\n")
    time.sleep(0.9)
    strike = random.randint(1, 10)
    if enemy_chance >= strike:
        print(
            f"{Fore.RED}{Style.BRIGHT}{name} {Style.RESET_ALL}has struck you "
            f"successfully...\n")
        loss = attack_value - defence
        print(f"You feel the warm heat of {Fore.RED}{Style.BRIGHT}blood... "
              f"you stagger back losing {loss} health.\n")
        return math.ceil(loss)

    else:
        print("The enemy misses!")
        return 0


def found_loot(char):
    """
    Applies found loot to character
    """
    loot_list = ["docs/common.txt", "docs/legandary.txt",
                 "docs/exotic.txt"]
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
        print(f"\nan {Fore.YELLOW}{Style.BRIGHT}{rarity} item - {name}\n")

    elif rarity == "Legendary":
        print(f"\na {Fore.MAGENTA}{Style.BRIGHT}{rarity} item - {name}\n")

    else:
        print(f"\na {Fore.BLUE}{Style.BRIGHT}{rarity} item - {name}\n")

    if assign == "attack":
        char.set_attack(char.get_attack()+value)
        print("Your new Close Attack stat is...")
        print(char.get_attack(), "\n")

    elif assign == "ranged":
        char.set_ranged(char.get_ranged()+value)
        print("Your new Ranged Attack stat is...")
        print(char.get_ranged(), "\n")

    elif assign == "defence":
        char.set_defence(char.get_defence()+value)
        if char.get_defence() > 13:
            char.set_defence(13)
        print("Your new Defence stat is...")
        print(char.get_defence(), "\n")

    elif assign == "magic":
        char.set_magic(char.get_magic()+value)
        print("Your new Magic Attack stat is...")
        print(char.get_magic(), "\n")

    else:
        if assign == "luck":
            char.set_luck(char.get_luck()+value)
            if char.get_luck() > 10:
                char.set_luck(10)
            print("Your new Luck stat is...")
            print(char.get_luck(), "\n")

        elif assign == "health":
            char.set_health(char.get_health()+value)
            print("Your new Health stat is...")
            print(char.get_health(), "\n")


def loot(luck, char_luck):
    """
    Calculates chance of loot dropping from enemy
    """
    loot_chance = random.randint(0, 4)
    if luck < loot_chance:
        print("That creature dropped no loot...")

    else:
        loot_list = ["docs/common.txt", "docs/legandary.txt",
                     "docs/exotic.txt"]
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
            print(f"{Fore.YELLOW}{Style.BRIGHT}{rarity} item - {name}\n")

        elif rarity == "Legendary":
            print("The enemy dropped a....")
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{rarity} item - {name}\n")

        else:
            print("The enemy dropped a....")
            print(f"{Fore.BLUE}{Style.BRIGHT}{rarity} item - {name}\n")

        if assign == "attack":
            char_luck.set_attack(char_luck.get_attack()+value)
            print("Your new Close Attack stat is...")
            print(char_luck.get_attack(), "\n")

        elif assign == "ranged":
            char_luck.set_ranged(char_luck.get_ranged()+value)
            print("Your new Ranged Attack stat is...")
            print(char_luck.get_ranged(), "\n")

        elif assign == "defence":
            char_luck.set_defence(char_luck.get_defence()+value)
            if char_luck.get_defence() > 13:
                char_luck.set_defence(13)
            print("Your new Defence stat is...")
            print(char_luck.get_defence(), "\n")

        elif assign == "magic":
            char_luck.set_magic(char_luck.get_magic()+value)
            print("Your new Magic Attack stat is...")
            print(char_luck.get_magic(), "\n")

        else:
            if assign == "luck":
                char_luck.set_luck(char_luck.get_luck()+value)
                if char_luck.get_luck() > 10:
                    char_luck.set_luck(10)
                print("Your new Luck stat is...")
                print(char_luck.get_luck(), "\n")

            elif assign == "health":
                char_luck.set_health(char_luck.get_health()+value)
                print("Your new Health stat is...")
                print(char_luck.get_health(), "\n")


def is_dead(health):
    """
    Checks if Guardian or Enemy has died
    """
    if health < 1:
        return True
    else:
        return False


def game_over(enemy_dead):
    """
    Checks for Game Over
    """
    if enemy_dead:
        return True
    else:
        print("The foul beast has struck you down Guardian....")
        print(Fore.RED + Style.BRIGHT + ascii_art.GAME_OVER)
        pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress "
              f"any key to return to the homescreen")
        adventure.welcome_screen()


def battle(enemy, guardian):
    """
    Function to handle battle sequence between Guardian and Enemy
    """
    clear_display()
    print(Fore.RED + Style.BRIGHT + ascii_art.ENEMY)
    print(f"{Fore.RED}{Style.BRIGHT}"
          f"{enemy.get_e_name()}{Style.RESET_ALL}"
          f", and they look ready for a fight!\n")
    print(
        f"Check out the {Fore.RED}{Style.BRIGHT}{enemy.get_e_name()}"
        f"'s{Style.RESET_ALL} stats:\n")
    stats = vars(enemy)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")

    fight = True

    while fight:
        print(
            "\nYou have engaged the creature, which attack would you like to"
            f" use:\n {Fore.GREEN}{Style.BRIGHT}'C' for 'Close', 'R' for"
            f" 'Ranged', 'M' for 'Magic' attack?\n")
        choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")
        while choice != "c" and choice != "r" and choice != "m":
            print(
                'Invalid input - Enter "C" for "Close", "R" for "Ranged"'
                ', "M" for "Magic"\n')
            choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")

        if choice == "c":
            damage = guardian.get_attack() - enemy.get_e_defence()

        elif choice == "r":
            damage = guardian.get_ranged() - enemy.get_e_defence()

        else:
            damage = guardian.get_magic() - enemy.get_e_defence()
        clear_display()
        typing_print("You wind up for the attack!!...\n")
        time.sleep(0.8)
        strike = strike_chance(guardian.get_luck())

        if strike:
            enemy.set_e_health(enemy.get_e_health() - damage)
            print(f"\nYou struck the enemy, {Fore.RED}{Style.BRIGHT}"
                  f"{enemy.get_e_name()}'s blood gushes....\n")

        else:
            print("Enemy dodged your attack\n")

        enemy_dead = is_dead(enemy.get_e_health())

        if not enemy_dead:
            print(
                f"{Fore.RED}{Style.BRIGHT}{enemy.get_e_name()}'s "
                f"{Style.RESET_ALL}health is {enemy.get_e_health()}")
            guardian.set_health(guardian.get_health() - enemy_attack
                                (enemy.get_e_chance(),
                                enemy.get_e_attack(),
                                enemy.get_e_name(),
                                guardian.get_defence()))

            guardian_dead = is_dead(guardian.get_health())

            if guardian_dead:
                clear_display()
                print(f'You died {guardian.get_name()}\n')
                game_over(enemy_dead)
                fight = False
                return False

            else:
                print(f"{guardian.get_name()}'s remaining health is...."
                      f"{guardian.get_health()}")

        else:
            fight = False
            print(f"{Fore.RED}{Style.BRIGHT}{enemy.get_e_name()}"
                  f"{Style.RESET_ALL}, has been slain!\n")
            if guardian.get_health() < 100:
                guardian.set_health(100)
            loot(guardian.get_luck(), guardian)
            return True
