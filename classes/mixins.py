import time
import os
import sys


class TypeWriter():
    """
    Typewiter Animation
    """
    @staticmethod
    def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)

    @staticmethod
    def typingInput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        value = input()
        return value


class ClearDisplayMixin():
    """
    Contains a static function to be used across multiple classes
    """
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    @staticmethod
    def clear_display():
        """"
        Clears the console
        """
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
