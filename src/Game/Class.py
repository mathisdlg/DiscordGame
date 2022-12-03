CLASS_LIST = ["Thief", "Priest", "Mage", "Figther", "Paladin", "Ranger", "Druid", "Black Mage", "Labyrinths Master", "Berserker", "Assasin", "Bard", "Cleric", "Hunter", "Villager", "Beast Master", "Artificer", "Craftsman", "Alchemist", "Wizard", "Bettor", "Dragon Slayer"]


def choose_class():
    while True:
        class_ = input("Enter your class: ")
        if class_ in CLASS_LIST:
            return class_


class Class:
    """
    Class:
        - Thief
        - Priest
        - Mage
        - Figther
        - Paladin
        - Ranger
        - Druid
        - Black Mage
        - Labyrinths Master
        - Berserker
        - Assasin
        - Bard
        - Cleric
        - Hunter
        - Villager
        - Beast Master
        - Artificer
        - Craftsman
        - Alchemist
        - Wizard
        - Bettor
        - Dragon Slayer
        
    """

    def __init__(self, name, side):
        self.class_name = name
        self.side = side


class Thief(Class):
    
    def __init__(self):
        self.class_name = "Thief"
        self.side = "darkness"
        self.bonus_stat = [] #TODO
        self.special_skill = [] #TODO
        
        Class().__init__(self.class_name, self.side)


class Paladin(Class):
    
    def __init__(self):
        self.class_name = "Paladin"
        self.side = "light"
        self.bonus_stat = [] #TODO
        self.special_skill = [] #TODO
        
        Class().__init__(self.class_name, self.side)