"""
Reclaim The Light Adventure Game
"""

from getch import pause
import colorama
from colorama import Fore, Style
import ascii_art
import functions
import adventure

colorama.init(autoreset=True)


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
            adventure.act_1()
        elif choices == "m":
            menu = False
            functions.clear_display()
            mission_log()
        elif choices == "a":
            menu = False
            about()
        else:
            print("That was an invalid input, please enter S,M,I")


def mission_log():
    """
    Povides the player with a mission log for the game
    """
    functions.clear_display()
    print(Fore.GREEN + ascii_art.MISSION_LOG)
    functions.typing_print(
        "\nThe last city was attacked by the colition of Darkness.\n"
        "Their aim was to acquire the last city's light crystal the source\n"
        "of sustainable power that has allowed us to survive for so long.\n"
        "Our intel tells us that the crystal was brought to IO and we need\n"
        "you to go there and retreive it. Beware IO is very hostile with\n"
        "alot of dangerous foe lerking in the shadows, be careful Guardian\n"
        "the city wont last without the light crstal.\n"
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
    print(Fore.GREEN + ascii_art.ABOUT)
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
        'A Mage likes to stick to their magic attacks when fightingfoes but\n'
        'is not afraid to use a weapon, they have the best in class magic\n'
        'attack & a good ranged stat but fall away when it comes to close\n'
        'attack or defense.\n')
    pause(f"{Fore.CYAN}{Style.BRIGHT}Press any key to continue....")
    functions.clear_display()
    welcome_screen()
