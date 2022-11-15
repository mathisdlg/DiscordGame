from Game_mod import *

class Player:
    """
    Player:
        - name
        - Classe
        - Race
        - Level
        - Stat point
        - Statistics:
            - PV
            - PM
            - Strenght
            - Agility
            - Intelligence
            - Wisdom
            - Luck

    """
    def __init__(self, p_name, classe: Class, race: Race):
        self.name = p_name
        self.classe = classe
        self.race = race
        self.level = 0
        self.stat_point = 0
        self.stats = {"PV": 100, "PM": 10, "STR": 1, "AG": 1, "INT": 1, "WIS": 1, "LUK": 1}
    
    def __str__(self) -> str:
        return self.name
    
    def __format__(self, __format_spec: str) -> str:
        return self.name
    
    def win_level(self, nb: int):
        self.level +=nb
    
    def win_stat_point(self, nb: int):
        self.stat_point += nb
    
    def say_hello(self, p_hello: Player):
        print("Hello {}".format(p_hello))
        return 0
    
    def save_player(self):
        pass
    
    def load_player(self):
        pass