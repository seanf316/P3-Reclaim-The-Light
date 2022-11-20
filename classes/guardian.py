"""
Guardian Class
"""


class Guardian:
    """
    Creates the Guardian object
    *"g" refers to Guardian
    """
    def __init__(self, g_attack, g_defence, g_health, g_luck, g_magic,
                 g_ranged, g_name):
        self.attack = g_attack
        self.defence = g_defence
        self.health = g_health
        self.luck = g_luck
        self.magic = g_magic
        self.ranged = g_ranged
        self.name = g_name

    def get_health(self):
        """
        Gets Guardian current health stat
        """
        return self.health

    def get_attack(self):
        """
        Gets Guardian current close attack stat
        """
        return self.attack

    def get_ranged(self):
        """
        Gets Guardian current ranged attack stat
        """
        return self.ranged

    def get_magic(self):
        """
        Gets Guardian current magic attack stat
        """
        return self.magic

    def get_defence(self):
        """
        Gets Guardian current defence stat
        """
        return self.defence

    def get_luck(self):
        """
        Gets Guardian current defence stat
        """
        return self.luck

    def get_name(self):
        """
        Gets Guardian current defence stat
        """
        return self.name

    def set_health(self, new_health):
        """
        Gets Guardian current health stat
        """
        self.health = new_health

    def set_attack(self, new_attack):
        """
        Gets Guardian current close attack stat
        """
        self.attack = new_attack

    def set_ranged(self, new_ranged):
        """
        Gets Guardian current ranged attack stat
        """
        self.ranged = new_ranged

    def set_magic(self, new_magic):
        """
        Gets Guardian current magic attack stat
        """
        self.magic = new_magic

    def set_defence(self, new_defence):
        """
        Gets Guardian current defence stat
        """
        self.defence = new_defence

    def set_luck(self, new_luck):
        """
        Gets Guardian current defence stat
        """
        self.luck = new_luck

    def set_name(self, new_name):
        """
        Gets Guardian current defence stat
        """
        self.name = new_name
