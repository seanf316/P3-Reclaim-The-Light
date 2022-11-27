"""
Adventure Narrative Functions
"""


from pprint import pprint
import time
import colorama
from colorama import Fore, Style
from getch import pause
import functions
import ascii_art
import story
colorama.init(autoreset=True)

character = ''


def welcome_screen():
    """
    Displays Game title, provides mission log and game rules
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.TITLE)

    menu = True
    while menu:
        choices = input(f'Press {Fore.GREEN}{Style.BRIGHT}"S"{Style.RESET_ALL}'
                        f' to {Fore.GREEN}{Style.BRIGHT}Start{Style.RESET_ALL}'
                        f',{Fore.GREEN}{Style.BRIGHT} "M"{Style.RESET_ALL} for'
                        f' {Fore.GREEN}{Style.BRIGHT}Mission Log'
                        f'{Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}"A"'
                        f'{Style.RESET_ALL} for {Fore.GREEN}{Style.BRIGHT}'
                        f'About{Style.RESET_ALL}:\n').lower().strip(" ")
        if choices == "s":
            menu = False
            functions.clear_display()
            nessus()
        elif choices == "m":
            menu = False
            functions.clear_display()
            mission_log()
        elif choices == "a":
            menu = False
            functions.clear_display()
            about()
        else:
            print("That was an invalid input, please enter S,M or A\n")


def mission_log():
    """
    Povides the player with a mission log for the game
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.MISSION_LOG)
    functions.typing_print(
        "\nThe last city was attacked by the coalition of Darkness.\n"
        "Their aim was to acquire the last city's light crystal the source\n"
        "of sustainable power that has allowed us to survive for so long.\n"
        "Our intel tells us that the crystal was brought to Nessus and we\n"
        "need you to go there and retrieve it. Beware Nessus is very hostile\n"
        "with a lot of dangerous foes lurking in the shadows, be careful\n"
        "Guardian the city won't last without the light crystal.\n"
        "\nThe people of the last city are counting on you Guardian!\n"
        )
    pause(f"{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue....")
    functions.clear_display()
    welcome_screen()


def about():
    """
    Shows player the about section for the game
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.ABOUT)
    print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to Reclaim The Light")
    print(
        "\nReclaim The Light is a text adventure game where the outcome\n"
        "of the story is changed based on the user's choices throughout.\n"
        "\n1. You will need to input a name for your Guardian\n"
        "2. You will need to select a Guardian class.\n"
        "3. Make choices and have fun!\n"
    )
    print('\033[1;4m' + 'Guardian Classes' + '\033[0m')
    print(
        f'\n{Fore.GREEN}{Style.BRIGHT}Warrior:\n{Style.RESET_ALL}'
        'The most physically powerful of the 3 classes, they have high\n'
        'attack & defense stats but fall away when it comes to ranged\n'
        'or magic attack.\n'
        f'\n{Fore.GREEN}{Style.BRIGHT}Assassin:\n{Style.RESET_ALL}'
        'As the name suggests they are the stealthiest of the 3 classes,\n'
        'they have a high ranged attack & a good defense stat but fall away\n'
        'when it comes to close attack or magic attack.\n'
        f'\n{Fore.GREEN}{Style.BRIGHT}Mage:\n{Style.RESET_ALL}'
        'A Mage likes to stick to their magic attacks when fighting foes but\n'
        'is not afraid to use a weapon, they have the best in class magic\n'
        'attack & a good ranged stat but fall away when it comes to close\n'
        'attack or defense.\n')
    pause(f"{Fore.CYAN}{Style.BRIGHT}Press any key to continue....")
    functions.clear_display()
    welcome_screen()


def path_choice(choice, select_1, select_2,
                error, function_1, function_2):
    '''
    Function used throughout the game to
    direct the story depending on your choice.
    '''
    choice2 = input(Fore.GREEN + Style.BRIGHT + choice +
                    Style.RESET_ALL).lower().strip(" ")
    if choice2 == select_1:
        function_1()
    elif choice2 == select_2:
        function_2()
    else:
        print(error)
        path_choice(choice, select_1, select_2, error, function_1, function_2)
    print(Style.RESET_ALL)


def nessus():
    '''
    Asks you to begin the game, prints the first
    paragraph and loads the first choice.
    '''
    functions.clear_display()
    global character
    character = functions.gen_char()
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.STATS)
    print(f"{Fore.GREEN}{Style.BRIGHT}Your Guardians Stats")
    print(f"{Fore.GREEN}{Style.BRIGHT}--------------------")
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.NESSUS)
    functions.typing_print(story.NESSUS)
    path_choice('\nWould you like to go through the Jungle'
                ' or Village? Enter J or V:\n',
                'j',
                'v',
                'Invalid input - Enter J or V: ',
                jungle, village)


def jungle():
    """
    Function for Jungle narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.JUNGLE)
    functions.typing_print(story.JUNGLE)
    path_choice('\nInvestigate the Outpost or Continue on the jungle path? '
                'Enter I or C:\n',
                'i',
                'c',
                'Invalid input - Enter I or C: ',
                encounter_1, jungle_continue)


