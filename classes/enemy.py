class Enemy:
    """
    Creates the Enemy object
    *"e" refers to Enemy
    """
    def __init__(self, EHealth, EAttack, EChance, EName):
        self.health = EHealth
        self.attack = EAttack
        self.chance = EChance
        self.name = EName

    def getEHealth(self):
        """
        Gets Enemy current health stat
        """
        return self.health

    def getEAttack(self):
        """
        Gets Enemy current close attack stat
        """
        return self.attack

    def getEChance(self):
        """
        Gets Enemy current defense stat
        """
        return self.chance

    def getEName(self):
        """
        Gets Enemy current defense stat
        """
        return self.name

    def setEHealth(self, new_health):
        """
        Gets Enemy current health stat
        """
        self.health = new_health

    def setEAttack(self, new_attack):
        """
        Gets Enemy current close attack stat
        """
        self.attack = new_attack

    def setEChance(self, new_chance):
        """
        Gets Enemy current magic attack stat
        """
        self.chance = new_chance

    def setEName(self, new_enemy_name):
        """
        Gets Enemy current defense stat
        """
        self.name = new_enemy_name


class Boss(Enemy):
    """
    Subclass of enemy for Bosses
    """
    def __init__(self, EHealth, EAttack, EChance, EName,
                 ESuper):
        super().__init__(EHealth, EAttack, EChance, EName)
        self.super = ESuper

    def getBSuper(self):
        """
        Gets Boss super move stat
        """
        return self.super

    def setBSuper(self, new_boss_super):
        """
        Gets Boss super move stat
        """
        self.super = new_boss_super
