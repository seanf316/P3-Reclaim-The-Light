class Enemy:
    """
    Creates the Enemy object
    *"e" refers to Enemy
    """
    def __init__(self, e_heatlh, e_attack, e_chance, e_name):
        self.heatlh = e_heatlh
        self.attack = e_attack
        self.chance = e_chance
        self.enemy_name = e_name

    def get_health(self):
        """
        Gets Enemy current health stat
        """
        return self.heatlh

    def get_attack(self):
        """
        Gets Enemy current close attack stat
        """
        return self.attack

    def get_chance(self):
        """
        Gets Enemy current defense stat
        """
        return self.chance

    def get_enemy_name(self):
        """
        Gets Enemy current defense stat
        """
        return self.enemy_name()

    def set_health(self, new_health):
        """
        Gets Enemy current health stat
        """
        self.heatlh = new_health

    def set_attack(self, new_attack):
        """
        Gets Enemy current close attack stat
        """
        self.attack = new_attack

    def set_chance(self, new_chance):
        """
        Gets Enemy current magic attack stat
        """
        self.chance = new_chance

    def set_enemy_name(self, new_enemy_name):
        """
        Gets Enemy current defense stat
        """
        self.enemy_name = new_enemy_name


class Boss(Enemy):
    """
    Subclass of enemy for Bosses
    """
    def __init__(self, e_heatlh, e_attack, e_chance, e_name,
                 e_super):
        super().__init__(e_heatlh, e_attack, e_chance, e_name)
        self.boss_super = e_super

    def get_boss_super(self):
        """
        Gets Boss super move stat
        """
        return self.boss_super

    def set_boss_super(self, new_boss_super):
        """
        Gets Boss super move stat
        """
        self.boss_super = new_boss_super
