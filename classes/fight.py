import random
import math
import time
from pprint import pprint
import colorama
from .guardian import Guardian
from .enemy import Enemy, Boss
from .mixins import ClearDisplayMixin, TypeWriter 
from colorama import Fore
colorama.init(autoreset=True)


class Fight:
    
    def __init__(self, battle):
        self.battle = self.battle()

    def genEnem(self, level_boss):
        """
        Spawn a random enemy or boss and assigns stats
        """
        file = open('enemy.txt', 'r', encoding="utf8")
        lines = file.readlines()
        enemy = lines[random.randint(0, len(lines)-1)][:-1]
        file.close()
        file = open('boss.txt', 'r', encoding="utf8")
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

    def strike_chance(self, luck):
        """
        Sets up Guardian attack and uses random to see if successful
        """
        strike = random.randint(0, 4)
        if luck < strike:
            print("You missed!")
            return False

        else:
            return True

    def enemyAttack(self, strike_chance, attack_value, name, defence):
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

    def isDead(self, health):
        """
        Checks if Guardian or Enemy has died
        """
        if health < 1:
            return True
        else:
            return False

    def loot(self, luck, genChar):
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
            file = open(itemType, "r", encoding="utf8")
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

        def gameOver(self, enemyDead):
            if enemyDead:
                print("Congratulations Guardian you have slain")
            else:
                print("The foul beast has struck you down Guardian....")

        def battle(self, genEnem, genChar):
            print(f"Its... {Fore.RED}{genEnem.getEName()}{Fore.WHITE}"
                f", and they look ready for a fight!\n")
            print(f"Check out {Fore.RED}{genEnem.getEName()}'s{Fore.WHITE} stats...\n")
            stats = vars(genEnem)
            for key, value in stats.items():
                pprint(f"{key.capitalize()} : {value}")

            battle = True

            while battle:
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
                    ClearDisplayMixin.clear_display()
                    damage = genChar.getAttack()

                elif choice == "r":
                    damage = genChar.getRanged()

                else:
                    damage = genChar.getMagic()

                TypeWriter.typingPrint("You wind up for the attack!!...\n")
                time.sleep(0.8)
                strike = strike_chance(genChar.getLuck())

                if strike:
                    genEnem.setEHealth(genEnem.getEHealth() - damage)
                    print(f"You struck the enemy, {Fore.RED}{genEnem.getEName()}'s"
                        f" blood gushes....\n")
                    print(genEnem.getEName(), 's health is now', genEnem.getEHealth())

                else:
                    print("Enemy dodged your attack")

                enemyDead = isDead(genEnem.getEHealth())

                if not enemyDead:
                    genChar.setHealth(genChar.getHealth() - enemyAttack
                                    (genEnem.getEChance(),
                                    genEnem.getEAttack(),
                                    genEnem.getEName(),
                                    genChar.getDefence()))

                    guardianDead = isDead(genChar.getHealth())

                    if guardianDead:
                        battle = False
                        return False

                    else:
                        print("Guardian's remaining health is....",
                            genChar.getHealth())

                else:
                    battle = False
                    print(genEnem.getEName(), "has been slain")
                    loot(genChar.getLuck(), genChar)
                    return True
