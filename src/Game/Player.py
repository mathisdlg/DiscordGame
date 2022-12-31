from Game.Class import Class
from Game.Race import Race

class Player:
    """
    Player:
        - name
        - Classe
        - Race
        - Level
        - Stat point
        - Statistics:
            - HP
            - MP
            - Strength
            - Defense
            - Agility
            - Dodge
            - Intelligence
            - Wisdom
            - Luck
        - clan

    """
    def __init__(self, p_name, classe: Class, race: Race):
        self.name = p_name
        self.classe = classe
        self.race = race
        self.level = 0
        self.stat_point = 0
        self.stats = {"HP": 100, "MP": 10, "STR": 1, "DEF":10, "AG": 1, "DODG": 1, "INT": 1, "WIS": 1, "LUK": 1}
        clan = None
    
    def __str__(self) -> str:
        return self.name
    
    def __format__(self, __format_spec: str) -> str:
        return self.name
    
    def win_level(self, nb: int):
        self.level += nb
    
    def win_stat_point(self, nb: int):
        self.stat_point += nb
    
    def say_hello(self, p_hello):
        print(f"Hello {p_hello.name}")
        return 0


    ########################################################
    #                   Get method                         #
    def get_name(self):
        return self.name
    
    def get_class(self):
        return self.classe
    
    def get_race(self):
        return self.race
    
    def get_level(self):
        return self.level
    
    def get_stat_point(self):
        return self.stat_point
    
    def get_stats(self):
        return self.stats
    
    def get_clan(self):
        return self.clan
    ########################################################


    ########################################################
    #                   Set method                         #
    def set_clan(self, clan_name):
        self.clan = clan_name
        return 0
    
    def set_stats(self, stats):
        pass #TODO
    ########################################################
    
    def duel(self, opponent, type):
        pass #TODO