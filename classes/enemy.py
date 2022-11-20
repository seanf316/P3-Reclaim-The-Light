"""
Enemy Class
"""


class Enemy:
    """
    Creates the Enemy object
    *"e" refers to Enemy
    """
    def __init__(self, e_health, e_attack, e_chance, e_name):
        self.health = e_health
        self.attack = e_attack
        self.chance = e_chance
        self.name = e_name

    def get_e_health(self):
        """
        Gets Enemy current health stat
        """
        return self.health

    def get_e_attack(self):
        """
        Gets Enemy current close attack stat
        """
        return self.attack

    def get_e_chance(self):
        """
        Gets Enemy current defense stat
        """
        return self.chance

    def get_e_name(self):
        """
        Gets Enemy current defense stat
        """
        return self.name

    def set_e_health(self, new_health):
        """
        Gets Enemy current health stat
        """
        self.health = new_health

    def set_e_attack(self, new_attack):
        """
        Gets Enemy current close attack stat
        """
        self.attack = new_attack

    def set_e_chance(self, new_chance):
        """
        Gets Enemy current magic attack stat
        """
        self.chance = new_chance

    def set_e_name(self, new_enemy_name):
        """
        Gets Enemy current defense stat
        """
        self.name = new_enemy_name


class Boss(Enemy):
    """
    Subclass of enemy for Bosses
    """
    def __init__(self, e_health, e_attack, e_chance, e_name,
                 e_super):
        super().__init__(e_health, e_attack, e_chance, e_name)
        self.super = e_super

    def get_boss_super(self):
        """
        Gets Boss super move stat
        """
        return self.super

    def set_boss_super(self, new_boss_super):
        """
        Gets Boss super move stat
        """
        self.super = new_boss_super