def jungle_continue():
    """
    Function for Jungle Continue Choice Narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.CAMP)
    functions.typing_print(story.JUNGLE_1)
    time.sleep(1)
    functions.sleep()
    time.sleep(1)
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.BANG)
    functions.typing_print(story.JUNGLE_2)
    path_choice('\nFight or Surrender? '
                'Enter F or S:\n',
                'f',
                's',
                'Invalid input - Enter F or S: ',
                encounter_3, surrender)


def village():
    """
    Function for Village narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.VILLAGE)
    functions.typing_print(story.VILLAGE)
    path_choice('\nOpen the box or Continue on the village path? '
                'Enter O or C:\n',
                'o',
                'c',
                'Invalid input - Enter O or C: ',
                encounter_2, weapons_depot)


def weapons_depot():
    """
    Function for Weapon Depot Narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.WEAPON)
    functions.typing_print(story.WEAPON_DEPOT)
    pause(f"{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.ENCOUNTER_2)
    functions.typing_print('You check the first chest and......\n')
    time.sleep(.7)
    functions.typing_print('\n...nothing unfortunately, lets move on.\n')
    time.sleep(.7)
    functions.typing_print('\nYou check the second chest and......\n')
    time.sleep(.7)
    functions.typing_print('\nBingo its......\n')
    functions.found_loot(character)
    functions.typing_print('\nYou check the third chest and......\n')
    time.sleep(.7)
    functions.typing_print('\nNice one its......\n')
    functions.found_loot(character)
    time.sleep(.7)
    functions.clear_display()
    functions.typing_print(story.WEAPON_DEPOT_1)
    time.sleep(.7)
    print(Fore.RED + Style.BRIGHT + ascii_art.BOOM)
    time.sleep(.7)
    functions.typing_print(story.WEAPON_DEPOT_2)
    path_choice('\nFight or Surrender? '
                'Enter F or S:\n',
                'f',
                's',
                'Invalid input - Enter F or S: ',
                encounter_4, surrender)


def encounter_1():
    """
    Function for 1st Enemy encounter
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.OUTPOST)
    functions.typing_print(story.ENCOUNTER_1)
    time.sleep(1)
    functions.clear_display()
    print(Fore.RED + Style.BRIGHT + ascii_art.BOOM)
    time.sleep(1)
    functions.clear_display()
    functions.typing_print('What was that? the outpost is now lit up there\n'
                           'is a table snapped in half laying on the ground\n'
                           'beside you. It was thrown by something or\n'
                           'someone, you look around the room and you see\n'
                           'something hiding in the shadows you approach and\n'
                           'you see that its a ......\n')
    time.sleep(1)
    enemy = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print(story.ENCOUNTER_1A)
    decison = input(f'\n{Fore.GREEN}{Style.BRIGHT}Enter "F" or '
                    f'S: {Style.RESET_ALL}\n').lower().strip(" ")
    while decison != 'f' and decison != 's':
        print('Invalid input - Please Enter "F" or "S"\n')
        input(f'\n{Fore.GREEN}{Style.BRIGHT}Enter "F" or '
              f'S: {Style.RESET_ALL}\n').lower().strip(" ")
    if decison == 'f':
        functions.typing_print(
            '\nOne of the creatures moves forward thirsting for blood,\n'
            'you see that its.....\n')
        enemy_1 = functions.gen_enemy()
        functions.battle(enemy_1, character)
        pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
        functions.clear_display()
        functions.typing_print(
            'One down one to go the second creature speaks...\n'
            'You will pay with your life guardian, it leaps into view\n'
            'its.....')
        enemy_2 = functions.gen_enemy()
        functions.battle(enemy_2, character)
        functions.typing_print(
            "\nThat's that done now its time to get to the mines....\n")
        pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    elif decison == "s":
        surrender()
    mines()


