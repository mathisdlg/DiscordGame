class Object:
    """
    Objet:
        - Sword                     (Weapon)
        - Ring                      (Armor)
        - Katana                    (Weapon)
        - Book                      (Armor)
        - Helmet                    (Armor)
        - Armor                     (Armor)
        - mage staff                (Weapon)
        - wish ring                 (Object)
        - Bow                       (Weapon)
        - Baguette                  (Weapon)
        - Shield                    (Weapon)
        - Boots                     (Armor)
        - Champagne                 (Object)
        - Hat                       (Armor)
        - potion of life            (Object)
        - doppleganger potion       (Object)
        - HP Potion                 (Object)
        - MP Potion                 (Object)
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