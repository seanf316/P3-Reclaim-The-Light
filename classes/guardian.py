class Guardian:
    """
    Creates the Guardian object
    *"g" refers to Guardian
    """
    def __init__(self, g_heatlh, g_close_attack, g_ranged_attack,
                 g_magic_attack, g_defense, g_luck, g_name):
        self.heatlh = g_heatlh
        self.close_attack = g_close_attack
        self.ranged_attack = g_ranged_attack
        self.magic_attack = g_magic_attack
        self.defense = g_defense
        self.luck = g_luck
        self.guardian_name = g_name

    def get_health(self):
        """
        Gets Guardian current health stat
        """
        return self.heatlh

    def get_close_attack(self):
        """
        Gets Guardian current close attack stat
        """
        return self.close_attack

    def get_ranged_attack(self):
        """
        Gets Guardian current ranged attack stat
        """
        return self.ranged_attack

    def get_magic_attack(self):
        """
        Gets Guardian current magic attack stat
        """
        return self.magic_attack

    def get_defense(self):
        """
        Gets Guardian current defense stat
        """
        return self.defense

    def get_luck(self):
        """
        Gets Guardian current defense stat
        """
        return self.luck

    def set_health(self, new_health):
        """
        Gets Guardian current health stat
        """
        self.heatlh = new_health

    def set_close_attack(self, new_close_attack):
        """
        Gets Guardian current close attack stat
        """
        self.close_attack = new_close_attack

    def set_ranged_attack(self, new_ranged_attack):
        """
        Gets Guardian current ranged attack stat
        """
        self.ranged_attack = new_ranged_attack

    def set_magic_attack(self, new_magic_attack):
        """
        Gets Guardian current magic attack stat
        """
        self.magic_attack = new_magic_attack

    def set_defense(self, new_defense):
        """
        Gets Guardian current defense stat
        """
        self.defense = new_defense

    def set_luck(self, new_luck):
        """
        Gets Guardian current defense stat
        """
        self.luck = new_luck
