RACE_LIST = ["Humain", "Elve", "Dwarf", "Vampire", "Fairy", "Leprechaun", "Orc", "Halfelin", "Dragon", "Robot", "Cyborg"]

def choose_race():
    while True:
        race_ = input("Enter your race: ")
        if race_ in RACE_LIST:
            return race_


class Race:
    """
    Race:
        - Humain
        - Elve
        - Dwarf
        - Vampires
        - Fairy
        - Leprechaun
        - Orc
        - Halfelin
        - Dragon
        - Robot
        - Cyborg
        - 
    Bonus stat:
        - 
    """
    def __init__(self, race_name):
        self.race_name = race_name