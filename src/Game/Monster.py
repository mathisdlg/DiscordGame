class Monster:
    def __init__(self, Stats: list, name:str=None, boss:bool=False, berserk:bool=False):
        self.name = name
        self.stats = Stats
        self.boss = boss
        self.berserk = berserk
        