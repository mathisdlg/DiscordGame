RACE_LIST = ['Human', 'Elf', 'Dwarf', 'Vampire', 'Fairy', 'Leprechaun', 'Orc', 'Halfelin', 'Dragon', 'Robot', 'Cyborg', 'Zombie', 'Cyclops', 'Giant', 'Black Elf', 'Half-Demon']

def choose_race():
    while True:
        race_ = input("Enter your race: ")
        if race_ in RACE_LIST:
            return race_


class Race:
    """
    """
    def __init__(self, race_name):
        self.race_name = race_name
        self.race_level = 0