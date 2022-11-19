class Guardian:
    """
    Creates the Guardian object
    *"g" refers to Guardian
    """
    def __init__(self, Gattack, Gdefence, Ghealth, Gluck, Gmagic, Granged,
                 Gname):
        self.attack = Gattack
        self.defence = Gdefence
        self.health = Ghealth
        self.luck = Gluck
        self.magic = Gmagic
        self.ranged = Granged
        self.name = Gname

    def getHealth(self):
        """
        Gets Guardian current health stat
        """
        return self.health

    def getAttack(self):
        """
        Gets Guardian current close attack stat
        """
        return self.attack

    def getRanged(self):
        """
        Gets Guardian current ranged attack stat
        """
        return self.ranged

    def getMagic(self):
        """
        Gets Guardian current magic attack stat
        """
        return self.magic

    def getDefence(self):
        """
        Gets Guardian current defence stat
        """
        return self.defence

    def getLuck(self):
        """
        Gets Guardian current defence stat
        """
        return self.luck

    def getName(self):
        """
        Gets Guardian current defence stat
        """
        return self.name

    def setHealth(self, newHealth):
        """
        Gets Guardian current health stat
        """
        self.health = newHealth

    def setAttack(self, newAttack):
        """
        Gets Guardian current close attack stat
        """
        self.attack = newAttack

    def setRanged(self, newRanged):
        """
        Gets Guardian current ranged attack stat
        """
        self.ranged = newRanged

    def setMagic(self, newMagic):
        """
        Gets Guardian current magic attack stat
        """
        self.magic = newMagic

    def setDefence(self, newDefence):
        """
        Gets Guardian current defence stat
        """
        self.defence = newDefence

    def setLuck(self, newLuck):
        """
        Gets Guardian current defence stat
        """
        self.luck = newLuck

    def setName(self, newName):
        """
        Gets Guardian current defence stat
        """
        self.name = newName
