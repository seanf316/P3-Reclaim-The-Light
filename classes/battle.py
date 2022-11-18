import random
import math
from pprint import pprint
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


def enemyAttack(strike_chance, attack_value, name, defence):
    """
    Sets up Enemy attack and uses random to see if successful
    """
    print(name, "is about to strike...")
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


def loot(luck, genChar):
    """
    Calculates chance of loot dropping from enemy
    """
    loot_chance = random.randint(0, 4)
    if luck < loot_chance:
        print("That creature dropped no loot...")

    else:
        lootList = ["common.txt", "legandary.txt", "exotic.txt"]
        listnum = random.randint(0, 2)
        itemType = lootList[listnum]
        file = open(itemType, "r")
        lines = file.readlines()

        item = random.randint(0, len(lines)-1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        rarity = splitItemLine[0]
        name = splitItemLine[1]
        value = int(splitItemLine[2])
        assign = splitItemLine[3]

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
            genChar.setAttack(genChar.getAttack()+value)
            print("Your new Close Attack stat is...")
            print(genChar.getAttack())

        elif assign == "ranged":
            genChar.setRanged(genChar.getRanged()+value)
            print("Your new Ranged Attack stat is...")
            print(genChar.getRanged())

        elif assign == "defence":
            genChar.setDefence(genChar.getDefence()+value)
            print("Your new Defence stat is...")
            print(genChar.getDefence())

        elif assign == "magic":
            genChar.setMagic(genChar.getMagic()+value)
            print("Your new Magic Attack stat is...")
            print(genChar.getMagic())

        else:
            if assign == "luck":
                genChar.setLuck(genChar.getLuck()+value)
                print("Your new Luck stat is...")
                print(genChar.getLuck())

            elif assign == "health":
                genChar.setHealth(genChar.getHealth()+value)
                print("Your new Health stat is...")
                print(genChar.getHealth())


def gameOver(enemyDead):
    if enemyDead:
        print("Congratulations Guardian you have slain")
    else:
        print("The foul beast has struck you down Guardian....")


def battle(enemy_spawn, genChar):
    print("Whats that coming over the hill?????")
    print("Its a...", enemy_spawn.get_enemy_name(), "Looking for a fight!")
    print("Check out its stats....")
    pprint(vars(enemy_spawn))

    battle = True

    while battle:
        print(
            '\nYou have engaged the creature, which attack would you like to'
            ' use:\n "C" for "Close", "R" for "Ranged", "M" for "Magic" attack?\n')
        choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")
        while choice != "c" and choice != "r" and choice != "m":
            print(
            'Invalid input - Enter "C" for "Close", "R" for "Ranged"'
            ', "M" for "Magic"\n')
            choice = input("Enter 'C', 'R' or 'M': ").lower().strip(" ")

        if choice == "c":
            damage = genChar.getAttack()

        elif choice == "r":
            damage = genChar.getRanged()

        else:
            damage = genChar.getMagic()

        print("You wind up for the attack!!...")
        strike = strike_chance(genChar.getLuck())
        
        if strike:
            enemy_spawn.set_health(enemy_spawn.get_health() - damage)
            print(f"You struck the enemy, {Fore.RED}blood gushes....")
            print(f"{enemy_spawn.get_enemy_name()}'s health is now {enemy_spawn.get_health()}")

        else:
            print("Enemy dodged your attack")
        
        enemyDead = isDead(enemy_spawn.get_health())
        
        if not enemyDead:
            genChar.setHealth(genChar.getHealth() - enemyAttack(enemy_spawn.get_chance(), enemy_spawn.get_attack(), enemy_spawn.get_enemy_name(), genChar.getDefence()))
            
            guardianDead = isDead(genChar.getHealth())
            
            if guardianDead:
                battle = False
                return False
            
            else:
                print("Guardian's remaining health is....", genChar.getHealth())
                
        else:
            battle = False
            print(enemy_spawn.get_enemy_name(), "has been slain")
            loot(genChar.getLuck(), genChar)
            return True
        
levelBoss = True

genChar = Guardian(100, 90, 11, 12, 1, 14, "LEE!")


pprint(vars(genChar))

whoDied = battle(enemy_spawn(levelBoss), genChar)
gameOver(whoDied)

whoDied = battle(enemy_spawn(levelBoss), genChar)
gameOver(whoDied)

whoDied = battle(enemy_spawn(levelBoss), genChar)
gameOver(whoDied)