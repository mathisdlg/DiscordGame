import random

"""
module game for programer's discord server
"""


class Player:
    """
    Player:

    """
    def __init__(self, p_name):
        self.name = p_name
    
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
    def __init__(self):
        pass



class Job:
    """
    Job:
        - Professeur
        - Journaliste
        - 
    """



class Classe:
    """
    Classe:
        - Voleur
        - Prètre
        - Mage
        - Gerrier
        - 
    """
    def __init__(self):
        pass



class Race:
    """
    Race:
        - Humain
        - Elfe
        - Nain
        - 
    """
    def __init__(self):
        pass




if __name__ == '__main__':
    player = Player("Mathis")
    player_michel = Player("Michel")
    player.say_hello(player_michel)