def encounter_2():
    """
    Function for free loot encounter
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.ENCOUNTER_2)
    functions.typing_print(story.ENCOUNTER_2)
    time.sleep(1.2)
    functions.found_loot(character)
    functions.typing_print("Wait there's another item in there its....\n")
    time.sleep(1.2)
    functions.found_loot(character)
    functions.typing_print("Thats a great haul I'm glad I stopped to open the "
                           "box.\n\n")
    print("Your new stats are:\n")
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    weapons_depot()


def encounter_3():
    """
    Function for 2nd Enemy encounter
    """
    functions.clear_display()
    functions.typing_print(story.ENCOUNTER_3)
    enemy = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy, character)
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.typing_print("\nThats one down 2 to go, the next enemy steps up "
                           "its a...")
    time.sleep(1)
    enemy1 = functions.gen_enemy()
    functions.battle(enemy1, character)
    functions.typing_print("\nYou stare at the 3rd enemy ready to fight...\n"
                           "they look in your eyes and retreat in fear, as\n"
                           "they run they drop an item its......\n\n")
    functions.found_loot(character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.typing_print("That was tough but I need to keep moving and get"
                           "to the mines....")
    mines()


def encounter_4():
    """
    Function for 3rd Enemy encounter
    """
    functions.clear_display()
    functions.typing_print(story.ENCOUNTER_4)
    time.sleep(1)
    enemy = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy, character)
    print("Your new stats are:\n")
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print('You took the first one out with ease, the second\n'
                           'enemy steps up its a.....')
    time.sleep(1)
    enemy1 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy1, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print('Thats two down, the creatures rage at the sight\n'
                           'of their fallen comrades. "You will pay for\n'
                           'their deaths Guardian", one of the enemies\n'
                           'jumps at you its a.....')
    time.sleep(1)
    enemy2 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy2, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print('Thats three down, the last creature shouts\n'
                           '"For the Darkness" and leaps at you its a....')
    time.sleep(1)
    enemy3 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy3, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print(story.ENCOUNTER_4A)
    time.sleep(.5)
    functions.sleep()
    time.sleep(.5)
    functions.sleep()
    time.sleep(.5)
    functions.clear_display()
    functions.typing_print('You wake up feeling much better lets get to the '
                           'mines.....\n')
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    mines()


def surrender():
    """
    Function to run the surrender narrative
    """
    functions.clear_display()
    functions.typing_print(story.SURRENDER)
    time.sleep(1)
    print(Fore.RED + Style.BRIGHT + ascii_art.GAME_OVER)
    print(f'{character.get_name()} you have been slain, the light crystal'
          f' is lost....')
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress "
          f"any key to return to homescreen")
    welcome_screen()


def mines():
    """
    Function to run the Mines narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.MINES)
    functions.typing_print(story.MINES_1)
    enemy = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print(
        '"You will pay for his death Guardian", the 2nd enemy leaps forward\n'
        'its a......\n')
    enemy1 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy1, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.BRIDGE)
    functions.typing_print(story.MINES_2)
    path_choice('\nFight or Surrender? '
                'Enter F or S:\n',
                'f',
                's',
                'Invalid input - Enter F or S: ',
                encounter_5, surrender)


def encounter_5():
    """
    Function for 4th Enemy encounter
    """
    functions.clear_display()
    functions.typing_print(
        'You dont hesitate, you raise your sword and\n'
        'charge at the first enemy in front of you it is a.....\n')
    enemy = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print(
        'You shake the blood from your sword and shout "Whos Next"\n'
        'one of the enemies behind you comes forward its a....\n')
    enemy1 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy1, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    functions.typing_print(
        'Another enemy leaps on your back in a rage, you throw the\n'
        'enemy off and see that its a....\n')
    enemy2 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy2, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    functions.clear_display()
    functions.typing_print(
        'You stare at the last enemy in your way and point your sword\n'
        '"Your next". The enemy raises their weapon and rushes towards you\n'
        'its a.....')
    enemy3 = functions.gen_enemy()
    time.sleep(1)
    functions.battle(enemy3, character)
    stats = vars(character)
    for key, value in stats.items():
        pprint(f"{key.capitalize()} : {value}")
    functions.typing_print(
        'Thats them all slain time to reclaim the light.....')
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    reclaim()


def reclaim():
    """
    Function for Reclaim Narrative
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.LIGHT)
    functions.typing_print(story.RECLAIM)
    time.sleep(1)
    functions.clear_display()
    functions.typing_print(story.RECLAIM_1)
    time.sleep(1)
    print(Fore.RED + Style.BRIGHT + ascii_art.BOSS)
    functions.typing_print(story.RECLAIM_2)
    time.sleep(1)
    functions.clear_display()
    boss = functions.gen_boss()
    functions.battle(boss, character)
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.RECLAIM)
    time.sleep(1)
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.RECLAIM_1)
    time.sleep(1)
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.THANKS)
    functions.typing_print(
        f'Thank you for playing {Fore.GREEN}{Style.BRIGHT}'
        f'{character.get_name()}, I hope you enjoyed your adventure.')
    pause(
        f'\n{Fore.CYAN}{Style.BRIGHT}\n'
        f'Press any key to return to the homescreen...')


def main():
    """
    Starts Adventure
    """
    welcome_screen()
