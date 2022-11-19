import time
import os
import sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clear_display():
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
