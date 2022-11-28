CLASS_LIST = ["Thief", "Priest", "Mage", "Figther", "Paladin", "Ranger", "Druid", "Black Mage", "Labyrinths Master", "Berserker", "Assasin", "Bard", "Cleric", "Hunter", "Villager", "Beast Master", "Artificer", "Craftsman", "Alchemist", "Wizard"]


def choose_class():
    while True:
        class_ = input("Enter your class:")
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

    Bonus stat:
        - 
    """

    def __init__(self):
        pass
    
    def set_class(self, class_):
        if class_ in CLASS_LIST:
            self.class_name = class_
            return 0
        else:
            return 1
