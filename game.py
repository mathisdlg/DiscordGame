import random

"""
module game for prog(r)amer's discord server
"""


class Player:
    """
    Player:
        - name
        - Classe
        - Race
        - Level
        - Statistics:
            - PV
            - PM
            - Strenght
            - Agility
            - intelligence
            - Wisdom
            - Luck

    """
    def __init__(self, p_name, classe, race):
        self.name = p_name
        self.classe = classe
        self.race = race
        self.level = 0
        self.stats = {"PV": 100, "PM": 100, "STR": 1, "AG": 1, "INT": 1, "WIS": 1, "LUK": 1}
    
    def __str__(self) -> str:
        return self.name
    
    def __format__(self, __format_spec: str) -> str:
        return self.name
    
    def say_hello(self, p_hello):
        print("Hello {}".format(p_hello))
        return 0



class Objet:
    """
    Objet:
        - Epée
        - Bague
        - Katana
        - Livre
        - Casque
        - Armure
        - Baton de mage
        - Anneau de souhat
        - Arc
        - Baguette
        - Armure
        - Bouclier
        - Bottes
        - Champagne
        - Chapeau
        - Potion de vie
        - Potion de doppleganger
        - Potion de PM
        - 
    Bonus stat:
        - 
    """
    def __init__(self, objet_name):
        self.objet_name = objet_name



class Job:
    """
    Job:
        - Professeur
        - Journaliste
        - Programmers
        - Gamer
        - 
    Bonus stat:
        - 
    """
    def __init__(self, job_name):
        self.job_name = job_name



class Classe:
    """
    Classe:
        - Voleur
        - Prètre
        - Mage
        - Gerrier
        - Prêtre
        - 
    
    Bonus stat:
        - 
    """
    def __init__(self, classe_name):
        self.classe_name = classe_name



class Race:
    """
    Race:
        - Humain
        - Elfe
        - Nain
        - Sang-mélée
        - Vampires
        - 
    Bonus stat:
        - 
    """
    def __init__(self, race_name):
        self.race_name = race_name




if __name__ == '__main__':
    player = Player("Mathis")
    player_michel = Player("Michel")
    player.say_hello(player_michel)