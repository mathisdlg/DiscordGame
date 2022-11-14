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
    def __init__(self, p_name, classe, race):
        self.name = p_name
        self.classe = classe
        self.race = race
        self.level = 0
        self.stat_point = 0
        self.stats = {"PV": 100, "PM": 100, "STR": 1, "AG": 1, "INT": 1, "WIS": 1, "LUK": 1}
    
    def __str__(self) -> str:
        return self.name
    
    def __format__(self, __format_spec: str) -> str:
        return self.name
    
    def win_level(self, nb):
        self.level +=nb
    
    def win_stat_point(self, nb):
        self.stat_point += nb
    
    def say_hello(self, p_hello):
        print("Hello {}".format(p_hello))
        return 0