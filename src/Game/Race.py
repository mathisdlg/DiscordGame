RACE_LIST = ['Human', 'Elf', 'Dwarf', 'Vampire', 'Fairy', 'Leprechaun', 'Orc', 'Halfelin', 'Dragon', 'Robot', 'Cyborg', 'Zombie', 'Cyclops', 'Giant', 'Black Elf', 'Half-Demon', 'Troll', 'Metamorph']


def display_races():
    for race in RACE_LIST:
        print(f"{race}")

def choose_race():
    while True:
        race_ = input("Enter your race[h to see all races]: ")
        if race_ in RACE_LIST:
            return race_
        elif race_ == 'h':
            display_races()
        else:
            print("Invalid race: {} not found!".format(race_))



class Race:
    """
    """
    def __init__(self, race_name):
        self.race_name = race_name
        self.race_level = 0