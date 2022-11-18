import random
import math
import colorama
from guardian import Guardian
from enemy import Enemy, Boss
from colorama import Fore
colorama.init(autoreset=True)


def enemy_spawn(level_boss):
    """
    Spawn a random enemy or boss and assigns stats
    """
    file = open('enemy.txt', 'r')
    lines = file.readlines()
    enemy = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()
    file = open('boss.txt', 'r')
    lines = file.readlines()
    boss = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()

    if level_boss is False:
        health = random.randint(50, 100)
        attack = random.randint(10, 20)
        chance = random.randint(1, 10)

        return Enemy(health, attack, chance, enemy)

    else:
        health = random.randint(200, 250)
        attack = random.randint(30, 50)
        chance = random.randint(1, 8)
        super_move = random.randint(100, 200)

        return Boss(health, attack, chance, boss, super_move)


def enemy_attack(strike_chance, attack_value, name, defence):
    """
    Sets up Enemy attack and uses random to see if successful
    """
    print(name, "is about to strike...")
    strike = random.randint(0, 10)
    if strike_chance >= strike:
        print(f"{name} has struck you successfully...")
        loss = attack_value - defence
        print(f"You feel the warm heat of '{Fore.RED}blood'")
        print("you stagger back losing", loss, "health.")
        return math.ceil(loss)

    else:
        print("The enemy misses!")
        return 0


def strike_chance(luck):
    """
    Sets up Guardian attack and uses random to see if successful
    """
    strike = random.randint(0, 4)
    if luck < strike:
        print("You missed!")
        return False

    else:
        print("You struck the enemy!")
        return True


def isDead(health):
    """
    Checks if Guardian or Enemy has died
    """
    if health < 1:
        return True
    else:
        return False
