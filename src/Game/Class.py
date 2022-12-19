CLASS_LIST = ['Thief', 'Priest', 'Mage', 'Figther', 'Paladin', 'Ranger', 'Druid', 'Black Mage', 'Labyrinths Master', 'Berserker', 'Assassin', 'Bard', 'Cleric', 'Hunter', 'Villager', 'Beast Master', 'Artificer', 'Craftsman', 'Alchemist', 'Wizard', 'Bettor', 'Dragon Slayer', 'Blacksmith', 'Necromancer', 'Warlock', 'Elementalist', 'Ninja', 'Monk', 'Crusader', 'Demolitionist']


def choose_class():
    while True:
        class_ = input("Enter your class: ")
        if class_ in CLASS_LIST:
            return class_


class Class:
    """
    Class:
    """
    def __init__(self, name):
        self.class_name = name
        self.class_level = 0