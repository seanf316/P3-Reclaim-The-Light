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
    print(Fore.GREEN + ascii_art.TITLE)

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
            act_1()
        elif choices == "m":
            menu = False
            functions.clear_display()
            mission_log()
        elif choices == "a":
            menu = False
            functions.clear_display()
            about()
        else:
            print("That was an invalid input, please enter S,M,I\n")


def mission_log():
    """
    Povides the player with a mission log for the game
    """
    functions.clear_display()
    print(Fore.GREEN + Style.BRIGHT + ascii_art.MISSION_LOG)
    functions.typing_print(
        "\nThe last city was attacked by the colition of Darkness.\n"
        "Their aim was to acquire the last city's light crystal the source\n"
        "of sustainable power that has allowed us to survive for so long.\n"
        "Our intel tells us that the crystal was brought to Nessus and we\n"
        "need you to go there and retreive it. Beware Nessus is very hostile\n"
        "with alot of dangerous foe lerking in the shadows, be careful\n"
        "Guardian the city wont last without the light crstal.\n"
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
        "of the story is changed based off the user's choices throughout.\n"
        "\n1. You will need to input a name for your Guardian\n"
        "2. You will need to select a Guardian class.\n"
        "3. Make choices and have fun!.\n"
    )
    print('\033[1;4m' + 'Guardian Classes' + '\033[0m')
    print(
        f'\n{Fore.GREEN}{Style.BRIGHT}Warrior:\n{Style.RESET_ALL}'
        'The most physically powerful of the 3 classes, they have high\n'
        'attack & defense stats but fall away when it comes to ranged\n'
        'or magic attack.\n'
        f'\n{Fore.GREEN}{Style.BRIGHT}Assassin:\n{Style.RESET_ALL}'
        'As the name suggests they are the stealthiest of the 3 classes,\n'
        'they havea high ranged attack & a good defense stat but fall away\n'
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
    choice = input(Fore.GREEN + Style.BRIGHT + choice).lower().strip(" ")
    if choice == select_1:
        function_1()
    elif choice == select_2:
        function_2()
    else:
        print(error)
        path_choice(choice, select_1, select_2, error, function_1, function_2)
    print(Style.RESET_ALL)


def act_1():
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
    path_choice('\nInvestigate outpost or Continue on the jungle path? '
                'Enter I or C:\n',
                'i',
                'c',
                'Invalid input - Enter I or C: ',
                encounter_1, village)


def village():
    """
    Function for Village narrative
    """


def encounter_1():
    """
    Function for 1st Enemy encounter
    """
    functions.clear_display()
    functions.typing_print(story.ENCOUNTER_1)
    time.sleep(.75)
    functions.clear_display()
    print(Fore.RED + Style.BRIGHT + ascii_art.ENCOUNTER_1)
    time.sleep(.75)
    functions.clear_display()
    functions.typing_print('What was that? the outpost is now little but there'
                           'is something hiding in the shadows you approach'
                           ' and you see that\n')
    enemy = functions.gen_enemy()
    functions.battle(enemy, character)
    pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    jungle()


def main():
    welcome_screen()


main()
