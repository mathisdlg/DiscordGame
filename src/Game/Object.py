class Object:
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
    def __init__(self, objet_name, rarity):
        self.objet_name = objet_name


class Sword(Object):
    
    def __init__(self, objet_name, rarity):
        Object.__init__(self, objet_name, rarity)
        self.range = "Melee"


class Ego():
    
    def __init__(self):
        pass