import random

"""
module game for programer's discord server
"""


class Player:
    """
    Player:
        - name
        - Classe
        - Race

    """
    def __init__(self, p_name, classe, race):
        self.name = p_name
        self.classe = classe
        self.race = race
    
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
        - épée
        - bague
        - katana
        - livre
        - casque
        - armure
        - baton de mage
        - 
    """
    def __init__(self, objet_name):
        self.objet_name = objet_name



class Job:
    """
    Job:
        - Professeur
        - Journaliste
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
        - 
    """
    def __init__(self, race_name):
        self.race_name = race_name




if __name__ == '__main__':
    player = Player("Mathis")
    player_michel = Player("Michel")
    player.say_hello(player_michel)