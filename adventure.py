from pprint import pprint
import colorama
from colorama import Fore, Style
from getch import pause
import functions
import ascii_art
import story
colorama.init(autoreset=True)


def path_choice(choice, select_1, select_2,
                error, function_1, function_2, *args):
    '''
    Function used throughout the game to
    direct the story depending on your choice.
    '''
    choice = input(Fore.GREEN + choice).lower().strip(" ")
    if choice == select_1:
        function_1(*args)
    elif choice == select_2:
        function_2(*args)
    else:
        print(Fore.GREEN + error)
        path_choice(choice, select_1, select_2,
                    error, function_1, function_2, *args)
        print(Style.RESET_ALL)


def act_1():
    '''
    Asks you to begin the game, prints the first
    paragraph and loads the first choice.
    '''
    # functions.clear_display()
    # character = functions.gen_char()
    # functions.clear_display()
    # print(Fore.GREEN + ascii_art.STATS)
    # print(f"{Fore.GREEN}Your Guardians Stats")
    # print(f"{Fore.GREEN}--------------------")
    # stats = vars(character)
    # for key, value in stats.items():
    #     pprint(f"{key.capitalize()} : {value}")
    # pause(f"\n{Fore.CYAN}{Style.BRIGHT}\nPress any key to continue...")
    functions.clear_display()
    print(Fore.GREEN + ascii_art.ACT_1)
    print(story.IO)
    path_choice('        Would you like to go through Jungle'
                ' or Village? Enter J or V:\n        ',
                'j',
                'v',
                '        Error - Please enter J or V:',
                jungle, village)


def jungle():
    pass


def village():
    pass

act_1()